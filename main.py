import discord
import colorama
import os
import sys
import threading
import subprocess
import time
from pyfiglet import Figlet
import json
from PIL import Image
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions, MissingPermissions
from os.path import exists
from _thread import *
from win10toast import ToastNotifier
from colorama import Fore, Back, Style
from utils.clear import *
from utils.colors import *


threads = []

toast = ToastNotifier()

configfile = 'config.json'

counter = 0
themecounter = 1
theme = theme_original

def inputprefix():
    input("Input Prefix: ")

    data = {
        "prefix": prefix
    }

    with open(configfile, 'w') as file_object:
        json.dump(data, file_object)

    return data

if not exists(configfile):
    data = inputprefix()
else:
    with open('config.json', 'r') as f:
        data = json.load(f)

prefix = data["prefix"]

def inputtoken():
    token = input(f"Input Token: ")

    data = {
        "token": token
    }

    with open(configfile, 'w') as file_object:
        json.dump(data, file_object)

    return data

if not exists(configfile):
    data = inputtoken()
else:
    with open('config.json', 'r') as f:
        data = json.load(f)

token = data["token"]


bot = commands.Bot(command_prefix=prefix, self_bot=True, help_command=None)


intents = discord.Intents().default()
intents.members = True
client = discord.Client(intents=intents)


print(f"Booting TMG SB")
time.sleep(1.0)
print(f"{Fore.RED}Made by WolvTMG")


toast.show_toast(
    "Thanks for using TMG SB",
    f"Booted in " + time.strftime("%S"),
    # icon_path=""
    duration=2,
)

clear()

def load():
    bot.load_extension("cogs.maincommands")

def themes():
    global themecounter
    print(F"""
                              ████████╗██╗  ██╗███████╗███╗   ███╗███████╗███████╗
                              ╚══██╔══╝██║  ██║██╔════╝████╗ ████║██╔════╝██╔════╝
                                 ██║   ███████║█████╗  ██╔████╔██║█████╗  ███████╗
                                 ██║   ██╔══██║██╔══╝  ██║╚██╔╝██║██╔══╝  ╚════██║
                                 ██║   ██║  ██║███████╗██║ ╚═╝ ██║███████╗███████║
                                 ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝     ╚═╝╚══════╝╚══════╝

                                [1] Original     | [2] Blue         | [3] Yellow
                                [4] White        | [5] Black        | [6] Exit



       """)

    select = input(
        f"                                                      Choice: ") 
    if select == '1':
        themecounter = 1
        clear()
        menu()
    elif select == '2':
        themecounter = 2
        clear()
        menu()
    elif select == '3':
        themecounter = 3
        clear()
        menu()
    elif select == '4':
        themecounter = 4
        clear()
        menu()
    elif select == '5':
        themecounter = 5
        clear()
        menu()
    elif select == '6':
        themecounter = 6
        clear()
        menu()
    else:
        clear()
        themes()



def menu():
    global counter
    global themecounter
    global theme

    if themecounter == 1:
        theme = theme_original
    elif themecounter == 2:
        theme = theme_blue
    elif themecounter == 3:
        theme = theme_yellow
    elif themecounter == 4:
        theme = theme_white
    elif themecounter == 5:
        theme = theme_black

    print(theme + f"""
            ████████╗███╗   ███╗ ██████╗               ███╗   ███╗██╗██████╗ ██╗   ██╗██╗████████╗███████╗
            ╚══██╔══╝████╗ ████║██╔════╝               ████╗ ████║██║██╔══██╗██║   ██║██║╚══██╔══╝██╔════╝
               ██║   ██╔████╔██║██║  ███╗    █████╗    ██╔████╔██║██║██║  ██║██║   ██║██║   ██║   █████╗
               ██║   ██║╚██╔╝██║██║   ██║    ╚════╝    ██║╚██╔╝██║██║██║  ██║╚██╗ ██╔╝██║   ██║   ██╔══╝
               ██║   ██║ ╚═╝ ██║╚██████╔╝              ██║ ╚═╝ ██║██║██████╔╝ ╚████╔╝ ██║   ██║   ███████╗
               ╚═╝   ╚═╝     ╚═╝ ╚═════╝               ╚═╝     ╚═╝╚═╝╚═════╝   ╚═══╝  ╚═╝   ╚═╝   ╚══════╝

                                                 Made by {colorama.Fore.RESET}WolvTMG#0766 """ +
    theme + f"""                                                                                         Logged in as {bot.user} (ID: Coming Soon)

                                [1] Start Script | [2] Update       | [3] Join Discord
                                [4] Spammer      | [5] Nuker        | [6] Clear
                                [7] Themes       | [8] Update Log   | [9] Exit script
        """)


    select = input(theme + "                                                      Choice: ")
    if select == '1' and counter == 0:
        counter = counter + 1
        load()
        print("Script has been started")
        time.sleep(2)
        clear(); menu()
    elif select == '1' and counter >= 1:
        print("Script has already been started")
        time.sleep(2)
        clear(); menu()
    elif select == '2':
        e = input("[Update] No updates yet\n\n[Enter] to exit updates")
        clear(); menu()
    elif select == '3':
        print(".gg/uYCeDP3")
        time.sleep(5)
        clear(); menu()
    elif select == '4':
        clear(); menu()
    elif select == '5':
        clear(); menu()
    elif select == '6':
        clear(); menu()
    elif select == '7':
        clear()
        themes()
    elif select == '8':
        e = input("\n[Update] Changelog 4/4/2022, nothing yet\n\n[Enter] to exit changelog")
        clear(); menu()
    elif select == '9':
        sys.exit()
    else:
        print("Invalid option")
        time.sleep(5)
        clear(); menu()

process = threading.Thread(target=menu)
process.start()

bot.run(token, bot=False)

