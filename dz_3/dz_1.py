table = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
 
 
def number_16(n):
    if (n <= 0):
        return ''
    exit_number = n % 16
    return number_16(n//16) + table[exit_number]

number = int(input())
print("Перевод в 16", number, number_16(number))

