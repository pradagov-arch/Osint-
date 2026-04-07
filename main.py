from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
import requests
import socket
import random
import threading

USER_AGENTS = [
"Mozilla/5.0",
"Mozilla/5.0 (Android)",
"Mozilla/5.0 (iPhone)"
]

PLATFORMS = {
"GitHub": "https://github.com/{}",
"Reddit": "https://reddit.com/user/{}",
"Twitch": "https://twitch.tv/{}",
"Snapchat": "https://www.snapchat.com/add/{}"
}

KV = """
BoxLayout:
orientation: "vertical"

TextInput:  
    id: user  
    hint_text: "Username"  

TextInput:  
    id: domain  
    hint_text: "Domain"  

Button:  
    text: "Scan"  
    on_press: app.start_scan()  

ScrollView:  
    Label:  
        id: output  
        text: "Results..."  
        size_hint_y: None  
        height: self.texture_size[1]  
        text_size: self.width, None

"""

def headers():
return {"User-Agent": random.choice(USER_AGENTS)}

def scan_user(username):
res = []
for name, url in PLATFORMS.items():
try:
r = requests.get(url.format(username), headers=headers(), timeout=5)
if r.status_code == 200:
res.append(f"[FOUND] {name}")
else:
res.append(f"[MISS] {name}")
except:
res.append(f"[ERROR] {name}")
return res

def domain_ip(domain):
try:
return socket.gethostbyname(domain)
except:
return "Error"

class AppGUI(App):
def build(self):
return Builder.load_string(KV)

def start_scan(self):  
    threading.Thread(target=self.run_scan).start()  

def run_scan(self):  
    user = self.root.ids.user.text  
    domain = self.root.ids.domain.text  

    text = "Scanning...\n\n"  

    results = scan_user(user)  
    for r in results:  
        text += r + "\n"  

    if domain:  
        ip = domain_ip(domain)  
        text += f"\nIP: {ip}"  

    self.root.ids.output.text = text

AppGUI().run()

Ich will es als ApK haben mit vcn aber ohne vcn und Desktop installieren geht das?
