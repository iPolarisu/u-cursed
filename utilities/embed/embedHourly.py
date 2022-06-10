import discord
from utilities.scraper.hourly import urlHourly, notificationData
from utilities.constants.ucursed import EMBED_COLOR
from utilities.constants.hourly import SCHEDULE_ICON

# create post embed given notification info
def embedHourlyGen(course_name, code, section, week, days_data):
        embed = discord.Embed(title = course_name, description = week ,color = EMBED_COLOR)
        
        # mapping the info of each day's blocks to a field (they come in groups of 3)
        for day in days_data:
                day_name = day[0]
                class_types = day[1::3]
                class_rooms = day[2::3]
                class_times = day[3::3]
                class_info = ""
                for typ, room, time in zip(class_types, class_rooms, class_times):
                        class_info += f"{typ} | {room} \n {time} \n\n"

                embed.add_field(name = day_name, value = class_info, inline = False)
        
        embed.set_thumbnail(url = SCHEDULE_ICON)
        embed.set_footer(text = f'{code}-{section}')

        return embed

# embed of last post given code and section
def notificationEmbed(code, section, week):
        try:
                urlHistData = urlHourly(code, section)
                data = notificationData(urlHistData, week)
                course_name = data[0]
                week = data[1]
                days_data = data[2]
                embed = embedHourlyGen(course_name, code, section, week, days_data)
                return embed
        except:
                return False
