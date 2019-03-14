import discord
import os
import random
import json
from bs4 import BeautifulSoup

URL = 'https://www.felixcloutier.com/x86'
TOKEN = os.environ['TOKEN']

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print('------')


@client.event
async def on_message(message):
    if not 'x86' not in message.content:
        return
    instruction = random_x86()
    url = f'{URL}{instruction["link"]}'
    await client.send_message(
        message.channel,
        f'{instruction["instruction"]} is a fun one: {url}'


def random_x86():
    with open('x86.json') as f:
        data = f.read()
        arr = json.loads(data)
        return random.choice(arr)


client.run(TOKEN, bot=True)
