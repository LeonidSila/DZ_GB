from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

b1 = KeyboardButton('/Заметки')
b3 = KeyboardButton('/Парсер')

b1_parser = KeyboardButton('/Погода_сегодня')
b2_parser = KeyboardButton('/Погода_завтра')
b3_parser = KeyboardButton('/Погода_по_часам')
b4_parser = KeyboardButton('/Назад')
b1_zametka = KeyboardButton('/Создать_заново')
b2_zametka = KeyboardButton('/Прочитать_всё')
b3_zametka = KeyboardButton('/Определенный_день')

b_zametka_p = KeyboardButton('/Понедельник')
b_zametka_v = KeyboardButton('/Вторник')
b_zametka_s = KeyboardButton('/Среда')
b_zametka_h = KeyboardButton('/Четверг')
b_zametka_pi = KeyboardButton('/Пятница')
b_zametka_sb = KeyboardButton('/Суббота')
b_zametka_vs = KeyboardButton('/Воскресенье')
b_zametka_nasad = KeyboardButton('/Назад')

b_zametka_off = KeyboardButton('/Назад')

# pole1 = KeyboardButton('/1')
# pole2 = KeyboardButton('/2')
# pole3 = KeyboardButton('/3')
# pole4 = KeyboardButton('/4')
# pole5 = KeyboardButton('/5')


kb_zametka_car = ReplyKeyboardMarkup(resize_keyboard=True)
kb_parser = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client = ReplyKeyboardMarkup(resize_keyboard=True)
kb_zametka = ReplyKeyboardMarkup(resize_keyboard=True)
kb_zametka_tdy = ReplyKeyboardMarkup(resize_keyboard=True)
kb_client.add(b1).add(b3)
kb_parser.add(b1_parser).add(b2_parser).add(b3_parser).add(b4_parser)
kb_zametka.add(b1_zametka).add(b2_zametka).add(b3_zametka).add(b4_parser)
kb_zametka_tdy.add(b_zametka_p).add(b_zametka_v).add(b_zametka_s).add(b_zametka_h).add(b_zametka_pi).add(b_zametka_sb).add(b_zametka_vs).add(b_zametka_nasad)
kb_zametka_car.add(b_zametka_off)

