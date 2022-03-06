import discord
import pyfiglet
import requests
import io
import aiohttp
import warnings
import colorama
from discord.ext import commands
import random
import sys
from colorama import Fore
from pyfiglet import Figlet
import os
import requests 
from http.client import HTTPException
import base64
import hashlib


#<--------------Commands Start-------------->
class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.message.delete()
        await ctx.send("```ini\n[utils] utilities\n[fun] fun stuff\n[encryption] encrypt stuff\n[activity] choose activity\n[nsfw] self explanitory\n[crypto] check cryptocurrency prices\n\n[TMG - MIDVITE]```", delete_after=8)

    @commands.command()
    async def utils(self, ctx):
        await ctx.message.delete()
        await ctx.send("```ini\n[cl] clears messages\n[ascii] (message)\n[whois] whois command\n\n[TMG - MIDVITE]```", delete_after=8)

    @commands.command()
    async def fun(self, ctx):
        await ctx.message.delete()
        await ctx.send("```ini\n[cock] measures ur cock\n[cf] coin flip\n[ak] emoji\n[awp] emoji\n[lmg] emoji\n\n[TMG - MIDVITE]```", delete_after=8)

    @commands.command()
    async def nsfw(self, ctx):
        await ctx.message.delete()
        await ctx.send("```ini\n[porn] random porn gif\n[blowjob] random blowjob\n[anal] random anal\n[hentai] random hentai\n[boobs] random boob pic\n\n[TMG - MIDVITE]```", delete_after=8)
    
    @commands.command()
    async def encryption(self, ctx):
        await ctx.message.delete()
        await ctx.send("```ini\n[encode_base64] encrypt with base64\n[encode_md5] encrypt with md5\n[encode_sha1] encrypt with sha1\n[encode_sha384] encrpyt with sha384\n[encode_sha224] encrpy with sha224\n[encode_sha512] encrpy with sha512\n[encode_leet] encrpyt with leet\n\n[TMG - MIDVITE]```", delete_after=8)

    @commands.command()
    async def activity(self, ctx):
        await ctx.message.delete()
        await ctx.send("```ini\n[streaming] streaming activity\n[playing] playing activity\n[listening] listen activity\n[watching] watches activity\n[stopactivity] stops activity\n\n[TMG - MIDVITE]```", delete_after=8)
    
    @commands.command()
    async def crypto(self, ctx):
        await ctx.message.delete()
        await ctx.send("```ini\n[btc] bitcoin\n[eth] etherum\n[xmr] xmr\n[xrp] xrp\n[doge] dogecoin\n\n[TMG - MIDVITE]```", delete_after=8)

    @commands.command()
    async def porn(self, ctx):
        await ctx.message.delete()
        choose = ["https://media.discordapp.net/attachments/909329669151670272/917541503491002398/D678DD10-7E5A-4559-9F31-986E094453CA.gif",
                "https://media.discordapp.net/attachments/822314610798755860/822325955950936075/LOL100ROBUX.gif", 
                "https://tenor.com/view/chad-cock-order-bbc-muscular-guy-gif-23529914", "https://giphy.com/gifs/EooFElWfrBWMO05mIi"]
        image = random.choice(choose)
        await ctx.send(image, delete_after=8)

    @commands.command()
    async def ascii(self, ctx, *,text: str=None):
        await ctx.message.delete()
        if text is None:
            await ctx.send("```init\nInvalid argument\n\n[TMG - MIDVITE]", delete_after=20)
        else:
            f = Figlet(font='Slant')
            j = (f.renderText(text))
            try:
                await ctx.send(f"```{j}```", delete_after=20)
            except discord.HTTPException:
                try:
                    await ctx.send(f"```{j}```", delete_after=20)
                except Exception as e:
                    await ctx.send(f"Error: {e}", delete_after=20)

    @commands.command()
    async def online(self, ctx):
        await ctx.message.delete()
        await ctx.send("```ini\nTMG is online\n\n[TMG - MIDVITE]```", delete_after=8)

    @commands.command()
    async def offline(self, ctx):
        await ctx.message.delete()
        await ctx.send("```ini\nTMG is now offline\n\n[TMG - MIDVITE]```", delete_after=8)
        sys.exit()

    @commands.command(name="id")
    async def id_(ctx, user: discord.User):
        await ctx.message.delete()
        await ctx.send(user.id)

    @commands.command()
    async def cf(self, ctx):
        await ctx.message.delete()
        choose = ["Heads", "Tails"]
        cf = random.choice(choose)

        await ctx.send("```ini\n"+ cf +"\n\n[TMG - MIDVITE]```", delete_after=8)

    @commands.command()
    async def cock(self, ctx):
        await ctx.message.delete()
        choose = ["8=D 1%", "8==D 2 millimeter defeater", "8===D 5%", "8====D 7%", "8=====D 10%", "8======D 13%", "8=======D 17%", "8========D 22%", "8=========D 38%", "8==========D 44%", "8===========D 90%", "8============D 100% BIG BLACK COCK"]
        cock = random.choice(choose)

        await ctx.send("```ini\n"+ cock +" \n\n[TMG - MIDVITE]```", delete_after=8)

    @commands.command(aliases=["clear"])
    async def cl(self, ctx, amount: int):
        await ctx.message.delete()
        async for message in ctx.message.channel.history(limit=amount).filter(lambda m: m.author == self.bot.user).map(lambda m: m):
            try:
                await message.delete()
            except:
                pass   

    @commands.command()
    async def blowjob(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        api = requests.get("https://nekos.life/api/v2/img/blowjob")
        json = api.json()
        async with aiohttp.ClientSession() as session:
            async with session.get(json['url']) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.send(file=discord.File(data, 'img.png'))
                    await ctx.send(user.mention + " This could be you and me")
                except HTTPException:
                    print(f"{Fore.RED}{Fore.YELLOW}This user has disabled NSFW content in their dms")

    @commands.command()
    async def boobs(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        api = requests.get("https://nekos.life/api/v2/img/boobs")
        json = api.json()
        async with aiohttp.ClientSession() as session:
            async with session.get(json['url']) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.send(file=discord.File(data, 'img.png'))
                    await ctx.send(user.mention + " This could be you and me")
                except HTTPException:
                    print(f"{Fore.RED}{Fore.YELLOW}This user has disabled NSFW content in their dms")
    
    @commands.command()
    async def anal(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        api = requests.get("https://nekos.life/api/v2/img/anal")
        json = api.json()
        async with aiohttp.ClientSession() as session:
            async with session.get(json['url']) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.send(file=discord.File(data, 'img.png'))
                    await ctx.send(user.mention + " This could be you and me")
                except HTTPException:
                    print(f"{Fore.RED}{Fore.YELLOW}This user has disabled NSFW content in their dms")
    
    @commands.command()
    async def hentai(self, ctx, user: discord.User = None):
        await ctx.message.delete()
        api = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
        json = api.json()
        async with aiohttp.ClientSession() as session:
            async with session.get(json['url']) as resp:
                if resp.status != 200:
                    return await ctx.send('Could not download file...')
                data = io.BytesIO(await resp.read())
                try:
                    await ctx.send(file=discord.File(data, 'img.png'))
                    await ctx.send(user.mention + " This could be you and me")
                except HTTPException:
                    print(f"{Fore.RED}{Fore.YELLOW}This user has disabled NSFW content in their dms")

    @commands.command()
    async def ak(self, ctx):
        await ctx.message.delete()
        ak = '︻╦╤─'
        await ctx.send(ak, delete_after=8)

    @commands.command()
    async def awp(self, ctx):
        await ctx.message.delete()
        awp = '︻デ═一'
        await ctx.send(awp, delete_after=8)

    @commands.command()
    async def lmg(self, ctx):
        await ctx.message.delete()
        lmg = '︻╦̵̵͇╤──'
        await ctx.send(lmg, delete_after=8)

    @commands.command()
    async def btc(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=BTC&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        await ctx.send(f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`', delete_after=8)

    @commands.command()
    async def xmr(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=XMR&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        await ctx.send(f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`', delete_after=8)

    @commands.command()
    async def xrp(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=XRP&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        await ctx.send(f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`', delete_after=8)

    @commands.command()
    async def doge(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=DOGE&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        await ctx.send(f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`', delete_after=8)

    @commands.command()
    async def eth(self, ctx):
        await ctx.message.delete()
        r = requests.get("https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=USD,EUR")
        kekistan = r.json()
        eur = kekistan['EUR']
        usd = kekistan['USD']
        await ctx.send(f'EUR: `{str(eur)}€`\nUSD: `{str(usd)}$`', delete_after=8)

    @commands.command()
    async def streaming(self, ctx, *, message):
        await ctx.message.delete()
        stream = discord.Streaming(
            name = message,
            url = "https://www.twitch.tv/tmgwolv", 
        )
        await self.bot.change_presence(activity=stream)    
        
    @commands.command()
    async def playing(self, ctx, *, message):
        await ctx.message.delete()
        game = discord.Game(
            name=message
        )
        await self.bot.change_presence(activity=game)
    
    @commands.command()
    async def listening(self, ctx, *, message):
        await ctx.message.delete()
        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening, 
                name=message, 
            ))
              
    @commands.command()
    async def watching(self, ctx, *, message):
        await ctx.message.delete()
        await self.bot.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, 
                name=message
            ))

    @commands.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
    async def stopactivity(self, ctx):
        await ctx.message.delete()
        await self.bot.change_presence(activity=None, status=discord.Status.dnd)

    @commands.command()
    async def whois(self, ctx, *, user: discord.User = None): 
        await ctx.message.delete()
        if user is None:
            user = ctx.author      
        date_format = "%a, %d %b %Y %I:%M %p"
        return await ctx.send("Registered: " + user.created_at.strftime(date_format))

    @commands.command()
    async def encode_base64(self, ctx, *, args):
        await ctx.message.delete()
        msg = base64.b64encode('{}'.format(args).encode('ascii'))
        enc = str(msg)
        enc = enc[2:len(enc)-1]
        await ctx.send(enc)  

    @commands.command()
    async def encode_md5(self, ctx, *, args):
        await ctx.message.delete()
        msg = hashlib.md5(args.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)

    @commands.command()
    async def encode_sha1(self, ctx, *, args):
        await ctx.message.delete()
        msg = hashlib.sha1(args.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)

    @commands.command()
    async def encode_sha384(self, ctx, *, args):
        await ctx.message.delete()
        msg = hashlib.sha3_384(args.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)

    @commands.command()
    async def encode_sha224(self, ctx, *, args):
        await ctx.message.delete()
        msg = hashlib.sha3_224(args.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)

    @commands.command()
    async def encode_sha512(self, ctx, *, args):
        await ctx.message.delete()
        msg = hashlib.sha3_512(args.encode())
        crnja =  msg.hexdigest()
        await ctx.send(crnja)

    @commands.command()
    async def encode_leet(self, ctx, *, args):
        await ctx.message.delete()
        encoded = args.replace('e', '3').replace('a', '4').replace('i', '!').replace('u', '|_|').replace('U', '|_|').replace('E', '3').replace('I', '!').replace('A', '4').replace('o','0').replace('O','0').replace('t','7').replace('T','7').replace('l','1').replace('L','1').replace('k','|<').replace('K','|<').replace('CK','X').replace('ck','x').replace('Ck','X').replace('cK','x')
        await ctx.send(f'`{encoded}`')
#<--------------Commands End-------------->


def setup(bot):
    bot.add_cog(Commands(bot))
    
    