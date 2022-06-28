import discord
from utilities.constants.ucursed import *

# creates an embed with useful information about the bot
# TO DO: Fix hard-coding
def embedHelpGen():
        embed = discord.Embed(title = BOT_NAME, description = BOT_DESC, color = EMBED_COLOR)

        # general info
        embed.add_field(name = 'About', value = BOT_INFO_ABOUT, inline = False)

        # commands info
        embed.add_field(name = 'Commands', value = BOT_INFO_COMMANDS, inline = False)

        # disclaimer
        embed.add_field(name = 'Disclaimer', value = BOT_INFO_DISCLAIMER, inline = False)

        embed.set_footer(icon_url = FOOTER_ICON, text = SEMESTER)

        return embed