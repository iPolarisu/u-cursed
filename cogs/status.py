import discord
from discord.ext import commands, tasks

# images
botIcon = 'https://cdn.discordapp.com/avatars/745371842570879027/099af3da03aec44ddf54bc8cac02b1e4.png?size=128'
footerIcon = 'https://i.ibb.co/FmRwzfz/integrante.png'

# info
version = '0.4.0'
footerText = 'by Polaris | Primavera 2020 | U-Help'

class Status(commands.Cog):
    def __init__(self, bot, *args, **kwargs):
        self.bot = bot
    
    # gives current status of bot
    @commands.command()
    @commands.guild_only()
    async def Status(self, ctx):
        embed = discord.Embed(title = 'Current Status', color = discord.Colour.red())                 # embed creation
        embed.set_thumbnail(url = botIcon)                                                            # add botPic 
        embed.add_field(name = 'Version', value = version, inline = True)                             # add version field
        embed.add_field(name = 'Ping', value = f'{round(self.bot.latency*1000)}ms', inline = True)    # add ping field 
        embed.add_field(name = 'Guilds', value = f'{len(self.bot.guilds)}', inline = True)            # add guilds field
        embed.set_footer(icon_url = footerIcon, text = footerText)                                        # set footer
        await ctx.send(embed = embed)

# cog loaded
def setup(bot):
    bot.add_cog(Status(bot))
    print('Status is loaded.')