import discord
from utilities.embed import embedPost as ep
from utilities.constants.error import NO_COURSE
from discord.ext import commands, tasks

class Tests(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    # test for last post
    @commands.command()
    @commands.guild_only()
    async def test(self, ctx, code, section):
        #try:
        code = code.upper()
        embed = ep.notificationEmbed(code, section)
        await ctx.send(embed = embed)
        #except:
            #await ctx.send(content = NO_COURSE)

# cog loaded
def setup(bot):
    bot.add_cog(Tests(bot))
    print('Tests is loaded.')