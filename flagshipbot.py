import os
import discord
import random
import json
from dotenv import load_dotenv

intents = discord.Intents.default()
intents.members = True

load_dotenv()
TOKEN = os.getenv('FLAGSHIP_TOKEN')

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
    guild = discord.utils.get(client.guilds,name='platinum hendai')
    botchannel = discord.utils.get(client.get_all_channels(),name='bot-announce')
    await botchannel.send(content="Purging <@&859740424881045504> roles for the day...")
    padikuranda = await botchannel.send(content="Congratulations <@!407265504693059584> for being the Flagship Stedier of the Year!")
    await padikuranda.add_reaction(random.choice(client.emojis))

    role = discord.utils.get(guild.roles, name='Flagship stedier of the day')

    file = open("flagshipdata.txt","r")
    fdata = file.read()
    if(fdata != ''):
        datas = json.loads(fdata)
    else:
        datas = 0
    file.close()

    for stateboard in role.members:
        print(role.name)
        print(stateboard.name)
        try:
            await stateboard.remove_roles(role,reason="Purging for a new day")
        except discord.Forbidden:
            print(f"Forbidden task is being done for {stateboard.name}")
        except discord.HTTPException:
            print("EZ HTTTP funs")

        if(type(datas) != dict):
            datas = {stateboard.name:1}
        elif(stateboard.name not in datas.keys()):
            datas[stateboard.name] = 1
        elif(stateboard.name in datas.keys()):
            datas[stateboard.name] = datas[stateboard.name]+1
        fo = open("flagshipdata.txt","wt")
        fo.write(str(datas).replace("\'","\""))

        msg = await botchannel.send(content=stateboard.name+" was a flagship stedier "+str(datas[stateboard.name])+" times!")
        await msg.add_reaction(random.choice(client.emojis))


client.run(TOKEN)
