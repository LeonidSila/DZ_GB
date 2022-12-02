from random import randint



def sort_leonid(numbers_sort):
    for i in range(len(numbers)):
        index = 1
        for j in range(i + 1, len(numbers)):
            if numbers[j] < numbers[index]:
                index = j
        numbers_sort[i], numbers_sort[index] = numbers_sort[index], numbers_sort[i]



numbers = []
for i in range(30):
    numbers.append(randint(10, 70))
a = numbers

print('Было',len(numbers), numbers,sep='\n')
numbers.sort()
print('Стало', numbers)
sort_leonid(a)
print(a)
