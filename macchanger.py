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

def check_and_cast(input_value):
    try:
        # Attempt to convert the input to an integer
        return int(input_value)
    except ValueError:
        # If conversion fails, print "wrong input"
        print()
        style_print("[*] Invalid input", 'red')

# Call the function and print the result
result = check_and_cast(a)
if result is not None:
    a = int(a)
    while True:
        os.system('sudo macchanger -r eth0')
        time.sleep(a)
else:
    time.sleep(3)
    
