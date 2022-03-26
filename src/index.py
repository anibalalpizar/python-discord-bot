
"""
Copyright (c) 2022 Anibal-Alpizar.
https://github.com/Anibal-Alpizar
"""

import discord
from discord.ext import commands
import datetime
from urllib import parse, request
import re
from discord_together import DiscordTogether
import asyncio



bot = commands.Bot(command_prefix='>', description="here the description of the bot")


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)
# you can add more operations following the same pattern 



@bot.command()
async def info(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}", description="Descripcion", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    embed.add_field(name="Server Region", value=f"{ctx.guild.region}")
    embed.add_field(name="Server ID", value=f"{ctx.guild.id}")
    # embed.set_thumbnail(url=f"{ctx.guild.icon}")
    embed.set_thumbnail(url="")
    await ctx.send(embed=embed)

@bot.command()
async def yt(ctx, *, search):
    query_string = parse.urlencode({'search_query': search})
    html_content = request.urlopen('http://www.youtube.com/results?' + query_string)
    # print(html_content.read().decode())
    search_results=re.findall('watch\?v=(.{11})',html_content.read().decode('utf-8'))
    print(search_results)
    # I will put just the first result, you can loop the response to show more results
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Streaming(name="https://github.com/Anibal-Alpizar", url="https://github.com/Anibal-Alpizar"))
    print('Bot is ready!')


@bot.event
async def on_ready():
    print(f"Bot logged into {bot.user}.")
    bot.togetherControl = await DiscordTogether("token bot")


@bot.command()
async def start(ctx):
    # Here we consider that the user is already in a VC accessible to the bot.
    link = await bot.togetherControl.create_link(ctx.author.voice.channel.id, 'youtube') ##youtube = channel voice
    await ctx.send(f"Click on blue link!\n{link}")





bot.run('token bot')