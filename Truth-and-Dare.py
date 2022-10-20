from keep_alive import keep_alive
import discord
from discord.ext import commands,tasks
from itertools import cycle
import random
from dotenv import load_dotenv
import os
from choices import truths,dares
load_dotenv()

intents = discord.Intents(messages = True , guilds = True ,  reactions = True , members = True , presences = True)
client  = commands.Bot(command_prefix = '.', intents = intents)


@client.event 
async def on_ready():
  change_status.start()
  print("I am turned on!!")

status = cycle(['With Friends','With Parents','With Love','With Yourself'])


@tasks.loop(seconds=5)
async def change_status():
  await client.change_presence(activity=discord.Game(f'{next(status)} | .help'))  

  
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandNotFound):
    await ctx.send('Invalid Command Used. Type .help to know the commands')
                       
  if isinstance(error, commands.MissingRequiredArgument):
    await ctx.send('Give proper values to the command an argument is missing')
  
  
@client.command()
async def clean(ctx, num = 1):
  await ctx.channel.purge(limit = num+1)  


@client.command(aliases = ['t'])

async def truth(ctx):

  await ctx.send(random.choice(truths))


@client.command(aliases = ['d'])

async def dare(ctx):
  
  await ctx.send(random.choice(dares))



keep_alive()
client.run(os.getenv('TOKEN'))
