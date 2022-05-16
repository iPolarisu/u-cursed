import discord
from utilities import scraper as sc

EMBED_COLOR = discord.Colour.red

# creates an embed with info from post
def notification(title, url, curso, code, tipo, icon, cargo, name):
        embed = discord.Embed(title = title, color = EMBED_COLOR)                      # create embed, add title and red colour
        
        if url != None:                                                        # if post has url
                embed = discord.Embed(title = title, url = url, color = EMBED_COLOR)  # create same embed but w/hyperlink
        
        embed.add_field(name = curso, value = code+' | '+tipo)                 # add post info
        embed.set_thumbnail(url = icon)                                        # add post icon
        embed.set_footer(text = name)                                          # add poster name
        
        if cargo != None:                                                      # if poster has cargo
                embed.set_footer(icon_url = cargo, text = name)                # add image            

        return embed

# embed of last post given code and section
def notificationEmbed(code, section):
        try:
                urlCursoData = sc.urlCurso(code, section)                     
                data = sc.notificationData(urlCursoData)   
                title = data[0]                                         
                url = data[1]
                curso = data[2]
                code = data[3]
                tipo = data[4]
                icon = data[5]
                cargo = data[6]
                name = data[7]
                embed = notification(title, url, curso, code, tipo, icon, cargo, name)
                return (embed, curso, title)
        except:
                return False
