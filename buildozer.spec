[app]
title = ScannerApp
package.name = scannerapp
package.domain = org.pradagov

source.dir = .
source.include_exts = py,kv

requirements = python3,kivy,requests,urllib3,chardet,idna,certifi

orientation = portrait
fullscreen = 0

android.permissions = INTERNET
android.api = 31
android.minapi = 21
