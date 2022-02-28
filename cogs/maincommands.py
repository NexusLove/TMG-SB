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


#<--------------Commands Start-------------->
class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx):
        await ctx.message.delete()
        await ctx.send("```ini\n[utils] utilities\n[fun] fun stuff\n[nsfw] self explanitory\n\n[TMG - MIDVITE]```", delete_after=8)

    @commands.command()
    async def utils(self, ctx):
        await ctx.message.delete()
        await ctx.send("```ini\n[cl] clears messages\n[ascii] (message)\n\n[TMG - MIDVITE]```", delete_after=8)

    @commands.command()
    async def fun(self, ctx):
        await ctx.message.delete()
        await ctx.send("```ini\n[cock] measures ur cock\n[cf] coin flip\n\n[TMG - MIDVITE]```", delete_after=8)

    @commands.command()
    async def nsfw(self, ctx):
        await ctx.message.delete()
        await ctx.send("```ini\n[porn] random porn gif\n[blowjob] random blowjob\n[anal] random anal\n[hentai] random hentai\n[boobs] random boob pic\n\n[TMG - MIDVITE]```", delete_after=8)

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
#<--------------Commands End-------------->


def setup(bot):
    bot.add_cog(Commands(bot))
    
    