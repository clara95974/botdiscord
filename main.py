# coding=utf-8
import discord
import asyncio
from token import TOKEN
ws_url='ws://Guesser-Cluster.scoder12.repl.co'
guess_url='https://guess-it.scoder12.repl.co/guess'
client = discord.Client()
@client.event
async def on_ready():
  print ("hello")
@client.event
async def ​on_message(message):
  print(message.content)
client.run(TOKEN)