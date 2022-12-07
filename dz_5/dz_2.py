import random
import copy

my_list = []

for i in range(1, 4):
    my_list2 = []
    for j in range(1, 4):
        my_list2.append('*')
    my_list.append(my_list2)

computer_list = copy.deepcopy(my_list)
print(my_list)
print(computer_list)
for i in my_list:
    print(i)
print('Начинаем игру! В вы ходите первый! На место * Надо поставит X или 0:')

while True:
    user_1 = int(input('Выбираем столик: 1, 2, 3:'))-1
    user_2 = int(input('Выбираем позицияю в стоблике: 1, 2, 3:'))-1
    computer_list[user_1][user_2] = 'x'
    for i in computer_list:
        print(i)
    if user_1 != 1 and user_2 != 1 and computer_list[user_1][user_2] != 'x':
        computer_1 = 1
        computer_2 = 1
        computer_list[computer_1][computer_2] = '0'
        for i in computer_list:
            print(i)
        continue
    else:
        while True:
            n = 0
            сhoice_1 = random.randrange(0,3)
            choice_2 = random.randrange(0,3)
            print(choice_2, сhoice_1)
            if computer_list[сhoice_1][choice_2] == 'x':
                n += 1
                if n >10:
                    break 
                else:
                    continue
            
            else:
                computer_list[сhoice_1][choice_2] = '0'
                for i in computer_list:
                    print(i)
                break
    
    if computer_list[0][:] == 'x' or computer_list [1][:] == 'x' or computer_list [2][:] == 'x' or computer_list[0][0] and computer_list[1][1] and computer_list[2][2] == 'x' or computer_list[0][2] and computer_list[1][1] and computer_list[2][0] == 'x' : 
        print('Win')
        break
    else:
        continue
    






