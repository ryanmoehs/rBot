# commands list with prefix "!"
import discord
from discord.ext import commands

class Shout(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("!embed is ready")

    @commands.command()
    async def cmd(self, ctx):
        cmd_message = discord.Embed(title=f"Commands List (prefix !)", description="There are some commands you can use", color=discord.Color.random())
        cmd_message.add_field(name="!cmd", value="Show commands list", inline=False)
        cmd_message.add_field(name="!ping", value="Show bot's latency in ms", inline=False)
        cmd_message.add_field(name="!pingme", value="Show bot's latency in ms and send to dm", inline=False)
        cmd_message.add_field(name="!salam", value="Answer salam", inline=False)
        cmd_message.add_field(name="Note :", value="You can use slash command (prefix /) for easier use",inline=False)
        cmd_message.set_footer(text="by rBot")

        await ctx.send(embed=cmd_message)

    @commands.command()
    async def ingfo(self, ctx):
        ingfo_message = discord.Embed(title=f"{ctx.author.mention}", description="Deskripsi", color=discord.Color.random())
        ingfo_message.set_author(name=f"Requested by {ctx.author.mention}", icon_url=ctx.author.avatar)
        ingfo_message.set_thumbnail(url=ctx.author.avatar)
        ingfo_message.set_image(url=ctx.author.avatar)
        ingfo_message.add_field(name="Field name", value="Field value", inline=False)
        ingfo_message.set_footer(text="byb rBot")

        await ctx.send(embed=ingfo_message)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send("Halo")

    @commands.command()
    async def pingme(self, ctx):
        await ctx.author.send("Halo")

    @commands.command()
    async def salam(self, ctx):
        await ctx.send(f"Waalaikumussalam {ctx.author.mention}")

async def setup(client):
    await client.add_cog(Shout(client))