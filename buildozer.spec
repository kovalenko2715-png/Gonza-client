[app]

# (str) Название приложения
title = GonzaCloud

# (str) Имя пакета
package.name = gonzacloud

# (str) Домен пакета
package.domain = org.gonza

# (str) Директория с исходным кодом (где лежит main.py)
source.dir = .

# (list) Расширения файлов, которые нужно включить в сборку
source.include_exts = py,png,jpg,kv,atlas

# (str) ВЕРСИЯ ПРИЛОЖЕНИЯ (ЭТО ИСПРАВЛЯЕТ ТВОЮ ОШИБКУ)
version = 0.1

# (list) Зависимости приложения
# Добавь сюда свои библиотеки через запятую, если они нужны в коде
requirements = python3,kivy,hostpython3,requests,urllib3,certifi

# (int) Android API (33 — актуальный стандарт Google Play)
android.api = 33

# (int) Минимальный поддерживаемый API
android.minapi = 21

# (str) Версия Android NDK (25b — самая стабильная для Kivy сейчас)
android.ndk = 25b

# (bool) Использовать приватное хранилище данных
android.private_storage = True

# (list) Разрешения (Интернет и память)
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (str) Ориентация экрана
orientation = portrait

# (bool) Полноэкранный режим
fullscreen = 0

# (list) Архитектуры для сборки (arm64-v8a — для современных телефонов)
android.archs = arm64-v8a

# (bool) Пропускать обновление SDK (ускоряет сборку)
android.skip_update = False

# (bool) Предупреждать, если запуск от root
warn_on_root = 1

[buildozer]

# (int) Уровень логов (2 = максимально подробный для отладки)
log_level = 2

# (str) Путь к папке сборки
bin_dir = ./bin
