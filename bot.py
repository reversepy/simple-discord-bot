import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

# Load token from .env
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

# Intents and bot setup
intents = discord.Intents.default()
bot = commands.Bot(command_prefix='.', intents=intents)

# On ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="Made by Reverse | v.1.0"))

# Basic commands
@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")

@bot.command()
async def hello(ctx):
    await ctx.send(f"Hey {ctx.author.mention}, I'm alive!")

@bot.command()
async def info(ctx):
    await ctx.send("I'm a simple bot for a YouTube tutorial. 💡")

@bot.command()
async def reverse(ctx, *, text: str):
    await ctx.send(text[::-1])

bot.run(TOKEN)
