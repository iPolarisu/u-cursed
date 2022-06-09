import discord
from utilities.scraper.hourly import urlHourly, notificationData

EMBED_COLOR = 0xff0000

# create post embed given notification info
def embed(course_name, week, days_data):
        embed = discord.Embed(title = course_name, description = week ,color = EMBED_COLOR)
        
        for day in days_data:
                day_name = day[0]
                class_types = day[1::3]
                class_rooms = day[2::3]
                class_times = day[3::3]
                class_info = ""
                for typ, room, time in zip(class_types, class_rooms, class_times):
                        class_info += f"{typ} | {room} \n {time} \n"

                embed.add_field(name = day_name, value = class_info, inline = False)
        
        #embed.set_thumbnail(url = icon)
        #embed.set_footer(text = name)

        return embed

# embed of last post given code and section
def notificationEmbed(code, section, week):
        #try:
        urlHistData = urlHourly(code, section)
        data = notificationData(urlHistData, week)
        course_name = data[0]
        week = data[1]
        days_data = data[2]
        embed = embed(course_name, week, days_data)
        return embed
        #except:
         #       return False
