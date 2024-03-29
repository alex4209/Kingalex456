import os,platform
os.system('git pull')
os.system("clear")
print('\033[92;1m Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/Hf6WUhpV822AmZlGM6RA8P')
bhatti=platform.architecture()[0]
if bhatti=="32bit":
    __import__("p32")
elif bhatti=="64bit":
    __import__("p64")
