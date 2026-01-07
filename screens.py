from kivy.uix.screenmanager import Screen
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.list import OneLineAvatarIconListItem, IconLeftWidget, TwoLineAvatarListItem, ImageLeftWidget
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.filemanager import MDFileManager
from kivy.uix.image import Image
from kivy.uix.video import Video
from kivy.core.audio import SoundLoader
from kivy.properties import StringProperty, ObjectProperty
from kivy.network.urlrequest import UrlRequest
import os, json

# --- ПЛЕЕР ДЛЯ АУДИО (С КНОПКОЙ И НАЗВАНИЕМ) ---
class AudioPlayer(MDBoxLayout):
    source = StringProperty()
    sound = ObjectProperty(None, allownone=True)
    def play_audio(self):
        if not self.sound:
            self.sound = SoundLoader.load(self.source)
        if self.sound:
            if self.sound.state == 'stop':
                self.sound.play()
                self.ids.btn.icon = "pause"
            else:
                self.sound.stop()
                self.ids.btn.icon = "play"

# --- ЭКРАН ВВОДА IP (ПЕРВЫЙ ПРИ ВХОДЕ) ---
class ServerScreen(Screen):
    def connect(self):
        ip = self.ids.server_id.text.strip()
        if not ip:
            toast("Введите IP сервера")
            return
        # Авто-исправление формата под твой сервер 5000
        clean_ip = ip.replace("http://", "").split(":")[0]
        url = f"http://{clean_ip}:5000"
        MDApp.get_running_app().server_base_url = url
        
        toast("Проверка HTTP...")
        UrlRequest(url, on_success=self.go_next, on_error=self.fail, timeout=5)

    def go_next(self, req, result):
        self.manager.current = 'login'
        toast("Сервер найден")

    def fail(self, req, error):
        toast("Ошибка: Сервер не отвечает")

# --- ЭКРАН ЛОГИНА (ПРОВЕРКА АККАУНТА) ---
class LoginScreen(Screen):
    def do_login(self):
        app = MDApp.get_running_app()
        u = self.ids.user.text.strip()
        p = self.ids.pw.text.strip()
        
        # Проверка по локальной базе JsonStore
        if app.store.exists('accounts'):
            accounts = app.store.get('accounts')['data']
            if u in accounts and accounts[u] == p:
                app.username = u
                app.save_settings()
                self.manager.current = 'main'
            else:
                toast("Неверный логин или пароль")
        else:
            toast("Нет аккаунтов. Зарегистрируйтесь!")

# --- ЭКРАН РЕГИСТРАЦИИ (СОЗДАНИЕ АККАУНТА) ---
class RegisterAccScreen(Screen):
    def do_register(self):
        app = MDApp.get_running_app()
        u = self.ids.reg_user.text.strip()
        p = self.ids.reg_pw.text.strip()
        
        if len(u) < 3 or len(p) < 4:
            toast("Логин/Пароль слишком короткие")
            return
            
        accounts = app.store.get('accounts')['data'] if app.store.exists('accounts') else {}
        
        if u in accounts:
            toast("Логин занят")
        else:
            accounts[u] = p
            app.store.put('accounts', data=accounts)
            toast("Успешно! Теперь войдите")
            self.manager.current = 'login'

# --- ГЛАВНЫЙ ЭКРАН (СПИСОК КОМНАТ) ---
class MainScreen(Screen):
    def on_enter(self):
        self.ids.rooms_list.clear_widgets()
        app = MDApp.get_running_app()
        for name in app.all_rooms:
            it = OneLineAvatarIconListItem(text=name, on_release=lambda x, n=name: self.enter_room(n))
            it.add_widget(IconLeftWidget(icon="chat-outline"))
            self.ids.rooms_list.add_widget(it)
    
    def enter_room(self, name):
        self.manager.get_screen('chat_room').room_name = name
        self.manager.current = 'chat_room'

# --- ЭКРАН ЧАТА (ОТПРАВКА ТЕКСТА И ФАЙЛОВ) ---
class ChatRoomScreen(Screen):
    room_name = StringProperty("")
    
    def send_message(self, text=None, file_path=None):
        app = MDApp.get_running_app()
        txt = text or self.ids.msg_input.text.strip()
        if txt or file_path:
            msg = {"user": app.username, "nick": app.nickname, "text": txt, "file": file_path}
            # Отправка на Flask /send
            UrlRequest(f"{app.server_base_url}/send", req_body=json.dumps(msg))
            self.render_message(msg)
            self.ids.msg_input.text = ""

    def render_message(self, msg):
        app = MDApp.get_running_app()
        box = MDBoxLayout(orientation="vertical", adaptive_height=True, padding="10dp", spacing="5dp")
        item = TwoLineAvatarListItem(text=msg['nick'], secondary_text=msg['text'] or "")
        
        # Аватарка отправителя
        if msg['user'] == app.username and os.path.exists(app.avatar_path):
            item.add_widget(ImageLeftWidget(source=app.avatar_path))
        else:
            item.add_widget(IconLeftWidget(icon="account"))
        box.add_widget(item)

        # ПЛЕЕРЫ ДЛЯ ФАЙЛОВ
        f = msg.get('file')
        if f and os.path.exists(f):
            ext = os.path.splitext(f)[1].lower()
            if ext in ['.jpg', '.png', '.jpeg']:
                box.add_widget(Image(source=f, size_hint_y=None, height="250dp"))
            elif ext in ['.mp3', '.wav']:
                box.add_widget(AudioPlayer(source=f))
            elif ext in ['.mp4']:
                box.add_widget(Video(source=f, state='pause', size_hint_y=None, height="250dp"))
        self.ids.messages_list.add_widget(box)

    def open_file_manager(self):
        self.fm = MDFileManager(exit_manager=lambda x: self.fm.close(), select_path=self.select_file, preview=True)
        self.fm.show("/storage/emulated/0")

    def select_file(self, path):
        self.fm.close()
        self.send_message(file_path=path)

# --- ЭКРАН ПРОФИЛЯ (НИК И ФОТО) ---
class ProfileScreen(Screen):
    def choose_avatar(self):
        self.fm = MDFileManager(exit_manager=lambda x: self.fm.close(), select_path=self.set_avatar)
        self.fm.show("/storage/emulated/0")
    def set_avatar(self, path):
        app = MDApp.get_running_app()
        app.avatar_path = path
        app.save_settings()
        self.ids.avatar_preview.source = path
        self.fm.close()
    def save_profile(self):
        app = MDApp.get_running_app()
        app.nickname = self.ids.nick_field.text
        app.save_settings()
        toast("Профиль сохранен")

# --- ЭКРАН СОЗДАНИЯ КОМНАТЫ ---
class RegisterScreen(Screen):
    def create_room(self):
        n = self.ids.room_name.text.strip()
        if n:
            app = MDApp.get_running_app()
            app.all_rooms[n] = {"owner": app.username}
            app.save_settings()
            self.manager.current = 'main'
