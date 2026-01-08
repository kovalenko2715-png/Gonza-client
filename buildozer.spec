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
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# Добавь сюда свои библиотеки через запятую
requirements = python3,kivy,hostpython3,requests,urllib3,certifi

# (str) Custom source folders for requirements
# садят версию cython, которую мы указали в workflow
# (int) Android API to use
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage (True) or --dir public storage (False)
android.private_storage = True

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 0

# (list) The Android architectures to build for
android.archs = arm64-v8a

# (bool) skip update of- the android sdk
android.skip_update = False

# (bool) Display warning if buildozer is run as root
warn_on_root = 1

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug (with command output))
log_level = 2

# (int) Display warning if buildozer is run as root
warn_on_root = 1
