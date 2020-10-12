import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    jeff_quotes = ['you are POOR i am RICH', 'dei dei Waiste fellow', 'Po da panni', 'i am the JEFF BOY', 'Rascals, you are in lou with a dou']

    if(message.content.find("jeff") != -1 or message.content.find("Jeff") != -1):
        await message.channel.send(content=random.choice(jeff_quotes),tts=True)

client.run(TOKEN)

