import discord
from utilities.scraper.post import urlHist, postData
from utilities.constants.ucursed import EMBED_COLOR

# create post embed given notification info
def embedPostGen(title, url, curso, code, tipo, icon, cargo, name):
        embed = discord.Embed(title = title, color = EMBED_COLOR)
        
        # add hyperlink if available
        if url:
                embed = discord.Embed(title = title, url = url, color = EMBED_COLOR)
        
        embed.add_field(name = curso, value = code+' | '+tipo)
        embed.set_thumbnail(url = icon)
        embed.set_footer(text = name)

        # add cargo if available
        if cargo:
                embed.set_footer(icon_url = cargo, text = name)

        return embed

# embed of last post given code and section
def notificationEmbed(code, section):
        try:
                urlHistData = urlHist(code, section)                     
                data = postData(urlHistData)  
                title = data[0]                                         
                url = data[1]
                curso = data[2]
                code = data[3]
                tipo = data[4]
                icon = data[5]
                cargo = data[6]
                name = data[7]
                embed = embedPostGen(title, url, curso, code, tipo, icon, cargo, name)
                return embed
        except:
                return False
