import pyfiglet
import time
import os
import termcolor
from termcolor import colored
from pyfiglet import Figlet
os.system("clear")
figlet = Figlet(font="slant")
ascii_banner = figlet.renderText("Auto Mac Changer")
lines = ascii_banner.split('\n')
colors = ["red"]
for i, line in enumerate(lines):
    color = colors[i % len(colors)]
    print(colored(line, color))

def style_print(text, red):
    print(colored(text,red, attrs=['bold']))
print()
style_print("                                      [ Made by Cyber Storm ]", 'cyan')

style_print("[+] Welcome to Auto Mac Changer [+]", 'red')
print()
a = (input(colored("[*] How often you want to change your mac address(In seconds)----> ", 'red', attrs=['bold'])))
if '1' in a:
    a = int(a)
    while True:
        os.system("sudo macchanger -r eth0")
        time.sleep(a)
elif '2' in a:
    a = int(a)
    while True:
        os.system("sudo macchanger -r eth0")
        time.sleep(a)
elif '3' in a:
    a = int(a)
    while True:
        os.system("sudo macchanger -r eth0")
        time.sleep(a)
elif '4' in a:
    a = int(a)
    while True:
        os.system("sudo macchanger -r eth0")
        time.sleep(a)
elif '5' in a:
    a = int(a)
    while True:
        os.system("sudo macchanger -r eth0")
        time.sleep(a)
elif '6' in a:
    a = int(a)
    while True:
        os.system("sudo macchanger -r eth0")
        time.sleep(a)
elif '7' in a:
    a = int(a)
    while True:
        os.system("sudo macchanger -r eth0")
        time.sleep(a)
elif '8' in a:
    a = int(a)
    while True:
        os.system("sudo macchanger -r eth0")
        time.sleep(a)
elif '9' in a:
    a = int(a)
    while True:
        os.system("sudo macchanger -r eth0")
        time.sleep(a)
else:
    style_print("[+] Wrong Input [+]", 'red')
    