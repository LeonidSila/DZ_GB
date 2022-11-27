user = (input())

if user[0] > user[1]:
    a = 'больше'
else:
    a = 'меньшее'
if user[1] > user[2]:
    b = 'больше'
else:
    b = 'меньше'
if user[2] > user[3]:
    c = 'больше'
else:
    c = 'меньше'
# if user[3] > user[4]:
#     d = 'больше'
# else:
#     d = 'меньше'

for i in range(len(a)):
    if a[i]<a[i-1]:
        i += 1
        f = "Yes"
    else:
        f = "No"

print(user[0],a, user[1],b, user[2],c, user[3], f) 