import discord
from courses import scraper as sc

# embed style
red = discord.Colour.red()
botIcon = 'https://cdn.discordapp.com/avatars/745371842570879027/099af3da03aec44ddf54bc8cac02b1e4.png?size=128'
footerText = 'by Polaris | Primavera 2020 | U-Help'
footerIcon = 'https://i.ibb.co/FmRwzfz/integrante.png'

# creates an embed with info from post
def notification(title, url, curso, code, tipo, icon, cargo, name):
        embed = discord.Embed(title = title, color = red)                      # create embed, add title and red colour
        
        if url != None:                                                        # if post has url
                embed = discord.Embed(title = title, url = url, color = red)   # create same embed but w/hyperlink
        
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

# embed with courses of server
def coursesEmbed(server_name, courses):
        embed = discord.Embed(title = server_name, color = red)
        embed.set_thumbnail(url = botIcon)
        embed.add_field(name = "Cursos Agregados", value = courses, inline = True)
        embed.set_footer(icon_url = footerIcon, text = 'https://i.ibb.co/FmRwzfz/integrante.png')
        return embed
