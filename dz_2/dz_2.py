# print ('Введите числа через запятую:') # 100, 1, 3, 5, 7, 5, 9, 4, 5, 7, 12, 15, 20
# user_input_2 = (input('Вводите число через ","===='))
# user = set(user_input_2)
# # max_1 = user.remove(max(user))
# max_2 = max(user_input_2)
# print(max_2)

N=int(input())
m_2 = 0
m_1 = 0
#    m=0 
m = int(input())
for i in range(1,N):
    i=int(input())
    
    if i > m:
        m_1 = i
    else:
        m_1 = m
    if i > m_1 or i > m and i!=m_1 and i!=m:
        m_2 = i
    else:
        m_2 = max(range(1,i))
    
    

#    for N in range(2,N+1):
#    if m<i:
#    m=i
print(m_1, m_2)