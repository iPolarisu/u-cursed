import discord
from utilities import embed as ce
from discord.ext import commands, tasks

class Tests(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot

    # test for last post
    @commands.command()
    @commands.guild_only()
    async def Test(self, ctx, code, section):
        try:
            embed = ce.notificationEmbed(code, section)
            await ctx.send(embed = embed)
        except:
            await ctx.send(content = 'No se ha encontrado información del curso, ejecuta U-Help para más detalles')

# cog loaded
def setup(bot):
    bot.add_cog(Tests(bot))
    print('Tests is loaded.')