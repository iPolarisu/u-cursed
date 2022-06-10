import discord
from utilities.constants.ucursed import *

# creates an embed with useful information about the bot
def embedHelpGen():
        embed = discord.Embed(title = 'Helperino', color = EMBED_COLOR)
        embed.add_field(name = 'U-Cursed', value = 'Sample text', inline = False)
        embed.set_footer(icon_url = FOOTER_ICON, text = SEMESTER)

        return embed