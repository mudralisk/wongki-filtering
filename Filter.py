#-*- coding: utf-8 -*-
import discord
import random
import os
from random import randint
from discord.ext import commands

client = commands.Bot(command_prefix = '.')
channel = client.get_channel("channel id")

filter_test = ["시발,존나,새기,새끼"]

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
		newmsg = newmsg.replace("새기","아이")
		newmsg = newmsg.replace("새끼","아이")
		newmsg = newmsg.replace("존나","매우")
		username = message.author.name
		outputmsg = username +": "+ newmsg
		await message.channel.send(outputmsg)
	else if '운지' in message.content:
		newmsg = message.content[:]
		await message.delete()
		newmsg = newmsg.replace("운지","중력500배")
		username = message.author.name
		outputmsg = username +": "+ newmsg
		await message.channel.send(outputmsg)
	else if '일리움' in message.content:
		outputmsg = "직업이 일리움ㅋㅋㅋ"
		await message.channel.send(outputmsg)
		
		

		

		


access_token = os.environ["BOT_TOKEN"]
client.run(access_token)

