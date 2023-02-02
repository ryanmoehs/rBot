import discord
import random
from discord.ext import commands
from discord import app_commands


class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.Cog.listener()
    async def on_ready(self):
        print("!ping is ready!")


    @app_commands.command(name="ping", description="Show bot's latency in ms.")
    async def ping(self, interaction: discord.Interaction):
        bot_latency = round(self.client.latency * 1000)
        if bot_latency <= 500:
            await interaction.response.send_message(f"Duar! Aku respon kamu dalam waktu {bot_latency} ms. Cepet kan?") 
        else:
            await interaction.response.send_message(f"Duh maap slow respon. Aku ngerespon kamu {bot_latency} ms kelamaan ga?") 

            

    @app_commands.command(name="pingme", description="Show bot's latency in ms and send into dm.")
    async def pingme(self, interaction: discord.Interaction):
        bot_latency = round(self.client.latency * 1000)
        await interaction.response.send_message(f"Pong! I need {bot_latency} ms to responding you")

class Salam(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("!salam is ready!")
    
    @app_commands.command(name="salam", description="Jawab salam.")
    async def salam(self, interaction: discord.Interaction, user: discord.User):
        await interaction.response.send_message(f"Waalaikumussalam {user.mention}")

class Qotd(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("!qotd is ready!")
    
    @app_commands.command(name="qotd", description="Quotes random.")
    async def qotd(self, interaction: discord.Interaction):
        with open("assets/qotd.txt", "r") as f:
            random_qotd = f.readlines()
            qotd = random.choices(random_qotd)
        await interaction.response.send_message(qotd)

class Help(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("!help is ready")

    @app_commands.command(name="help", description="Showing commands list")
    # @commands.command()
    async def help(self, interaction: discord.Interaction, user: discord.User):
    # async def help(self, ctx):
        help_embed = discord.Embed(title="Commands list", description="Here the commands", color=discord.Color.blue)
        help_embed.set_author(name=f"Requested by {user.mention}")
        # help_embed.set_thumbnail(url=interaction.user.default_avatar)
        # help_embed.set_image(url=interaction.user.default_avatar)
        help_embed.add_field(name="Commands lists", value="Field value", inline=False)
        # help_embed.set_footer(name="This is footer", icon_url=interaction.user.default_avatar)

        await interaction.response.send_message(embed=help_embed)

async def setup(client):
    await client.add_cog(Ping(client))
    await client.add_cog(Salam(client))
    await client.add_cog(Qotd(client))
    await client.add_cog(Help(client))