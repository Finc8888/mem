import requests      # Библиотека для отправки запросов
#import numpy as np   # Библиотека для матриц, векторов и линала
#import pandas as pd  # Библиотека для табличек
import time          # Библиотека для тайм-менеджмента

page_link = 'http://knowyourmeme.com/memes/all/page/1'
response1 = requests.get(page_link)
print(response1)


for key, value in response1.request.headers.items():
    print(key+": "+value)

# подгрузим один из методов этой библиотеки
from fake_useragent import UserAgent
UserAgent().chrome
