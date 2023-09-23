import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = commands.when_mentioned_or('!'), intents = intents)

@bot.event
async def on_ready():
	print(f'Logged in as {bot.user} (ID: {bot.user.id})')
	print('------')

async def main():
	try:
		await bot.load_extension("cogs.rps")
		await bot.load_extension("cogs.util")
		print(f'Extension loaded!')
	except Exception as e:
		print(f'Failed to load extension cogs.')
		print(str(e))
	await bot.start('MTE1NTE3NzY2Nzg3Njg4NDY2MA.GcwSQx.Onsex8kZCBTjzLEHa2zl0FsWBRplqBW71Gb_M8')

asyncio.run(main())

