import discord
from utilities.scraper.info import urlInfo, notificationData
from utilities.constants.ucursed import EMBED_COLOR, SEMESTER

# create post embed given notification info
def embedInfo(course_name, department_name, url, course_info_fields, course_info_values, sections_info):

        embed = discord.Embed(title = course_name, description = department_name, color = EMBED_COLOR)

        if url:
                embed = discord.Embed(title = course_name, url = url, description = department_name, color = EMBED_COLOR)
        
        # adding course info to the embed
        for field, value in zip(course_info_fields, course_info_values):
                embed.add_field(name = field, value = value, inline = False)

        # mapping the info of each section
        sections = ''
        for section in sections_info:
                section_info = ''
                section_info += f'**{section[0]}:**\n'
                for teacher in section[1:]:
                        section_info += f'{teacher}\n'

                sections += section_info
        
        embed.add_field(name = 'Secciones', value = sections, inline = False)
        
        # embed.set_thumbnail(url = SCHEDULE_ICON)

        embed.set_footer(text = SEMESTER)

        return embed

# embed of last post given code and section
def notificationEmbed(code):
       # try:
        urlInfoData = urlInfo(code)
        data = notificationData(urlInfoData)
        course_name = data[0]
        department_name = data[1]
        url = data[2]
        course_info_fields = data[3]
        course_info_values = data[4]
        sections_info = data[5]
        embed = embedInfo(course_name, department_name, url, course_info_fields, course_info_values, sections_info)
        return embed
        #except:
         #       return False
