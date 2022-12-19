# 2)Нужно напистаь программу
# В ней используем классы - имя студента name, номер группы group и список полученных оценок progress.
# В самой программе вводим список всех студентов.
# В программе нужно вывести список студентов, отсортированный по имени, А так же студентов, у которых низкие оценки
import os
import time

class Name:
    # teacher_name = 'Анна', 'Ольгая', 'Ира'
    # students_name = 'Александра', 'Алексей', 'Артем', 'Лидия', 'Ольга', 'Артем', 'Марта', 'Юлия', 'София', 'Екатерина', 'Андрей', 'София', 'Николай', 'Никита', 'Марк', 'Диана', 'Ева', 'София', 'Егор'

    students_name = 'Александра', 'Алексей', 'Артем', 'Лидия', 'Ольга', 'Антон'
    def name_students(user_name_students):
        Name.students_name = Name.students_name.append(user_students)
        # Name.students_name.sort
        return Name.students_name
    def name_teacher(user_name_teacher):
        Name.teacher_name = Name.teacher_name(user_name_teacher)
        return Name.teacher_name


class Group:
    # teacher_group = '1', '2', '3'
    students_group = '1', '2', '3'
    # def group_teacher(user_group_teacher):
    #     Group.teacher_group = Group.teacher_group.append(user_group_teacher)
    #     return Group.teacher_group
    def group_students(user_group_students):
        Group.students_group = Group.students_group.append(user_group_students)
        return Group.group_students

class Progress:
    students_progress = '2', '3', '4', '5'
    def progress_students(user_progress_studenst):
        Progress.students_progress = Progress.students_progress.append(user_progress_studenst)
        return Progress.students_progress

'''
Тут я пытался создать доболенение новых переменных, для создания новых груп, но пока мало знаний!
'''

# def creating_group(group_students, user_input_group, user_input_teacher):
#         globals()['group_' + str(user_input_group)] = {}
    
# def creating_tuple(user_group, user_teacher, group):
#         globals()['print_ '+ str(user_group)] = (user_teacher, group)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def creating_students():
    group_1 = {Name.students_name[0]: [Progress.students_progress[0], Progress.students_progress[1], Progress.students_progress[1]], Name.students_name[2]: [Progress.students_progress[3], Progress.students_progress[3], Progress.students_progress[3]] }
    group_2 = {Name.students_name[1]: [Progress.students_progress[3], Progress.students_progress[0], Progress.students_progress[0]], Name.students_name[5]: [Progress.students_progress[2], Progress.students_progress[2], Progress.students_progress[0]] }
    group_3 = {Name.students_name[4]: [Progress.students_progress[1], Progress.students_progress[1], Progress.students_progress[1]], Name.students_name[3]: [Progress.students_progress[2], Progress.students_progress[3], Progress.students_progress[1]] }
    return group_1, group_2, group_3

def creating_students_group(group, user_students, user_progress):
    group[user_students] = user_progress
    return group

def sorted_group(group_1):
    sorted_group_1 = sorted(group_1.items(), key=lambda x:x[0])
    group_1 = dict(sorted_group_1)
    return group_1
    
def sorted_students(group_1):
    min_each = {key: min(value) for key, value in group_1.items()}
    return min_each  


def print_creating_table(tables_1):
    for x, y in tables_1.items():
        print(x, *y, sep='|')
        print()

while True:
    a = creating_students()
    print('-'*30)
    print('Вывести список студентов? == 1') 
    print('Отсортированный по имени? == 2')
    print('Отсортированный по успеваемости? == 3')
    print('Добавить ученика == 4')
    user_q = int(input('Введите число:'))
    if user_q == 4:
        time.sleep(0.5)
        cls()
        user_students = input('Введите Имя ученика:::')
        user_progress = input('Введите оценки:::')
        user_group = int(input('Введите группу в которую он пойдет!:::'))
        if user_group == 1:
            creating_students_group(a[0], user_students, user_progress)
            time.sleep(0.5)
            cls()
            print(a[0])
            continue
        elif user_group == 2:
            creating_students_group(a[1], user_students, user_progress)
            time.sleep(0.5)
            cls()
            print(a[1])
            continue
        elif user_group == 3:
            creating_students_group(a[1], user_students, user_progress)
            time.sleep(0.5)
            cls()
            print(a[2])
            continue
        else:
            print('Нет таких групп')
            continue
    elif user_q == 2:
        out = {}
        out = out | a[0] | a[1] | a[2]
        out = sorted_group(out)
        time.sleep(0.5)
        cls()
        c = print_creating_table(out)
        continue
    elif user_q == 1:
        out = {}
        out = out | a[0] | a[1] | a[2]
        time.sleep(0.5)
        cls()
        print_creating_table(out)
        continue
    elif user_q == 3:
        out = {}
        out = out | a[0] | a[1] | a[2]
        time.sleep(0.5)
        cls()
        c = sorted_students(out)
        c = print_creating_table(c)
        continue







