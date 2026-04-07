[app]
title = ScannerApp
package.name = scannerapp
package.domain = org.pradagov

source.dir = .
source.include_exts = py,kv

version = 0.1

# nur das nötigste
requirements = python3,kivy,requests

orientation = portrait
fullscreen = 0

android.permissions = INTERNET

# WICHTIG: muss zur SDK Version passen
android.api = 33
android.minapi = 21
