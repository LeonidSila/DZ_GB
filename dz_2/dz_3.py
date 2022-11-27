uzer = int(input())

rub_25 = uzer // 25
rub_ostatok_1 = uzer - (rub_25 * 25)
rub_10 = rub_ostatok_1 // 10
rub_ostatok_2 = rub_ostatok_1 - (rub_10 * 10)
rub_3 = rub_ostatok_2 // 3
rub_ostatok_3 = rub_ostatok_2 - (rub_3*3)
rub_1 = rub_ostatok_3 // 1

print('25 купюра=',rub_25, '\n10 купюра=',rub_10, '\n3 купюра=',rub_3, '\n-1 купюра=',rub_1)