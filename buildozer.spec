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

# 🔥 WICHTIG
android.api = 33
android.minapi = 21
android.sdk_build_tools = 33.0.2

android.archs = arm64-v8a, armeabi-v7a

# stabiler Build
p4a.branch = master
