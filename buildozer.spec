[app]

# (str) Title of your application
title = GonzaCloud

# (str) Package name
package.name = gonzacloud

# (str) Package domain
package.domain = org.gonza

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas

# (str) Application version
version = 0.1

# (list) Application requirements
requirements = python3,kivy,hostpython3,requests,urllib3,certifi

# (int) Android API to use
android.api = 33

# (int) Minimum API required
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) Use --private data storage
android.private_storage = True

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen or not
fullscreen = 0

# (list) The Android architectures to build for
android.archs = arm64-v8a

# (bool) skip update of the android sdk
android.skip_update = False

# (bool) Display warning if buildozer is run as root
warn_on_root = 1

[buildozer]

# (int) Log level (2 = debug)
log_level = 2

# (str) Path to build artifacts
bin_dir = ./bin
