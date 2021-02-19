import discord
from discord.ext import commands

client = commands.Bot(command_prefix = ';')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('Under Python Development'))
    print('Bot is ready')
    

@client.command()
async def ping(ctx):
    await ctx.send('pong')

@client.command()
async def verify(ctx, userid):
    await ctx.send(f'{userid} verified')

client.run('TOKEN')
