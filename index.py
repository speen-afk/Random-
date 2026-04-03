import os
import discord
from discord.ext import commands

# Load the token from an environment variable
TOKEN = os.getenv("DISCORD_TOKEN")

# Create a bot instance
bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

# Run the bot
bot.run(TOKEN)