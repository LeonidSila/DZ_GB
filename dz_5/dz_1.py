import random
import copy
user_len = int(input('Размер поля: x на X. Введите X-1Раз>>>>>'))
my_list = []

for i in range(user_len):
    my_list2 = []
    for j in range(user_len):
        my_list2.append(0)
    my_list.append(my_list2)

    list_cumputer = random.randint(0, user_len-1)
    list_cumputer_2 = random.randint(0, user_len-1)
user_list = copy.deepcopy(my_list)
my_list[list_cumputer][list_cumputer_2] = 1

    
# print(cumputer)   
# print(list_cumputer)
# print(list_cumputer_2)
# print(my_list)
# print(user_list)
# print(type(list_cumputer))
for i in my_list:
    print(i)
print("###########################################")
for i in user_list:
    print(i)


while True:
    
    user = int(input(f'Введите координатe по X от 1 до {user_len}. Типа X Стобец=>>>>>>'))
    user_2 = int(input(f'Введите координатe по y от 1 до {user_len}. Типа Y Позиция в стодбце=>>>>>>'))
    if user-1 != list_cumputer or user_2-1 != list_cumputer_2:
        print('Мимо, давай заново')
        continue
    if user-1 and user_2-1 == list_cumputer and list_cumputer_2:
        print("ПоБЕДА")
        break
        
