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

android.api = 31
android.minapi = 21

android.archs = arm64-v8a, armeabi-v7a

# stabiler Build
p4a.branch = master
