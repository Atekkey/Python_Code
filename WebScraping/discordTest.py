token = 'MTAyMTYzMjg3NzUwODY5ODE0Mw.Gb_1U5.rpkUF21lfVYwWhg_z5KPRyw1MSes6PRLvUhTe0'

import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

"""
intents = discord.Intents().all()
bot = commands.Bot(command_prefix='.', intents=intents)
@bot.command(name='.')
async def sendYes(ctx):
    response = "YES"
    await ctx.send(response)
"""
globvar = "var"

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if not message.content.startswith('.'):
        return
    if message.content.startswith('.rep '):
        mess2 = message.content.strip('.rep')
        globvar = mess2
        await message.channel.send(mess2)


client.run(token)
