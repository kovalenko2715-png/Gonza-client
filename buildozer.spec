[app]
title = GonzaCloud
package.name = gonzacloud
package.domain = org.gonza
source.dir = .
source.include_exts = py,png,jpg,kv,json
version = 0.1

requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,requests,urllib3,certifi,openssl

orientation = portrait
fullscreen = 0
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

android.api = 31
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1

