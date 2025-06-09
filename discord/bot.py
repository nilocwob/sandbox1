# Requires 'messages' privileged intent to function

import discord
from discord.ext import commands
import random
import os
from dotenv import load_dotenv

load_dotenv()
token = os.getenv("TOKEN")

intents = discord.Intents(messages=True)
intents.message_content = True
bot = commands.Bot(command_prefix='!',intents=intents)

async def on_ready():
	print(f'Logged as {bot.user}!')

async def on_message(bot, message):
	if message.author == bot.user:
		return
	
@bot.command()
async def d20(ctx):
	die = random.randint(0,20)
	msg = f"You just rolled a {str(die)}"
	await ctx.send(msg)
	
bot.run(token)