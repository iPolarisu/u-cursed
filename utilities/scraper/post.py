import requests
from utilities.constants import cargos
from utilities.constants.ucursed import YEAR, SEASON
from bs4 import BeautifulSoup

# returns course's history url
def urlHist(code, section):
        return f'https://www.u-cursos.cl/ingenieria/{YEAR}/{SEASON}/{code}/{section}/historial/'

# scrapes course's history for the requested post
# TO DO: Adapt so scraper is able to select a finite number of posts (not just one)
def postData(urlHist):
    
    # setup for BeautifulSoup
    userAgent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:80.0) Gecko/20100101 Firefox/80.0'
    # define user-agent
    headers = {'User-Agent': userAgent}
    # requesting page
    page = requests.get(urlHist, headers = headers)
    # parsed page
    soup = BeautifulSoup(page.content, 'html.parser')

    # code and curso from url
    codeCurso = soup.find('h2').get_text()
    # info list
    codeCurso = codeCurso.split(' ',1)

    # obtaining code and curso from list
    code = codeCurso[0]
    curso = codeCurso[1]
    
    # data from last post
    postList = soup.find('ul', class_ = 'objetos c_0')
    post = postList.find('li')
    
    # data from h1
    h1 = post.h1
    
    # from img
    img1 = h1.img
    icon = img1['src']
    tipo = img1['alt']
    
    # from a
    a = h1.a

    # check if post has url
    if a:
        url = a['href']
        title = a.get_text()
    else:
        url = None
        title = h1.get_text()[:-26]

    # data from h2
    h2 = post.h2
    # op name
    name = h2.get_text()[8:-5]

    # from img 2
    if h2.find('img', class_ = 'cargo'):
        img2 = h2.img
        cargo = img2['title']
        cargo = cargos.CARGOS[cargo]
    else:
        cargo = None

    return (title, url, curso, code, tipo, icon, cargo, name)