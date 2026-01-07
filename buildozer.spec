[app]
title = Gonza Cloud
package.name = gonzacloud
package.domain = org.gonza
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 1.0

# Добавили openssl и requests для работы с HTTPS ссылками туннелей
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,requests,urllib3,openssl,certifi

orientation = portrait
fullscreen = 0

# РАЗРЕШЕНИЯ (Добавили чтение памяти для выбора файлов и интернет)
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, MANAGE_EXTERNAL_STORAGE

# ВАЖНО для туннелей: разрешаем любой трафик
android.uses_cleartext_traffic = True

# Архитектуры для современных смартфонов
android.archs = arm64-v8a, armeabi-v7a

# Чтобы клавиатура не перекрывала поле ввода в чате
android.window_softinput_mode = adjustPan

# Иконка (если есть, положи в папку icon.png)
# icon.filename = %(source.dir)s/icon.png

[buildozer]
log_level = 2
warn_on_root = 1
