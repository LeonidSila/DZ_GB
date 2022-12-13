import copy
import datetime
import time
import os  


now = datetime.datetime.now()
computer_data = []
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
    
def create_fail():
    my_file_1 = open("Понедельник.txt", "w+")
    my_file_2 = open("Вторник.txt", "w+")
    my_file_3 = open("Среда.txt", "w+")
    my_file_4 = open("Четверг.txt", "w+")
    my_file_5 = open("Пятница.txt", "w+")
    my_file_6 = open("Суббота.txt", "w+")
    my_file_7 = open("Воскресенье.txt", "w+")
    return my_file_1, my_file_2, my_file_3, my_file_4, my_file_5, my_file_6, my_file_7

def read_all_my_file():
    with open('Понедельник.txt', 'r', encoding="utf-8") as f:
        print ('Понедельник', f.read(), sep='\n')
    with open('Вторник.txt', 'r', encoding="utf-8") as f:
        print ('Вторник', f.read(), sep='\n')
    with open('Среда.txt', 'r', encoding="utf-8") as f:
        print ('Среда', f.read(), sep='\n')
    with open('Четверг.txt', 'r', encoding="utf-8") as f:
        print ('Четверг', f.read(), sep='\n')
    with open('Пятница.txt', 'r', encoding="utf-8") as f:
        print ('Пятница', f.read(), sep='\n')
    with open('Суббота.txt', 'r', encoding="utf-8") as f:
        print ('Суббота', f.read(), sep='\n')
    with open('Воскресенье.txt', 'r', encoding="utf-8") as f:
        print ('Воскресенье', f.read(), sep='\n')
        time.sleep(4)
        cls()
        user_out = input('Введите ок'.lower())
        if user_out == 'ок':
            cls()
            return
        else:
            print('Говорю ОК!!')
            return

def write_my_file(user_day, user_write):
    with open(user_day, 'w', encoding="utf-8") as f:
        f.write(user_write)
    return user_day

def read_my_file(user_day):
    with open( user_day, 'r', encoding="utf-8") as f:
        return print (f.read())

def reminder_data(user_day, user_data):
    global computer_data
    global now
    print ('Сегодня->',now.strftime("%d-%m-%Y-%H:%M"))
    computer_data = copy.deepcopy(user_data)
    computer_data.append(user_day)
    return computer_data

def reminder():
    global computer_data

    with open(computer_data[1], 'r', encoding="utf-8") as f:
        return print (f.read())
    
    

def choice(user_choice):
    user_choice = user_choice.lower()
    if user_choice == 'напоминание':
        user_day = str(input()+'.txt')
        user_data = input('Введите дату согласно Форме. Формат d-m-Y H:M')
        return reminder_data(user_day, user_data)
    elif user_choice == 'просмотр':
        user_choice_what = int(input('прочесть все?(1), Прочесть определенный день!(2). Выберите 1 или 2:'))
        cls()
        if user_choice_what == 1:
            return read_all_my_file()
        elif user_choice_what == 2:
            user_data = input('Введите дату согласно Форме. Формат d-m-Y H:M')
            return read_my_file(user_day)
        else:
            return print('Проверьте написание!')
    elif user_choice == 'внести изминения':
        user_day = str(input('Введите день недели')+'.txt')
        user_write = input('Вводите текст')
        return write_my_file(user_day, user_write)
    else:
        return print('Что то пишите Вы не так')


while True:
    user_local = input('Первый запуск? д/н')
    cls()
    if user_local == 'д':
        create_fail()
    while True:
        if computer_data == now.strftime('%d-%m-%Y-%H:%M'):
            reminder()
            print('Напоминаем, ')
        user_choice = input('Напишите то, что будет указанно\nЧего вы хотите?\nНапоминание\nПросмотр\nВнести изминения\n')
        cls()
        choice(user_choice)
        continue
    
