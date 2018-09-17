            
import discord
from discord.ext import commands
import asyncio
import random 

bot = commands.Bot(command_prefix= "~")

@bot.event
async def on_ready():
         print("Verification for me")
         print (bot.user.id)

@bot.command(pass_context=True)
async def commands(cxt):
    await bot.say("~Commands, ~Mood, ~sigh, ~OwO,")

@bot.command(pass_context=True)
async def Mood(cxt):
    await bot.say("Thats a Mood")

@bot.command(pass_context=True)
async def sigh(cxt):
    await bot.say(":sigh:")

@bot.command(pass_context=True)
async def OwO(cxt):
    await bot.say(":OwO:")





