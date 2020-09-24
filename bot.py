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
        i += 1

@client.command(name='bmw', help="Randomly generated response to the command bmw")
async def bmw(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["bmw"])
        await ctx.send(response)
        i += 1

@client.command(name='lebron', help="Randomly generated response to the command lebron")
async def lebron(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["lebron"])
        await ctx.send(response)
        i += 1

@client.command(name='ivy', help="Randomly generated response to describe what Ivy Tran is")
async def ivy(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["ivy"])
        await ctx.send(response)
        i += 1

@client.command(name='hassan', help="Randomly generated response to describe what Hassan Wajid is")
async def hassan(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["hassan"])
        await ctx.send(response)
        i += 1

@client.command(name='monkey', help="Randomly generated response to the command monkey")
async def monkey(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["monkey"])
        await ctx.send(response)
        i += 1

@client.command(name='doyoulikeme?', help="Find out if momma Dowling likes you or not...")
async def doyoulikeme(ctx, number: int = 1):
    i = 0
    while i < number:
        response = random.choice(wisdom["doyoulikeme?"])
        await ctx.send(response)
        i += 1


keep_alive.keep_alive()
token = os.environ.get("DISCORD_BOT_SECRET")
client.run(token)
