# 1)
# Написать программу, где создадим класс Soup (для определения типа супа), принимающий 1 аргумент - который отвечает за основной продукт к выбираемому супу.
# В этом классе создать метод show_my_soup(), выводящий на печать «Суп - {Основной продукт}» в случае наличия добавки
# Это как доп к этой задаче - иначе отобразится следующая фраза: «Обычный кипяток»

import os
import time


class Soup:  
    """Базовый класс для всех сотрудников"""  
    soup_count = 1
    list_arg_gramm = {'Обычный кипяток': 1000}
  

    def cls():
        os.system('cls' if os.name=='nt' else 'clear')

    def append_list(list_arg_gramm, user_list):
        
        Soup.list_arg_gramm = list_arg_gramm | user_list
        Soup.soup_count += 1
        return Soup.list_arg_gramm
        

    def display_count(self):  
        print('Всего ингридиентов: %d' % Soup.soup_count)
        
    def show_my_soup (list_arg_gramm):
        
        for key, value in list_arg_gramm.items():
            print(f'Наименование: {key} // Вес: {value}')
        
  

    def user_arg():
        user_arg, user_gramm = (input('Введите наименование ингридиента и вес: ""Мясо 200"').split())
        user_list = {}
        user_list[user_arg] = user_gramm
        print(user_list)
        return user_list
        
    def del_list(list_arg_gramm, user_del):
        Soup.list_arg_gramm.pop(user_del)
        return Soup.list_arg_gramm

while True:
    user_input = int(input('Посмотреть суп? [1]/ Удалить элемент? [2]/ Добавить элемент [3]/ Выход [4] ==== Выберите число из списка'))
    if user_input == 1:
        Soup.display_count(Soup.soup_count)
        Soup.show_my_soup(Soup.list_arg_gramm)
        time.sleep(1.5)
        Soup.cls()
        continue
    elif user_input == 2:
        if Soup.soup_count == 1:
            print('Удалять нечего(((')
            time.sleep(1.5)
            Soup.cls()
            continue
        elif Soup.soup_count > 1:
            user_del = (input('Введите наименование, которое Вы хотите удалить'))
            user_del = user_del.capitalize()
            Soup.del_list(Soup.list_arg_gramm, user_del)
            time.sleep(1.5)
            Soup.cls()

    elif user_input == 3:
        a = Soup.user_arg()
        b = Soup.append_list(a, Soup.list_arg_gramm)
        Soup.display_count(a)
        Soup.show_my_soup(b)
        time.sleep(1.5)
        Soup.cls()
        continue
    elif user_input == 4:
        print('Пока')
        break



