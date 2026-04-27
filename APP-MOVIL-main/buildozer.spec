[app]
title = Emaus App
package.name = emaus_prayer
package.domain = com.eryck.emaus
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,js,css,json
version = 1.0.0

# Requerimientos para Flask
requirements = python3,flask,werkzeug,jinja2,itsdangerous,click,openssl,shishua

orientation = portrait
fullscreen = 0
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = False

# Evita que la pantalla se apague mientras se reza (opcional pero recomendado)
android.wakelock = True

# Nombre del archivo APK de salida
android.release_artifact = apk
android.skip_update_check = True
android.presplash_color = #E6D9C7

# Permisos básicos
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1