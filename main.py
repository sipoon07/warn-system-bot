import discord
from discord.ext import commands
import os
import asyncio
import json

TOKEN = "여긴 비어 있어요!!"

client = commands.bot(command_prefix="?", intents=discord.Intents.all())

@client.event
async def on_ready():
    print(f"Hello Everyone! Successfully logged is as Client {client.user.id}")

@client.event
async def on_guild_join(guild):
    with open("cogs/json/warns.json", "r") as f:
        data = json.load(f)

    data[str(guild.id)] = {}

    for member in guild.members:
        data[str(guild.id)][str(member.id)] = {}
        data[str(guild.id)][str(member.id)]["Infractions"] = 0

    with open("cogs/json/warns.json" "w") as f:
        json.dump(data, f, indent=4)

@client.event
async def on_guild_remove(guild):
    with open("cogs/json/warns.json", "r") as f:
        data = json.load(f)
    
    data.pop(str(guild.id))

    with open("cogs/json/warns.json", "w") as f:
        json.dump(data, f, indent=4)

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswitch(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load()
        await client.start(TOKEN)

asyncio.run(main())