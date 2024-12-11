import discord
from discord.ext import commands
import json

class WarnSys(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{__name__} is ready!")

    @commands.command()
    async def warn(self, ctx, member: discord.Member):
        
        with open("cogs/json/warns.json", "r") as f:
            data = json.load(f)
        
        if str(member.id) not in data[str(ctx.guild.id)]:

            await ctx.send("해당 유저는 경고가 없어요...")

        else:
            
            data[str(ctx.guild.id)][str(ctx.member.id)]["Infractions"] -= 1
            
            await ctx.send("경고가 제거되었어요!")
        
        with open("cogs/json/warns.json", "w") as f:
            json.dump(data, f, indent=4)

    @commands.command()
    async def removewarn(self, ctx, member: discord.Member):
        
        with open("cogs/json/warns.json", "r") as f:
            data = json.load(f)
        
        if str(member.id) not in data[str(ctx.guild.id)]:

            data[str(ctx.guild.id)][str(ctx.member.id)] = {}
            data[str(ctx.guild.id)][str(ctx.member.id)]["Infractions"] = 1

            await ctx.send("경고가 추가되었어요!")

        else:
            
            data[str(ctx.guild.id)][str(ctx.member.id)]["Infractions"] += 1
            
            await ctx.send("경고가 추가되었어요!")
        
        with open("cogs/json/warns.json", "w") as f:
            json.dump(data, f, indent=4)

    @commands.command()
    async def findwarns(self, ctx, member: discord.Member):

        with open("cogs/json/warns.json", "r") as f:
            data = json.load(f)

        if str(member.id) not in data[str(ctx.guild.id)]:

            await ctx.send("해당 유저는 경고가 없어요!")

        else:

            data[str(ctx.guild.id)][str(ctx.member.id)]["Infractions"]

            await ctx.send(f"{member.mention}님의 경고횟수는 {data[str(ctx.guild.id)][str(member.id)]["Infractions"]}번 입니다.")

async def setup(client):
    await client.add_cog(WarnSys(client))