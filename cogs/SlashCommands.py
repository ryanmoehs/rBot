import discord
import random
from discord.ext import commands
from discord import app_commands

# commands list for prefix "/"
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
            for rand in random_qotd:
                for q in qotd:
                    if q in rand:
                        await interaction.response.send_message(rand)
                        

class Cmd(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("!cmd is ready")
    @app_commands.command(name="command", description="Show commands list")
    # @commands.command()
    async def command(self, interaction: discord.Interaction):
        cmd_msg = discord.Embed(title="Commands List (prefix /)", description="There are some commands you can use", color=discord.Color.random())
        cmd_msg.add_field(name="/cmd", value="Show commands list", inline=False)
        cmd_msg.add_field(name="/ping", value="Show bot's latency in ms", inline=False)
        cmd_msg.add_field(name="/pingme", value="Show bot's latency in ms and send to dm", inline=False)
        cmd_msg.add_field(name="/salam", value="Answer salam", inline=False)
        cmd_msg.add_field(name="Note :", value="You can use shout command (prefix !) for oldschool mode",inline=False)
        cmd_msg.set_footer(text="by rBot")

        await interaction.channel.send(embed=cmd_msg)

class Ingfo(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("!ingfo is ready")

    @app_commands.command(name="ingfo", description="Showing user profile")
    async def ingfo(self, interaction: discord.Interaction, member: discord.Member):
        name = member.display_name
        pfp = member.display_avatar

        ingfo_embed = discord.Embed(title=f"Who is {name}?", description=f"Name : {name}", color=discord.Color.random())
        ingfo_embed.set_image(url=pfp)
        ingfo_embed.add_field(name="Personal Information", value=f"Name : {name}", inline=True)
        ingfo_embed.set_footer(text="rBot")

        await interaction.channel.send(embed=ingfo_embed)


async def setup(client):
    await client.add_cog(Ping(client))
    await client.add_cog(Salam(client))
    await client.add_cog(Qotd(client))
    await client.add_cog(Ingfo(client))
    await client.add_cog(Cmd(client))