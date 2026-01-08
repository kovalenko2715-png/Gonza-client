[app]

# (str) Title of your application
title = GonzaCloud

# (str) Package name
package.name = gonzacloud

# (str) Package domain (needed for android packaging)
package.domain = org.gonza

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include (let empty to include all the files)
source.include_exts = py,png,jpg,kv,json

# (str) Application versioning (method 1)
version = 0.1

# (list) Application requirements
# Добавлены все необходимые библиотеки для работы KivyMD и запросов через туннель
requirements = python3,kivy==2.2.1,kivymd==1.1.1,requests,urllib3,certifi,openssl,pillow

# (str) Presplash screen image
# presplash.filename = %(source.dir)s/data/presplash.png

# (str) Icon of the application
# icon.filename = %(source.dir)s/data/icon.png

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) Permissions
# Обязательно для работы с твоим сервером в Termux
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then skip trying to update the Android sdk
android.skip_update = False

# (bool) If True, then automatically accept SDK license
android.accept_sdk_license = True

# (str) The Android arch to build for.
# Для GitHub лучше оставить одну архитектуру, чтобы билд не шел вечно
android.archs = arm64-v8a

# (list) The Android themes to apply
android.theme = @android:style/Theme.NoTitleBar

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root (0 = off, 1 = on)
warn_on_root = 1
