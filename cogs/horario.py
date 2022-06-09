import discord
from utilities.embed import hourlyEmbed
from utilities.constants.error import NO_HOURLY
from utilities.constants.weeks import WEEK
from discord.ext import commands, tasks

class Horario(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    # test for last post
    @commands.command()
    @commands.guild_only()
    async def horario(self, ctx, code, section, week='act'):
        try:
            code = code.capitalize()
            week = WEEK[week]
            print(week)
            embed = hourlyEmbed.notificationEmbed(code, section, week)
            await ctx.send(embed = embed)
        except:
            await ctx.send(content = NO_HOURLY)

# cog loaded
def setup(bot):
    bot.add_cog(Horario(bot))
    print('Horario is loaded.')