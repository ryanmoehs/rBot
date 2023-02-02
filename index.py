import discord
import random
import os
import asyncio
from dotenv import load_dotenv
from discord.ext import commands

# load macem2 "rahasia"
load_dotenv()
token = os.getenv('TOKEN')

client = commands.Bot(command_prefix="!", intents=discord.Intents.all())
# pesan yg muncul ketika run bot
@client.event
async def on_ready():
    await client.tree.sync()
    print("Success: bot-py is connected to Discord")

async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")
            print(f"{filename[:-3]} is loaded")

async def main():
    async with client:
        await load()
        await client.start(token)

asyncio.run(main())

# command pake !
# ping user di server
# @client.command()
# async def ping(ctx):
#     bot_latency = round(client.latency * 1000)
#     await ctx.send(f"Pong! I need {bot_latency} ms to responding you")

# # nyapa user di server
# @client.command()
# async def salam(ctx):
#     await ctx.send(f"Waalaikumussalam {discord.Member.mention}!")

# # nyapa ping lewat dm
# @client.command()
# async def pingme(ctx):
#     await ctx.author.send("Pong!")

# # qotd
# @client.command()
# async def qotd(ctx):
#     with open("qotd.txt", "r") as f:
#         random_qotd = f.readlines()
#         qotd = random.choice(random_qotd)
    
#     await ctx.send(qotd)

# client.run(token)