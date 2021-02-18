# Written By: The one, the only Crow
# Date: Feb 18, 2021
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')

intents = discord.Intents().all()
client = discord.Client(intents = intents)

def crowbot():
    @client.event
    async def on_ready():
        for guild in client.guilds:
            if guild.id == SERVER:
                break
        print(
            f'{client.user} is connected to the following servers:\n'
            f'{guild.name} (id: {guild.id})'
        )
        for member in guild.members:
            print(member)

        global members
        members = '\n - '.join([member.name for member in guild.members])

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        caw_message_intake = [
            'caw',
            'ca caw',
            'caw!',
            'look a crow!',
            'it\'s a crow!',
            'crow',
            'crow#2174',
            '@crow#2174',
            '@crow'
        ]
        best_crow_message_intake = [
            'im the best crow',
            'i\'m the best crow',
            '@Crow is the best crow'
        ]
        if message.author.id == 152993332526579712 and message.content.lower() == 'im the best':
            response = "Behold! The almighty Crow!"
            await message.channel.send(response)
        if any(item in message.content.lower() for item in caw_message_intake):
            response = 'CA CAW!!'
            await message.channel.send(response)
        if message.content.startswith('!members'):
            response = members
            await message.channel.send(response)

    client.run(TOKEN)

if __name__ == '__main__':
    crowbot()


