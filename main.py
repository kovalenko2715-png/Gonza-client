from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.properties import StringProperty, DictProperty, ObjectProperty
from kivy.storage.jsonstore import JsonStore
from kivy.factory import Factory
import screens

class ChatApp(MDApp):
    username = StringProperty("")
    password = StringProperty("")
    nickname = StringProperty("Elite User")
    avatar_path = StringProperty("")
    server_base_url = StringProperty("")
    all_rooms = DictProperty({"Общий чат": {"owner": "admin"}})

    def build(self):
        self.store = JsonStore('settings.json')
        self.load_settings()
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Amber"
        
        # Регистрация всех классов
        for cls_name in dir(screens):
            cls = getattr(screens, cls_name)
            if isinstance(cls, type):
                Factory.register(cls_name, cls=cls)

        return Builder.load_file("gonza.kv")

    def load_settings(self):
        if self.store.exists('user'):
            d = self.store.get('user')
            self.username = d.get('name', "")
            self.nickname = d.get('nickname', "Elite User")
            self.avatar_path = d.get('avatar', "")

    def save_settings(self):
        self.store.put('user', name=self.username, nickname=self.nickname, avatar=self.avatar_path)

    def logout(self):
        self.root.ids.screen_manager.current = 'server'

if __name__ == '__main__':
    ChatApp().run()
