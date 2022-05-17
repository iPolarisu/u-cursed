import requests
from utilities import ucursed
from bs4 import BeautifulSoup

# gives history url of given code and section 
def urlCurso(code, section):
        return f'https://www.u-cursos.cl/ingenieria/2022/1/{code}/{section}/historial/'

# scrapes urlCurso and returns info from last post
def notificationData(urlCurso):
    # setup for BeautifulSoup
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
    headers = {'User-Agent': userAgent}                     # define user agent
    page = requests.get(urlCurso, headers = headers)        # requesting page
    soup = BeautifulSoup(page.content, 'html.parser')       # parsed page
    
    # code and curso from url
    codeCurso = soup.find('h2').get_text()                  # general info of curso
    codeCurso = codeCurso.split(' ',1)                      # info list

    # obtaining code and curso from list
    code = codeCurso[0]                                     # code curso
    curso = codeCurso[1][:-16]                              # name curso
    
    # data from last post
    postList = soup.find('ul', class_ = 'objetos c_0')      # list of posts
    post = postList.find('li')                              # last post
    
    # data from h1
    h1 = post.h1
    
        # from img
    img1 = h1.img
    icon = img1['src']                                      # icon of post type
    tipo = img1['alt']                                      # post type
    
        # from a
    a = h1.a
    if a != None:                                           # check if post has url
        url = a['href']                                     # add url
        title = a.get_text()                                # post title w/url
    else:
        url = None                                          # don't add url
        title = h1.get_text()[:-26]                         # post title w/o url
    
    # data from h2
    h2 = post.h2
    name = h2.get_text()[8:-5]                              # op name 
    
        # from img 2
    if h2.find('img', class_ = 'cargo') != None:            # check if op has cargo
        img2 = h2.img
        cargo = img2['title']
        cargo = ucursed.CARGOS[cargo]                       # cargo                       
    else:
        cargo = None                                        # no cargo
    
    return (title, url, curso, code, tipo, icon, cargo, name)