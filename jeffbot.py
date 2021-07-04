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

    seskipnow_emojis = ['<:seksipnow:738364549857673307>','<:GodIsDead:802377987302752266>','<:seskichad:755620465153802320>','<:padikuranda:798197283983982654>','<:TargetEngaged:818493944001855511>','<:NoseyBoi:768846530823847937>']

    if(message.content.find("jeff") != -1 or message.content.find("Jeff") != -1 or message.content.find("JEFF") != -1):
        await message.channel.send(content=random.choice(jeff_quotes),tts=False)

    if(message.content.find("seski") != -1 or message.content.find("Seski") != -1 or message.content.find("pnow") != -1 or message.content.find("Pnow") != -1):
        await message.channel.send(content=random.choice(seskipnow_emojis),tts=False)

    if(message.content.find("SHIVOUDITYOW") != -1):
        await message.channel.send(content='https://www.youtube.com/watch?v=st5AgmryAYU&feature=share',tts=False)

client.run(TOKEN)

