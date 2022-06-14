import requests
from utilities.constants.ucursed import YEAR, SEASON
from utilities.constants.departments import DEPARTMENTS
from bs4 import BeautifulSoup

# returns ucampus url given department id (may not work with same prefix for some)
def urlInfo(course_id):
    department_prefix = course_id[:2]
    try:
        department = DEPARTMENTS[department_prefix]
    except:
        False
    return f'https://ucampus.uchile.cl/m/fcfm_catalogo/?semestre={YEAR}{SEASON}&depto={department}'

# scraps urlInfo and returns info from course
def notificationData(urlCurso, course_id):
    
    # setup for BeautifulSoup
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
    # define user-agent
    headers = {'User-Agent': userAgent}
    # requesting page
    page = requests.get(urlCurso, headers = headers)
    # parsed page
    soup = BeautifulSoup(page.content, 'html.parser')

    # get name of course
    courses = soup.find('div', {'id' : 'body'})

    # name of department
    department_name = courses.find('h1').contents[0]
    department_name = department_name.split('-')[1][1:]
    
    # course name h2 
    course_name = courses.find('h2', {'id' : course_id}).contents[0]

    # remove line breaks and styling
    course_name = course_name.replace('\n', '').replace('\t', '')

    # course legend dl leyenda cMA1001
    course_legend = courses.find('dl', {'class' : f'leyenda c{course_id}'})

    # course info
    course_info_values = course_legend.find_all('dd')
    course_info_fields = course_legend.find_all('dt')

    url = None

    # assign url if available and pop element
    if course_info_fields[0].contents[0] == 'Programa':
        url =  course_info_values[0].find('a')['href']
        course_info_fields.pop(0)
        course_info_values.pop(0)
    
    course_info_len = len(course_info_fields)
    # iterate over course info and get content from each field/value
    for i in range(course_info_len):
        course_info_fields[0] = course_info_fields[0].contents[0]
        course_info_values[0] = course_info_values[0].contents[0]

    # get all sections from given course id
    sections_table = courses.find('table', {'class' : f'cursos c{course_id}'}).find('tbody')
    sections_raw = sections_table.find_all('tr')

    sections_info = []
    # parses data from each section of the course
    for section in sections_raw:
        section_info = []

        # find section name/number
        section_name = section.find('h1').contents[0]
        # remove line breaks and styling
        section_name = section_name[3:-2]
        
        # get all teachers for this section
        section_teachers = section.find('ul', {'class' : 'profes'}).find_all('h1')

        # add both section name and teachers names to section info
        section_info.append(section_name)
        for teacher in section_teachers:
            section_info.append(teacher.get_text()[1:])

        # add this section to the full list
        sections_info.append(section_info)

    return course_name, department_name, url, course_info_fields, course_info_values, sections_info