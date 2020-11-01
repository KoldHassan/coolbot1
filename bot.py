import os
import random
import discord
import asyncio
import keep_alive
from discord.ext import commands
from makedictionaries import make_dictionaries

client = commands.Bot(command_prefix="1")

wisdom = make_dictionaries()

# change status
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    await client.change_presence(activity=discord.Game("1help"))


@client.command()
async def Hello(ctx):
    await ctx.send("Hi")



# all of the wisdoms

@client.command(name='dowlingwisdom', help="Valuable wisdom from momma Dowling herself")
async def deannawisdom(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["Dowling"])
        await ctx.send(response)
        if i < 4:
          i +=1
        elif i == 4:
          i = number

@client.command(name='bmw', help="Find out what Dowling thinks about BMW 💀")
async def bmw(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["bmw"])
        await ctx.send(response)
        if i < 4:
          i +=1
        elif i == 4:
          i = number

@client.command(name='lebron', help="Lebron James, no explanation needed")
async def lebron(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["lebron"])
        await ctx.send(response)
        if i < 4:
          i +=1
        elif i == 4:
          i = number

@client.command(name='ivy', help="Time to find out what Ivy Tran really is 💀")
async def ivy(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["ivy"])
        await ctx.send(response)
        if i < 4:
          i +=1
        elif i == 4:
          i = number

@client.command(name='hassan', help="Time to found out what Hassan really is 💀")
async def hassan(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["hassan"])
        await ctx.send(response)
        if i < 4:
          i +=1
        elif i == 4:
          i = number

@client.command(name='monkey', help="Monkey monkey")
async def monkey(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["monkey"])
        await ctx.send(response)
        if i < 4:
          i +=1
        elif i == 4:
          i = number

@client.command(name='doyoulikeme?', help="Find out if momma Dowling likes you or not... 💀")
async def doyoulikeme(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["doyoulikeme?"])
        await ctx.send(response)
        if i < 4:
          i +=1
        elif i == 4:
          i = number

@client.command(name='millergrove', help="Wisdom straight from milla grove 💀")
async def millergrove(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["millergrove"])
        await ctx.send(response)
        if i < 4:
          i +=1
        elif i == 4:
          i = number
    
@client.command(name='roast', help="Mrs. Dowling will roast the shit out of you 💀")
async def roast(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["roast"])
        await ctx.send(response)
        if i < 4:
          i +=1
        elif i == 4:
          i = number

@client.command(name='bababoey', help="Bababoey")
async def bababoey(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["bababoey"])
        await ctx.send(response)
        if i < 4:
          i +=1
        elif i == 4:
          i = number

keep_alive.keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
