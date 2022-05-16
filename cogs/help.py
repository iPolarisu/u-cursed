import discord
from discord.ext import commands, tasks

# images
helpIcon = 'https://i.ibb.co/dKsjvF5/questionmark.png'
footerIcon = 'https://i.ibb.co/FmRwzfz/integrante.png'

# text
footerText = 'by Polaris | Primavera 2020 | U-Help'

class Help(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
        self.bot.remove_command('help')
    
    # bot usage explanation
    @commands.command()
    @commands.guild_only()
    async def Help(self, ctx):
        author = ctx.author
        embed = discord.Embed(title = 'Helperino', color = discord.Colour.red())
        embed.set_image(url = helpIcon)
        embed.add_field(name = 'U-Cursed', value = 'Hola', inline = False)
        embed.set_footer(icon_url = footerIcon, text = footerText)
        await author.send(embed = embed)
        await ctx.send(content = f'Revisa tus DMs {author.mention}')

# cog loaded
def setup(bot):
    bot.add_cog(Help(bot))
    print('Help is loaded.')