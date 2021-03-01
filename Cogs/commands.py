import discord
from discord.ext import commands

bartenderRole = '<@&794666590532665345>'
adminRole = '<@&794628837891768340>'
modRole = '<@&794687361329266690>'


class CommandsCog(commands.Cog, name="Commands", description="List of Commands"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        name="members",
        aliases=["users", "mem"],
        help="Lists all members in the server",
        brief="List members"
    )
    async def members(self, ctx):

        global members
        members = '\n - '.join([member.name for member in ctx.message.guild.members])
        await ctx.channel.send("Members: " + "\n - " + members)

    @commands.command(
        name="bartender",
        aliases=["drinks"],
        help="Pings for the bartenders of the server",
        brief="Pings for the bartenders of the server"
                 )
    async def bartender(self, ctx):
        await ctx.channel.send(f"{bartenderRole} You are needed!")
        # print(bartenderRole)

    @commands.command(
        name="admin",
        aliases=["owner"],
        help="Pings for the administrator/Owner of the server",
        brief="Pings for the admins/Owner of the server"

                )
    async def admin(self, ctx):
        await ctx.channel.send(f"{adminRole} You are needed!")
        # print(bartenderRole)

    @commands.command(
        name="mod",
        aliases=["moderator"],
        help="Pings for the moderators of the server",
        brief="Pings for the mods of the server"
        )
    async def mod(self, ctx):
        await ctx.channel.send(f"{modRole} You are needed!")
        # print(bartenderRole)@bot.command(


def setup(bot):
    bot.add_cog(CommandsCog(bot))
