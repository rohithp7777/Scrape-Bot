import discord
from discord.ext import commands
from scrapper import advscrape
from scrapper import scrape

client = commands.Bot(command_prefix= '!')

@client.event
async def on_ready():
    await client.change_presence(status= discord.Status.online, activity=discord.Game('Hello there!'))
    print("Bot is ready.")

@client.command()
async def ping(ctx): 
    await ctx.send(f'Pong!{round(client.latency *1000)}ms')

@client.command()
async def clear(ctx, amount =5):
    await ctx.channel.purge(limit = amount)

@client.command()
async def search(ctx, *message):
    query = (" ").join(message)
    print(message)
    URL = "https://www.google.com/search?q=" + query
    item, link = scrape(URL)
    await ctx.send(item.text)
    await ctx.send(link)

@client.command()
async def advsearch(ctx, *message):
    query = (" ").join(message)
    print(message)
    URL = "https://www.google.com/search?q=" + query
    item = advscrape(URL)
    await ctx.send(item.text)  

client.run('TOKEN')
