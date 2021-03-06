
import discord
from discord.ext import commands
from discord.utils import get
from pretty_help import PrettyHelp
import json
from pathlib import Path

# TODO 2021-02-28 caleb:
#  - create method to call for message - response interactions (WTF did I mean by this?)
#  - collect heartbeat data from MC server and display it's status with a command (probably something like !MCStatus)
#  - Create DockerFile to AutoDeploy new bot updates
#  - Create CI/CD Pipeline for deploying bot updates

# #INIT# #

configFile = Path(__file__).parent / "configuration.json"

if configFile.exists():
# Get configuration.json
    pass
else:
    print("No token found!")
    inToken = input("Please enter your bot's token: ")
    inServer = input("Please enter your ServerID: ")
    
    data= {
        'token': inToken,
        'prefix': '$',
        'server': inServer
    }
    with open(configFile, 'w') as outfile:
        json.dump(data, outfile)

with open(configFile, "r") as config:
    data = json.load(config)
    token = data["token"]
    prefix = data["prefix"]
    server = data["server"]
# Intents
intents = discord.Intents().all()

bot = commands.Bot(command_prefix=prefix, intents=intents)

# Setting up Help Command Stuff
colorHelp = discord.Color.dark_blue()
bot.help_command = PrettyHelp(color=colorHelp)


initial_extensions = [
    "Cogs.onCommandError",
    "Cogs.commands"
]

print(initial_extensions)

if __name__ == '__main__':
    for extension in initial_extensions:
        try:
            bot.load_extension(extension)
        except Exception as e:
            print(f"Failed to load extension {extension}")

# #RUNNING# #


@bot.event
async def on_ready():
    await bot.change_presence(
        activity=discord.Activity(type=discord.ActivityType.watching, name=f"{bot.command_prefix}help"))
    for guild in bot.guilds:
        if guild.id == server:
            break
        print(
            f'{bot.user} is connected to the following servers:\n'
            f'{guild.name}'
        )
    global members
    members = '\n - '.join([member.name for member in guild.members])
    print(discord.__version__)

@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
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
    if message.author.id == 152993332526579712 and message.content.lower() == 'im the best':
        response = "Behold! The almighty Crow!"
        await message.channel.send(response)
    if any(item in message.content.lower() for item in caw_message_intake):
        response = 'CA CAW!!'
        await message.channel.send(response)

bot.run(token)
