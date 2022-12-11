import random
import copy
import time
ball_user = 1000
# Сделать поле чудес . Компьютер загадывает слово. А мы его угадываем. Делаем с помощью функций. Кто хочет посложней - добавляем очки и баран.

def Question(user_Question_level):
    question = {1:'Вопрос. Что использовали в Китае для глажки белья вместо утюга?', 2: 'Вопрос. В Швеции существует налог на собак, от которого многие пытаются уклониться.\nВ налоговой инспекции в Стокгольме придумали забавный способ борьбы с неплательщиками: \nсотрудница службы Эльфрида Карлсон ходит по домам и делает это.', 3:'Вопрос. Польский ученый-математик Гуго Дионисий Штейнгауз, прославившийся также своими афоризмами, говорил: «Комплимент женщине должен быть правдивее, чем…»', 4: 'Вопрос. Человеческие способности довольно велики. Например, мы можем собственными силами разогнать воздушный поток до 150–170 км/ч. В процессе чего человек способен произвести такой воздушный поток?', 5: 'Вопрос. Как у западных и южных славян назывались селение, деревня, курень?'}
    question_user = question[user_Question_level]
    return question_user

def Answers(user_Question_level):
    answers = {1: 'сковорода', 2: 'гавкает', 3: 'правда', 4: 'чихание', 5: 'жупа'}
    answers_user = answers[user_Question_level]
    return  answers_user


def pole(user_level): # Создаем общее поле
    my_list = []
    for j in range(user_level):
        my_list.append('x')

    # for i in my_list:
    #     print(i)
    return my_list

def print_pole(my_list):
    for i in my_list:
        print(i)
    return 'ПОЛЕ'




def range_len(a): # Создаем барабан
    my_list = []
    for i in range(a):
        my_list2 = []
        for j in range(a):
            my_list2.append('|')
        my_list.append(my_list2)
    my_list[0][6] = ' '
    my_list[6][0] = ' '
    my_list[0][0] = ' '
    my_list[6][6] = ' '
    return my_list

def print_list(my_list): # Выводим игровое поле
    print('Крутится барабан')
    for i in my_list:
        print(*i)
    return 
        
def clok_1(my_list):
        
            my_list[0][3] = '+'
            my_list[1][3] = '+'
            my_list[2][3] = '+'
            my_list[3][3] = '+'
            # for i in my_list:
            
            return my_list
def clok_2(my_list):
        
            my_list[0][3] = '|'
            my_list[0][6] = '+'
            my_list[1][3] = '|'
            my_list[1][5] = '+'
            my_list[2][3] = '|'
            my_list[2][4] = '+'
            
            return my_list

def clok_3(my_list):
            my_list[0][6] = ' '
            my_list[1][5] = '|'
            my_list[2][4] = '|'
            my_list[3][4] = '+'
            my_list[3][5] = '+'
            my_list[3][6] = '+'
            
            return my_list

def clok_4(my_list):
        
            my_list[3][4] = '|'
            my_list[3][5] = '|'
            my_list[3][6] = '|'
            my_list[6][6] = '+'
            my_list[5][5] = '+'
            my_list[4][4] = '+'
            
            return my_list

def clok_5(my_list):
        
            my_list[6][6] = ' '
            my_list[5][5] = '|'
            my_list[4][4] = '|'
            my_list[6][3] = '+'
            my_list[5][3] = '+'
            my_list[4][3] = '+'
            
            return my_list

def clok_6(my_list):
        
            my_list[6][3] = '|'
            my_list[5][3] = '|'
            my_list[4][3] = '|'
            my_list[6][0] = '+'
            my_list[5][1] = '+'
            my_list[4][2] = '+'
            
            return my_list
    
def clok_7(my_list):

            my_list[6][0] = ' '
            my_list[5][1] = '|'
            my_list[4][2] = '|'
            my_list[3][2] = '+'
            my_list[3][1] = '+'
            my_list[3][0] = '+'
            
            return my_list

def clok_8(my_list):
        
            my_list[3][2] = '|'
            my_list[3][1] = '|'
            my_list[3][0] = '|'
            my_list[0][0] = '+'
            my_list[1][1] = '+'
            my_list[2][2] = '+'
            
    
            return my_list

def clok_9(my_list):
            my_list[0][0] = ' '
            my_list[1][1] = '|'
            my_list[2][2] = '|'
            my_list[0][3] = '+'
            my_list[1][3] = '+'
            my_list[2][3] = '+'
    
    
            return my_list


def clok_out(clok_1, clok_2, clok_3, clok_4, clok_5, clok_6, clok_7, clok_8, clok_9, my_list):
    a = range_len(my_list)
    random_numbers = random.randint(1, 3)
    c = random.randint(1, 9)
    for i in range(3 + random.randint(0,  random_numbers)):
        print_list(clok_1(a))
        time.sleep(0.5)
        print_list(clok_2(a))
        time.sleep(0.5)
        print_list(clok_3(a))
        time.sleep(0.5)
        print_list(clok_4(a))
        time.sleep(0.5)
        print_list(clok_5(a))
        time.sleep(0.5)
        print_list(clok_6(a))
        time.sleep(0.5)
        print_list(clok_7(a))
        time.sleep(0.5)
        print_list(clok_8(a))
        time.sleep(0.5)
        print_list(clok_9(a))
  
    return 

def ball():
    global ball_user
    a = random.randrange(100, 1000, 100)
    b = random.randrange(100, 1000, 100) * -1
    d = random.random() 
    if d == 0:
        ball_user += a
        print(f'Вы выкрутил --- {a}')
        print(f'Ваши баллы {ball_user}')
    else:
        ball_user +=b
        print(f'Вы выкрутил --- {b}')
        print(f'Ваши баллы {ball_user}')
    
    return ball_user

def rait(a, user_input):
    a = list(a)
    for i in range(len(a)):
        if a[i] == user_input:
            print(f'Правильно, Буква {user_input.upper()}')
            a[i] = ''
            print(*a)
            break
        
        if user_input not in a:
            print('НЕА')
            break

    return a
            

while True:
    print('Игра НАЧАЛАСЬ!')
    user_level = int(input('Выберите слово от 1 до 5:'))
    if user_level < 1 or user_level > 5:
        print("Число брат")
        continue
    
    print(Question(user_level))
    a = Answers(user_level)
    pole_user = pole(len(a))
    print(a)
    print((pole_user))

    while True:
        if ball_user < 0:
            print('Пройгрыш')
            break
        user_input = input('Вводим Либо слово полснотью, либо букву от от слова:>>>>')
        if user_input == int():
            print('Пишем букавки либо слово, не число')
            continue
        if a == user_input:
            print('победа')
            break
        a = list(a)
        
        for i in range(len(a)):
            if a[i] == user_input:
                print(f'Правильно, Буква {user_input.upper()}')
                a[i] = 0
                ball_user += 500
                pole_user[i] = user_input
                print((pole_user))
                print(*a)
                break
        
            if user_input not in a:
                print('НЕА')
                ball_user -= 500
                user_rool = input('Крутим барабан? д/н')
                if user_rool == 'д':
                    clok_out(clok_1, clok_2, clok_3, clok_4, clok_5, clok_6, clok_7, clok_8, clok_9, 7)
                    ball()
                    break
                else:
                    break
                
    break
        


