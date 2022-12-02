
from random import randint
import random

a = int(input())
b = list(input()) 
numbers = []
for i in range(20):
    numbers.append(randint(10, 70))

mas =[]
for i in range(a): 
    mass = random.choice(numbers)

    mas.append([mass] * a)
print(mas) 



for i in mas: 
    for i2 in b: 
        print(mas, end=' ') 
    print()

for i in range(a):
    mas_out = (sum(mas[0][:] + mas[1][:] + mas[2][:]))/len(mas)
    

print(mas_out)

