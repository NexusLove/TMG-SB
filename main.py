import discord
import asyncio
import colorama
import os
import sys
import random
import aiohttp
import datetime
import threading
import subprocess
import psutil
import time
from pyfiglet import Figlet
import json
import re
import textwrap
from PIL import Image
from discord.ext import commands
from discord.ext.commands import Bot
from discord.ext.commands import has_permissions, MissingPermissions
from os.path import exists
from _thread import *
from win10toast import ToastNotifier
import multiprocessing
import keyboard
import base64
import utils.clear
from utils.clear import *
from colorama import Fore, Back, Style
try:
    import pyfade
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", 'pyfade'])

toast = ToastNotifier()

configfile = 'config.json'

counter = 0

def inputprefix():
    sys.pycache_prefix = input(pyfade.Fade.Horizontal(
        pyfade.Colors.col, f"Input Prefix: "))

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
    token = input(pyfade.Fade.Horizontal(pyfade.Colors.col, f"Input Token: "))

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
time.sleep(1.0)
clear()

def load():
    bot.load_extension("cogs.maincommands")

def menu():
    global counter
    print(colorama.Fore.RED + f"""
            ████████╗███╗   ███╗ ██████╗               ███╗   ███╗██╗██████╗ ██╗   ██╗██╗████████╗███████╗
            ╚══██╔══╝████╗ ████║██╔════╝               ████╗ ████║██║██╔══██╗██║   ██║██║╚══██╔══╝██╔════╝
               ██║   ██╔████╔██║██║  ███╗    █████╗    ██╔████╔██║██║██║  ██║██║   ██║██║   ██║   █████╗
               ██║   ██║╚██╔╝██║██║   ██║    ╚════╝    ██║╚██╔╝██║██║██║  ██║╚██╗ ██╔╝██║   ██║   ██╔══╝
               ██║   ██║ ╚═╝ ██║╚██████╔╝              ██║ ╚═╝ ██║██║██████╔╝ ╚████╔╝ ██║   ██║   ███████╗
               ╚═╝   ╚═╝     ╚═╝ ╚═════╝               ╚═╝     ╚═╝╚═╝╚═════╝   ╚═══╝  ╚═╝   ╚═╝   ╚══════╝

    {colorama.Fore.RED}                                             Made by {colorama.Fore.YELLOW}WolvTMG#0766
    {colorama.Fore.RED}                                            Logged in as {colorama.Fore.RED}{bot.user} {colorama.Fore.RED}(ID:{colorama.Fore.RED}{colorama.Fore.RED})

                                [1] Start Script | [2] Coming soon  | [3] Join Discord
                                [4] Coming soon  | [5] Coming soon  | [6] Coming soon
                                [7] Coming soon  | [8] Coming soon  | [9] Exit script
        """)


    select = input(f"{Fore.RED}                                                      Choice: ")
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
        clear(); menu()
    elif select == '8':
        clear(); menu()
    elif select == '9':
        sys.exit()
    else:
        print("Invalid option")
        time.sleep(5)
        clear(); menu()

start_new_thread(menu, ())

toast.show_toast(
    "Thanks for using TMG SB",
    f"Booted in " + time.strftime("%S"),
    # icon_path=""
    duration=20,
)

bot.run(token, bot=False)

