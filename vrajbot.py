import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('VRAJ_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    jeff_quotes = ['Yo wtf', 'Wtaf', 'gg', 'Why are you gay', 'CF sucks I hate it', 'Malayalis drive me up the wall', 'I am very funny XD XD','F']

    if(message.content.find("Vraj") != -1 or message.content.find("Viraj") != -1 or message.content.find("Gandhi") != -1 or message.content.find("dumb coder") != -1):
        await message.channel.send(content=random.choice(jeff_quotes),tts=True)

client.run(TOKEN)

