import discord
from utilities.constants import ucursed
from discord.ext import commands, tasks

class Help(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        self.bot.remove_command('help')
    
    # bot usage explanation
    @commands.command()
    @commands.guild_only()
    async def help(self, ctx):
        author = ctx.author
        embed = discord.Embed(title = 'Helperino', color = discord.Colour.red())
        #embed.set_image(url = helpIcon)
        embed.add_field(name = 'U-Cursed', value = 'Hola', inline = False)
        embed.set_footer(icon_url = ucursed.FOOTER_ICON, text = ucursed.SEMESTER)
        await author.send(embed = embed)
        await ctx.send(content = f'Revisa tus DMs {author.mention}')

# cog loaded
def setup(bot):
    bot.add_cog(Help(bot))
    print('Help is loaded.')