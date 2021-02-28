import discord
from discord.ext import commands
from discord.utils import get
from pretty_help import PrettyHelp
import json

# TODO 2021-02-24 caleb:
# - change over basic text based commands to actual discord API commands(Semi Completed)
# - create method to call for message - response interactions (WTF did I mean by this?)
# - collect heartbeat data from MC server and display it's status with a command (probably something like !MCStatus)
# - add Initial start flag for the first run of the bot to generate configuration.json, and prompt for token,prefix etc.
# - transfer logic from old python script to new one
# <- (Pretty much done, will check again before adding crowold.py to gitignore)


# #INIT# #

# Get configuration.json
with open("configuration.json", "r") as config:
    data = json.load(config)
    token = data["token"]
    prefix = data["prefix"]
    server = data["server"]

bartenderRole = '<@&794666590532665345>'
adminRole = '<@&794628837891768340>'
modRole = '<@&794687361329266690>'

# Intents
intents = discord.Intents().all()

bot = commands.Bot(command_prefix=prefix, intents=intents)

# Setting up Help Command Stuff
colorHelp = discord.Color.dark_blue()
bot.help_command = PrettyHelp(color=colorHelp)


initial_extensions = [
    "Cogs.onCommandError",
    #"Cogs.help",
    #"Cogs.ping"
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


class Commands(commands.Cog, name="Commands", description="List of Commands"):
    @commands.command(
        name="members",
        aliases=["users", "mem"],
        help="Lists all members in the server",
        brief="List members"
    )
    async def members(ctx):
        await ctx.channel.send(members)

    @commands.command(
        name="bartender",
        aliases=["drinks"],
        help="Pings for the bartenders of the server",
        brief="Pings for the bartenders of the server"
                 )
    async def bartender(ctx):
        await ctx.channel.send(f"{bartenderRole} You are needed!")
        # print(bartenderRole)

    @commands.command(
        name="admin",
        aliases=["owner"],
        help="Pings for the administrator/Owner of the server",
        brief="Pings for the admins/Owner of the server"

                )
    async def admin(ctx):
        await ctx.channel.send(f"{adminRole} You are needed!")
        # print(bartenderRole)

    @commands.command(
        name="mod",
        aliases=["moderator"],
        help="Pings for the moderators of the server",
        brief="Pings for the mods of the server"
        )
    async def mod(ctx):
        await ctx.channel.send(f"{modRole} You are needed!")
        # print(bartenderRole)@bot.command(


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
    if message.content.startswith('!commands'):
        response = '\n'.join([item for item in commands])
        # print( '\n'.join(item for item in commands))
        await message.channel.send(response)


bot.add_cog(Commands(bot))
bot.run(token)
