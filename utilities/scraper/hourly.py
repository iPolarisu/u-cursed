import requests
from bs4 import BeautifulSoup

# returns course's schedule url
def urlHourly(code, section):
        return f'https://www.u-cursos.cl/ingenieria/2022/1/{code}/{section}/horario_curso/'

# scrapes course's schedule for the requested week
def notificationData(urlHourly, requested_week):
    
    # setup for BeautifulSoup
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
    # define user-agent
    headers = {'User-Agent': userAgent}
    # requesting page
    page = requests.get(urlHourly, headers = headers)
    # parsed page
    soup = BeautifulSoup(page.content, 'html.parser')

    # get name of course
    course_name = soup.find('div', {'class' : 'cont'}).find('span').contents[0]
    
    # get current week's schedule
    schedule = soup.find('div', {'class' : 'ucursos horario_curso modern'})

    # check if user wanted this week or another one
    if requested_week != 0:
        weeks = schedule.find('ul', {'class' : 'paginas'}).findAll('a')
        week = weeks[requested_week]['href']
        urlHourly += week
        return notificationData(urlHourly, 0)

    # requested week's date
    this_week = schedule.find('h1').contents[0]

    # day's name and date
    days_date = schedule.find('thead').findAll('span', {'class' : 'no-movil'})

    # get content for each day
    days_content = schedule.find('table').find('tbody').findAll('td')
    
    # add relevant data
    days_data = []
    for day, day_content in enumerate(days_content):
        blocks = day_content.findAll('div', {'class':'bloque'})
        if blocks:
            day_data = []
            day_date = days_date[day].contents[0]
            day_data.append(day_date)
            for block in blocks:
                class_info = block.find('h1')
                class_type = class_info.contents[0]
                class_room = class_info.find('strong').contents[0]
                class_time = block.find('em').contents[0]
                day_data.append(class_type)
                day_data.append(class_room)
                day_data.append(class_time)
            days_data.append(day_data)
    
    return course_name, this_week, days_data