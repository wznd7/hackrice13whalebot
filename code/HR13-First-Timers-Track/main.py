import discord
from discord.ext import commands
import asyncio

intents = discord.Intents.all()
bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"), intents=intents)

@bot.event
async def on_ready():
	print(f'Bot {bot.user} is online! Id: {bot.user.id}')

async def main():
	await bot.start('MTE1NTE3NzY2Nzg3Njg4NDY2MA.GcwSQx.Onsex8kZCBTjzLEHa2zl0FsWBRplqBW71Gb_M8')

@bot.command()
async def timer(ctx: commands.Context, time: int):
	await asyncio.sleep(time)
	await ctx.send("your time is up!")


asyncio.run(main())