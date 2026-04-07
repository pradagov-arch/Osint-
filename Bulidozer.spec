[app]
title = ScannerApp
package.name = scannerapp
package.domain = org.pradagov

source.dir = .
source.include_exts = py,kv

version = 0.1

requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

android.api = 33
android.minapi = 21

android.ndk = 25b

p4a.branch = develop

android.accept_sdk_license = True
android.skip_update = True
