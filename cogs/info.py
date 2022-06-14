import discord
from utilities.embed import embedInfo
from utilities.constants.error import NO_STATUS
from discord.ext import commands, tasks

class Info(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
    
    # embeds current status of bot
    @commands.command()
    @commands.guild_only()
    async def info(self, ctx, code):
        #try:
        embed = embedInfo.notificationEmbed(code)
        await ctx.send(embed = embed)
        #except:
         #   await ctx.send(content = NO_STATUS)

# cog loaded
def setup(bot):
    bot.add_cog(Info(bot))
    print('Info is loaded.')