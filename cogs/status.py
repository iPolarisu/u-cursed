import discord
from utilities.embed import embedStatus
from utilities.constants.error import NO_STATUS
from discord.ext import commands, tasks

class Status(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
    
    # embeds current status of bot
    @commands.command()
    @commands.guild_only()
    async def status(self, ctx):
        try:
            ping = f'{round(self.bot.latency*1000)}ms'
            guilds = f'{len(self.bot.guilds)}'
            embed = embedStatus.embedStatusGen(ping, guilds)
            await ctx.send(embed = embed)
        except:
            await ctx.send(content = NO_STATUS)

# cog loaded
def setup(bot):
    bot.add_cog(Status(bot))
    print('Status is loaded.')