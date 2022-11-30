# user_input = input()
# n = 0

# for i in len(user_input):
#     if user_input[::-1].find('o') == True:
#         n = 1
#         if n == 1:
#             if user_input.find('o') == True:
#                 n += 1
#             else:
#                 n = 1
#     else:
#         n = 1

# if n == 1:
#     print('Тольк одна О')
# elif n == 0:
#     print('Нету О')

# if n == 2:


# user_input = input()

s = input()
count = len(s) - len(s.replace('o', ''))
if count == 0:
    pass
elif count == 1:
    print(s.index('o'))
else: # count > 1
    print(s[ :s.index('o')],'Первая О\n',s[s.index('o') :s.rindex('o')],'\nПоследня О', s[s.rindex('o')+1: ])