[app]
title = GonzaCloud
package.name = gonzacloud
package.domain = org.gonza
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 0.1

# Временно убрали сложные требования, оставили только базу для проверки
requirements = python3,kivy==2.2.1,kivymd==1.1.1,pillow,requests

orientation = portrait
fullscreen = 0
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# Настройки для архитектуры
android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
