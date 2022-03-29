import os
import logging
import discord
from discord.ext import commands, tasks
import json
import requests
import time
from bot_token import token


# Discord ID info
activity = discord.Activity(type=discord.ActivityType.watching, name="your words.")
author_id = "892999941146963969"

# Logger
logger = logging.getLogger("discord")
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
handler.setFormatter(
    logging.Formatter("%(asctime)s:%(levelname)s:%(name)s: %(message)s")
)
logger.addHandler(handler)


# Bot info
bot = commands.Bot(
    command_prefix="bb!",  # Change to desired prefix
    case_insensitive=True, # Commands aren't case-sensitive
    activity=activity,
    status=discord.Status.idle
)


# Author ID
bot.author_id = author_id  # Change to your discord id!!!

def reverse_text(x):
  return f'{x}'[::-1]

def upsidedown_text(word):
  f = open("upsidedown.json", "r")
  _dict = json.loads(f.read())
  _list = []

  for x in word:
    try:
      z = _dict[x]
    except:
      _list.append(x)
    else:
      _list.append(z)

  f.close()
  return ''.join(_list)

# Bot Ready
@bot.event
async def on_ready():  # When the bot is ready
    print(f"{bot.user} Started.")



'''
#Message respond event
@bot.event
async def on_message(message):
    if (message.author.bot):
        return
    if isinstance(message.channel, discord.channel.DMChannel):
        return
    r = upsidedown_text(message.content)
    r = reverse_text(r)
    await message.reply(r, mention_author=False)
'''


#Reverse
@bot.command(name="reverse", help="Reverses the input text!")
async def reverse(ctx, *, arg):
    r = reverse_text(arg)
    await ctx.reply(r, mention_author=False)

@reverse.error
async def reverse_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Error: Something went wrong.")


#Upsidedown
@bot.command(name="upsidedown", help="Makes the input text upsidedown!")
async def upsidedown(ctx, *, arg):
    r = upsidedown_text(arg)
    await ctx.reply(r, mention_author=False)

@upsidedown.error
async def upsidedown_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Error: Something went wrong.")

#Upsidedown + Backwards
@bot.command(name="full", help="Makes the input text upsidedown and backwards!")
async def full(ctx, *, arg):
    r = upsidedown_text(arg)
    r = reverse_text(r)
    await ctx.reply(r, mention_author=False)

@full.error
async def full_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send("Error: Something went wrong.")

@bot.command(name="emoji", help="")
async def emoji(ctx, *, arg):
    print(arg)
    await ctx.reply(arg, mention_author=False)



# boiler plate
if __name__ == "__main__":
    bot.run(token)