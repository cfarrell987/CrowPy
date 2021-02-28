import discord
from discord.ext import commands
from discord.utils import get
import json

# TODO 2021-02-24 caleb:
# - change over basic text based commands to actual discord API commands(Semi Completed)
# - create method to call for message - response interactions (WTF did I mean by this?)
# - collect heartbeat data from MC server and display it's status with a command (probably something like !MCStatus)
# - add Initial start flag for the first run of the bot to generate configuration.json, and prompt for token,prefix etc.
# - transfer logic from old python script to new one

# #INIT# #

# Get configuration.json
with open("configuration.json", "r") as config:
    data = json.load(config)
    token = data["token"]
    prefix = data["prefix"]
    server = data["server"]


class Greetings(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self._last_member = None


bartenderRole = '<@&794666590532665345>'
admin = '<@&794628837891768340>'
mod = '<@&794687361329266690>'

# Intents
intents = discord.Intents().all()

bot = commands.Bot(command_prefix=prefix, intents=intents)

# Load cogs
initial_extensions = [
    "Cogs.onCommandError",
    "Cogs.help",
    "Cogs.ping"
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


@bot.command(name="members", aliases=["users", "mem"])
async def members(ctx):
    await ctx.channel.send(members)


# bartenderRole = get(discord.Guild.roles, id=794666590532665345)


@bot.command(name="bartender", aliases=["drinks"])
async def bartender(ctx):
    await ctx.channel.send(f"{bartenderRole} You are needed!")
    # print(bartenderRole)


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
    commands = [
        # '!members',
        # '!bartender',
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
    if message.content.startswith('!admin'):
        response = f'{admin} You are needed'
        await message.channel.send(response)
    if message.content.startswith('!mod'):
        response = f'{mod} You are needed'
        await message.channel.send(response)
    if message.content.startswith('!commands'):
        response = '\n'.join([item for item in commands])
        # print( '\n'.join(item for item in commands))
        await message.channel.send(response)


bot.run(token)
