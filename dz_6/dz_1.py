import random
import copy


ship_1 = (1)
ship_2 = (1,2)
ship_3 = (1,2,3)


def range_len(a): # Создаем общее поле
    my_list = []
    for i in range(a):
        my_list2 = []
        for j in range(a):
            my_list2.append(0)
        my_list.append(my_list2)
    return my_list

def copy_my_list(my_list): # Копируем общее поле
    user_list = copy.deepcopy(my_list)
    return user_list


def computer_ship_1(user_len): # Создаем 1 Корабль
    list_cumputer_ship_1 = random.randint(0, user_len-1) # Возможно нужно -1 или +1
    list_cumputer_2_ship_1 = random.randint(0, user_len-1)
        
    return list_cumputer_ship_1, list_cumputer_2_ship_1
        

def computer_ship_2(user_len, list_cumputer_ship_1, list_cumputer_2_ship_1): # Создаем 2 корабль
    while True:
        list_cumputer_ship_2_1 = random.randint(0, user_len-1)
        list_cumputer_2_ship_2_1 = random.randint(0, user_len-1)
        if list_cumputer_ship_2_1 == list_cumputer_ship_1 and list_cumputer_2_ship_2_1 == list_cumputer_2_ship_1 and list_cumputer_ship_2_1 == 4:
            continue
        else:
            list_cumputer_ship_2_2 = list_cumputer_ship_2_1 + 1
            list_cumputer_2_ship_2_2 = list_cumputer_2_ship_2_1
        if list_cumputer_2_ship_2_2 == list_cumputer_ship_1 and list_cumputer_ship_2_2 == list_cumputer_2_ship_1 and list_cumputer_ship_2_1 == 4:
            continue
            if list_cumputer_ship_2_2 >=5:
                # print(list_cumputer_ship_2_2, 'Вы цикли')
                list_cumputer_ship_2_2 = list_cumputer_ship_2_2 - 2
                    # return list_cumputer_ship_2_1, list_cumputer_2_ship_2_1, list_cumputer_ship_2_2, list_cumputer_2_ship_2_2
                break
            else:
                break
        else:
            break
    return list_cumputer_ship_2_1, list_cumputer_2_ship_2_1, list_cumputer_ship_2_2, list_cumputer_2_ship_2_2
# Импортируем корабли в общий список
def install_ship(a, list_cumputer_ship_1, list_cumputer_2_ship_1, list_cumputer_ship_2_1, list_cumputer_2_ship_2_1, list_cumputer_ship_2_2, list_cumputer_2_ship_2_2):
    # print(type(a))
    if list_cumputer_ship_2_2 == 5:
        list_cumputer_ship_2_2 = list_cumputer_ship_2_2 - 2
    a[list_cumputer_ship_1][list_cumputer_2_ship_1] = 1
    a[list_cumputer_ship_2_1][list_cumputer_2_ship_2_1] = 2
    # print(list_cumputer_ship_2_2)
    a[list_cumputer_ship_2_2][list_cumputer_2_ship_2_2] = 3
    return a


def print_list(my_list, user_list): # Выводим игровое поле
    print('Таблица игры с расположение короблей')
    for i in my_list:
        print(i)
    print("###########################################")
    print('Таблица игры с расположением попаданий')
    for i in user_list:
        print(i)
    
    return '-----------------------------------------'

def user_play(user_list, user, user_2):
    user_list[user][user_2] = 'x'
    return user_list


while True: # Проверка на внимательного читателя
    user_len = int(input('Размер поля: от 5 до 10. Введите X-1Раз>>>>>'))
    if user_len < 5 or user_len > 10:
        print("Попробуй заново, что-то ты делаешь не так")
        continue
    else:
        print('Игра началась')
        print_list(range_len(user_len), copy_my_list(range_len(user_len)))
        a = range_len(user_len)
        b = copy_my_list(range_len(user_len))
        ships_1 = computer_ship_1(user_len)
        ships_2 = computer_ship_2(user_len, ships_1[0], ships_1[1])
        a = install_ship(a, ships_1[0], ships_1[1],ships_2[0],ships_2[1],ships_2[2],ships_2[3])
        win = 0
        count = 1
        
        print(type(ships_1))
            
        while True:
            for i in range(len(a)):
                if a[i].count('х'):
                    a[i].index('х')
                    a[i][a[i].index('х')] = 'x'
                    
                    win += count
            print(win)
            if win >= 3:
                print('Победа')
                again = input('Хотите заново?: где д это ДА, НЕТ это н::::>>>>> д/n:')
                if again == 'д':
                    break
                else:
                    break
            print('Сделай ход')
            user = int(input(f'Введите координатe по X от 1 до {user_len}. Типа X Стобец=>>>>>>'))
            
            if user < 0 or user > user_len:
                print('Что-то то ты даешь опять не так')
                continue
            user = user -1

            user_2 = int(input(f'Введите координатe по y от 1 до {user_len}. Типа Y Позиция в стодбце=>>>>>>')) 
            
            if user_2 < 0 or user_2 > user_len:
                print('Читай внимательнее')
                continue
            user_2 = user_2 -1
        
            if user == ships_1[0] and user_2 == ships_1[1]: #or user == ships_1[1] and user_2 == ships_1[0]:
                print('Поподание!')
                a[user][user_2] = 'х'
                b[user][user_2] = 'х'
                print_list(a, b)
                continue
            elif user == ships_2[0] and user_2 == ships_2[1]:# or user == ships_2[1] and user_2 == ships_2[0]:
                print('Поподание')
                a[user][user_2] = 'х'
                b[user][user_2] = 'х'
                print_list(a, b)
                continue
            elif user == ships_2[2] and user_2 == ships_2[3]:# or user == ships_2[3] and user_2 == ships_2[2]:
                print('Поподание')
                a[user][user_2] = 'х'
                b[user][user_2] = 'х'
                print_list(a, b)
                continue
            else:
                print('Мимо')
                b[user][user_2] = 'y'
                print_list(a, b)
                continue

    if again == 'д':
        continue
    else:
        print('Перезапусти!')
        break

            

    
    