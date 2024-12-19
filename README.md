# Auto-Mac-Changer
It's a tool to change your mac address how often you want, this is useful when you enter dark web or any security purposes.

# Installtion (tested on kali linux)
* At first install manual Mac Changer 
```bash
sudo apt install macchanger
```
* Clone the repository
```bash
git clone https://github.com/Cyber-Storm7/Auto-Mac-Changer.git
```
* Navigate the directory
```bash
cd Auto-Mac-Changer
```
* Install required modules for the script
```bash
pip install -r requirements.txt
```
* Run the script
```bash
python3 macchanger.py
```
* To stop the script press Ctrl + C , and now if you want to change your to the permanent on run :
```bash
sudo macchanger -p eth0
```
# Note 
Every time your mac address changes you will be disconnected from the internet and reconnect to the internet. 
# My YouTube Channel
http://www.youtube.com/@CyberStorm-5221
