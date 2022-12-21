# Написать простой парсер для извлечения информации с любого сайта.
# Например - новость, или погоду с сайта mail.ru

import requests
import os
from bs4 import BeautifulSoup as bs

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def pogoda_tomorrow(url_tomorrow):
    response = requests.get(url_tomorrow).text
    soup = bs(response, 'html.parser')
    # print(soup)
    city = soup.find('h1', class_='h1')
    weather = soup.find('p',class_="wthSBlock__commonWth")
    print(city.text)
    print('Температура в градусах:', weather.text)

def pogoda_today(url_today):
    response = requests.get(url_today).text
    soup = bs(response, 'html.parser')
    # print(soup)
    city = soup.find('h1', class_='h1')
    weather = soup.find('p',class_="wthSBlock__commonWth")
    print(city.text)
    print('Температура в градусах:', weather.text)

def pogoda_today_hr(url_today):
    list_1 = {}
    response_1 = requests.get(url_today).text
    soup = bs(response_1, 'html.parser')
    for x in soup.find_all('p', class_='wthSBlock__commonTime'):
        if x == 'День':
            continue
        for a in soup.find_all('p', class_="wthSBlock__commonWth"):
            list_1[x.text] = a.text
    list_1['  13:00    '] = list_1.pop('  День   13:00  ')
    list_1['  03:00    '] = list_1.pop('  Ночь   03:00  ')
    for k, v in list_1.items():
        print(k,v)
        

while True:
    url_tomorrow = 'https://meteolabs.ru/погода_санкт-петербург/завтра/' 
    url_today = 'https://meteolabs.ru/погода_санкт-петербург/сегодня/'
    print('Погода с сайта https://meteolabs.ru')
    user_input = int(input('1: Погода Сегодня\n2: Погода завтра\n3: Погода почасам\nВведите число:>'))
    if user_input == 1:
        cls()
        pogoda_today(url_today)
    elif user_input == 2:
        cls()
        pogoda_tomorrow(url_tomorrow)
    elif user_input == 3:
        cls()
        pogoda_today_hr(url_today)
    else:
        cls()
        print('Что-то вводите не так')
        break