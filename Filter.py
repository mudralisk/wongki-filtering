#-*- coding: utf-8 -*-
import discord
import random
import os
from random import randint
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
channel = client.get_channel("channel id")

filter_test = ["tlqkf","whssk"]

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Game('이쁜말 쓰는중'))
    print('Bot is ready.')


@client.event
async def on_message(message):
	if '시발' in message.content:
		newmsg = message.content[:]
		await message.delete()
		newmsg = newmsg.replace("시발","이런")
		username = message.author.name
		outputmsg = username +": "+ newmsg
		await message.channel.send(outputmsg)


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

