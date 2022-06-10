import discord
from utilities.constants.ucursed import *

# create post embed given notification info
def embedStatusGen(ping, guilds):
        embed = discord.Embed(title = 'Status', color = EMBED_COLOR)
        
        embed.add_field(name = 'Version', value = '0.1', inline = True)
        embed.add_field(name = 'Ping', value = ping, inline = True)
        embed.add_field(name = 'Guilds', value = guilds, inline = True)

        embed.set_thumbnail(url = BOT_ICON)
        embed.set_footer(icon_url = FOOTER_ICON, text = SEMESTER)

        return embed