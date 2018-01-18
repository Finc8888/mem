import requests      # Библиотека для отправки запросов
import numpy as np   # Библиотека для матриц, векторов и линала
import pandas as pd  # Библиотека для табличек
import time          # Библиотека для тайм-менеджмента
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

page_link = 'http://knowyourmeme.com/memes/all/page/1'
response1 = requests.get(page_link)
print('403-я ошибка - cервер дост-н и спос-н обраб-ть запросы, но не делает это'.center(80,'*'))
print(response1,'\n')

#User-Agent в глазах сервера
for key, value in response1.request.headers.items():
    print(key+": "+value)
print('Use fake_useragent module'.center(60,'*')) 

# подгрузим один из методов этой библиотеки
response = requests.get(page_link, headers={'User-Agent': UserAgent().chrome})
print(response,'\n')
print(UserAgent().chrome)

print('Получение контента с сайта мемов'.center(60,'*')) 
html = response.content
print(html[:2000])

soup = BeautifulSoup(html,'html.parser') # В опции также можно указать lxml,
                                         # если предварительно установить одноименный пакет
print(soup)
soup1 = soup.html.head.title
print('soup.html.head.title'.center(40,'*'),'\n',soup1)

soup2 = soup.html.head.title.text
print('soup.html.head.title.text'.center(40,'*'),'\n',soup2)
