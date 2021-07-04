import os
import discord
import random
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('FLAGSHIP_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    guild = client.guilds[0]
    botchannel = discord.utils.get(client.get_all_channels(),name='bot-announce')
    await botchannel.send(content="Purging <@&859740424881045504> roles for the day...")
    padikuranda = await botchannel.send(content="Congratulations <@!407265504693059584> for being the Flagship Stedier of the Year!")
    await padikuranda.add_reaction(random.choice(client.emojis))

client.run(TOKEN)
