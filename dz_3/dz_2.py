# str_ = input("")
# try:
#     # float(str_)
#     if str_.find('.') != -1 and str_.count('.') == 1:
#         print('ok')
#         if str_.find( "/", 1) == True:
#             print('ok')
#     else:
#         raise ValueError
# except ValueError:
#     print('ne ok')


str_ = input("")

if str_.find('.') == True:
    print('OK')
elif str_.find('/') == True:
    print('OK')
else:
    print('NO')