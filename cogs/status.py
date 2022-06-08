import discord
from utilities.constants import ucursed
from discord.ext import commands, tasks

class Status(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
    
    # gives current status of bot
    @commands.command()
    @commands.guild_only()
    async def status(self, ctx):
        embed = discord.Embed(title = 'Current Status', color = discord.Colour.red())
        embed.set_thumbnail(url = ucursed.BOT_ICON)
        embed.add_field(name = 'Version', value = 'N/A', inline = True)
        embed.add_field(name = 'Ping', value = f'{round(self.bot.latency*1000)}ms', inline = True)
        embed.add_field(name = 'Guilds', value = f'{len(self.bot.guilds)}', inline = True)
        embed.set_footer(icon_url = ucursed.FOOTER_ICON, text = ucursed.SEMESTER)
        await ctx.send(embed = embed)

# cog loaded
def setup(bot):
    bot.add_cog(Status(bot))
    print('Status is loaded.')