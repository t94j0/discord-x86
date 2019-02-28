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
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('x86'):
        instruction = random_x86()
        url = '%s%s' % (URL, instruction['link'])
        await client.send_message(
            message.channel,
            '%s is a fun one: %s' % (instruction['instruction'], url))


def random_x86():
    with open('x86.json') as f:
        data = f.read()
        arr = json.loads(data)
        return random.choice(arr)


client.run(TOKEN, bot=True)
