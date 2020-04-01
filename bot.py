# bot.py

# liberally borrowed from https://realpython.com/how-to-make-a-discord-bot-python/

import os

import discord
import asyncio
import requests

from zerotier import zerotier

from dotenv import load_dotenv
load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD = os.getenv('DISCORD_GUILD')
DISCORD_ZEROTIERCHANNEL = os.getenv('DISCORD_ZEROTIERCHANNEL')
ZEROTIER_NETWORK = os.getenv('ZEROTIER_NETWORK')
ZEROTIER_TOKEN = os.getenv('ZEROTIER_TOKEN')

print("Hello, world! We're using this bot token:\n{}".format(DISCORD_TOKEN))

client = discord.Client()

api = zerotier(ZEROTIER_TOKEN, ZEROTIER_NETWORK)

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # create the background task and run it in the background
        self.bg_task = self.loop.create_task(self.my_background_task())

    async def on_ready(self):
        print('Logged in as')
        print(self.user.name)
        print(self.user.id)
        print('------')

    async def my_background_task(self):
        await self.wait_until_ready()
        counter = 0
        channel = self.get_channel(int(DISCORD_ZEROTIERCHANNEL)) # channel ID goes here
        print(channel.name)
        while not self.is_closed():
            counter += 1
            print(counter)
            await channel.send("```ZEROTIER DEVICES:\n{}```".format(api.stringmembers()))
            await asyncio.sleep(60) # task runs every 5 seconds



if(1==1):
    client = MyClient()
    client.run(DISCORD_TOKEN)