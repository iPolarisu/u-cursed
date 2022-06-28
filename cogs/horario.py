import discord
from utilities.embed import embedHourly
from utilities.constants.error import NO_HOURLY
from utilities.constants.hourly import WEEK
from discord.ext import commands, tasks

class Horario(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    # returns an embeded version of course's schedule
    @commands.command()
    @commands.guild_only()
    async def horario(self, ctx, code, section, week='act'):
        try:
            code = code.upper()
            week = WEEK[week]
            embed = embedHourly.notificationEmbed(code, section, week)
            await ctx.send(embed = embed)
        except:
            await ctx.send(content = NO_HOURLY)

# cog loaded
def setup(bot):
    bot.add_cog(Horario(bot))
    print('Horario is loaded.')