# Written By: The one, the only Crow
# Date: Feb 18, 2021
import os
import discord
from dotenv import load_dotenv
#TODO 2021-02-20 caleb:
# - convert from CLIENT to BOT
# - change over basic text based commands to actual discord API commands
# - create method to call for message - response interactions
# - collect heartbeat data from MC server and display it's status with a command (probably something like !MCStatus)
# - Add Initial start flag for initial start flag

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
SERVER = os.getenv('DISCORD_SERVER')
intents = discord.Intents().all()
client = discord.Client(intents=intents)

#Roles
bartender = '<@&794666590532665345>'
admin = '<@&794628837891768340>'
mod = '<@&794687361329266690>'
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
        ]
        best_crow_message_intake = [
            'im the best crow',
            'i\'m the best crow',
            '@Crow is the best crow'
        ]
        commands = [
            '!members',
            '!bartender',
            '!admin',
            '!mod',
            '!commands'
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
        if message.content.startswith('!bartender'):
            response = f'{bartender} you are being called!'
            await message.channel.send(response)
        if message.content.startswith('!admin'):
            response = f'{admin} You are needed'
            await message.channel.send(response)
        if message.content.startswith('!mod'):
            response =f'{mod} You are needed'
            await message.channel.send(response)
        if message.content.startswith('!commands'):
            response = '\n'.join([item for item in commands])
            #print( '\n'.join(item for item in commands))
            await message.channel.send(response)

    client.run(TOKEN)

if __name__ == '__main__':
    crowbot()


