from aiogram import types, Dispatcher
from create_bot import dp, bot
from kb import kb_client, kb_parser, kb_zametka, kb_zametka_tdy, kb_zametka_car
from bs4 import BeautifulSoup as bs
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
import requests, os, copy, datetime, time, random


now = datetime.datetime.now()
computer_data = []

class FSM_zametka(StatesGroup):
    zametka = State()
    zametka2 = State()
    zametka3 = State()
    zametka4 = State()
    zametka5 = State()
    zametka6 = State()
    zametka7 = State()
   
    

async def command_start(message : types.Message):
        await bot.send_message(message.from_id, 'Матам не ругаемся, все проверяем! Начинаем GB dz 10', reply_markup=kb_client)
        await message.delete()

async def command_help(message : types.Message):
        await bot.send_message(message.from_id, 'Не знаю конечно в чем проблема, все просто тыкай кнопки', reply_markup=kb_client)
        await message.delete()
       

async def parser_dz(message : types.Message):
    await bot.send_message(message.from_id, 'Выбирай', reply_markup=kb_parser)
    
async def pogoda_tomorrow(message : types.Message):
        url_tomorrow = 'https://meteolabs.ru/погода_санкт-петербург/завтра/' 
        response = requests.get(url_tomorrow).text
        soup = bs(response, 'html.parser')
    # print(soup)
        city = soup.find('h1', class_='h1')
        weather = soup.find('p',class_="wthSBlock__commonWth")
        a = city.text
        b = weather.text
        await message.delete()
        await bot.send_message(message.from_id, a)
        await bot.send_message(message.from_id, b)
async def pogoda_today(message : types.Message):
        url_today = 'https://meteolabs.ru/погода_санкт-петербург/сегодня/'
        response = requests.get(url_today).text
        soup = bs(response, 'html.parser')
    # print(soup)
        city = soup.find('h1', class_='h1')
        weather = soup.find('p',class_="wthSBlock__commonWth")
        a = city.text
        b = weather.text
        await message.delete()
        await bot.send_message(message.from_id, a)
        await bot.send_message(message.from_id, b)

async def pogoda_today_hr(message : types.Message):
        url_today = 'https://meteolabs.ru/погода_санкт-петербург/сегодня/'
        list_1 = {}
        list_2 = []
        response_1 = requests.get(url_today).text
        soup = bs(response_1, 'html.parser')
        for x in soup.find_all('p', class_='wthSBlock__commonTime'):
            if x == 'День':
                continue
            for a in soup.find_all('p', class_="wthSBlock__commonWth"):
                list_1[x.text] = a.text
        list_1['  13:00    '] = list_1.pop('  День   13:00  ')
        list_1['  03:00    '] = list_1.pop('  Ночь   03:00  ')
        await message.delete()
        for k, v in list_1.items():
            await bot.send_message(message.from_id, (k, v))
async def nazad(message : types.Message):
    await message.delete()
    await bot.send_message(message.from_id, 'Возвращаю', reply_markup=kb_client)

async def zametka(message : types.Message):
    await message.delete()
    await bot.send_message(message.from_id, 'Вот', reply_markup=kb_zametka)

async def opredelenni_day(message : types.Message):
    await message.delete()
    await bot.send_message(message.from_id, 'Определенный день', reply_markup=kb_zametka_tdy)

async def nazad_v_zametka(message : types.Message):
    await message.delete()
    await bot.send_message(message.from_id, 'Возвращаю', reply_markup=kb_zametka)

async def create_fail(message : types.Message):
    await message.delete()
    my_file_1 = open("Понедельник.txt", "w+")
    my_file_2 = open("Вторник.txt", "w+")
    my_file_3 = open("Среда.txt", "w+")
    my_file_4 = open("Четверг.txt", "w+")
    my_file_5 = open("Пятница.txt", "w+")
    my_file_6 = open("Суббота.txt", "w+")
    my_file_7 = open("Воскресенье.txt", "w+")
    return my_file_1, my_file_2, my_file_3, my_file_4, my_file_5, my_file_6, my_file_7

async def read_all_my_file(message : types.Message):
    await message.delete()
    with open('Понедельник.txt', 'r', encoding="utf-8") as f:
        await bot.send_message(message.from_id, ('Понедельник', f.read()))
        # print ('Понедельник', f.read(), sep='\n')
    with open('Вторник.txt', 'r', encoding="utf-8") as f:
        await bot.send_message(message.from_id, ('Вторник', f.read()))
        # print ('Вторник', f.read(), sep='\n')
    with open('Среда.txt', 'r', encoding="utf-8") as f:
        await bot.send_message(message.from_id, ('Среда', f.read()))
        # print ('Среда', f.read(), sep='\n')
    with open('Четверг.txt', 'r', encoding="utf-8") as f:
        await bot.send_message(message.from_id, ('Четверг', f.read()))
        # print ('Четверг', f.read(), sep='\n')
    with open('Пятница.txt', 'r', encoding="utf-8") as f:
        await bot.send_message(message.from_id, ('Пятница', f.read()))
        # print ('Пятница', f.read(), sep='\n')
    with open('Суббота.txt', 'r', encoding="utf-8") as f:
        await bot.send_message(message.from_id, ('Суббота', f.read()))
        # print ('Суббота', f.read(), sep='\n')
    with open('Воскресенье.txt', 'r', encoding="utf-8") as f:
        await bot.send_message(message.from_id, ('Воскресенье', f.read()))
        # print ('Воскресенье', f.read(), sep='\n')
# async def cm_start(message : types.Message):
#     await FSM_zametka.zametka.set()
    

async def monday(message : types.Message, state : FSMContext):
    await FSM_zametka.zametka.set()
    await bot.send_message(message.from_id, 'Нажмите на кномпу, Назад, чтобы закончить', reply_markup=kb_zametka_car)
    
async def monday_write(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
            data['zameta'] = message.text
            a = str(data)
            with open('Понедельник.txt', 'w', encoding="utf-8") as f:
                f.write(a[61:])
            await state.finish()
async def cm_off(message : types.Message, state : FSMContext):
        await bot.send_message(message.from_id, 'Пора все', reply_markup=kb_zametka_tdy)
       
async def opredelenni_day(message : types.Message, state = None):
    await message.delete()
    await bot.send_message(message.from_id, 'Определенный день', reply_markup=kb_zametka_tdy)


async def tuesday(message : types.Message, state : FSMContext):
    await FSM_zametka.zametka2.set()
    await bot.send_message(message.from_id, 'Нажмите на кномпу, Назад, чтобы закончить', reply_markup=kb_zametka_car)
    
async def tuesday_write(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
            data['zameta2'] = message.text
            a = str(data)
            with open('Вторник.txt', 'w', encoding="utf-8") as f:
                f.write(a[61:])
            await state.finish()

async def wednesday(message : types.Message, state : FSMContext):
    await FSM_zametka.zametka3.set()
    await bot.send_message(message.from_id, 'Нажмите на кномпу, Назад, чтобы закончить', reply_markup=kb_zametka_car)
    
async def wednesday_write(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
            data['zameta3'] = message.text
            a = str(data)
            with open('Среда.txt', 'w', encoding="utf-8") as f:
                f.write(a[61:])
            await state.finish()

async def thursday(message : types.Message, state : FSMContext):
    await FSM_zametka.zametka4.set()
    await bot.send_message(message.from_id, 'Нажмите на кномпу, Назад, чтобы закончить', reply_markup=kb_zametka_car)
    
async def thursday_write(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
            data['zameta4'] = message.text
            a = str(data)
            with open('Четверг.txt', 'w', encoding="utf-8") as f:
                f.write(a[61:])
            await state.finish()

async def friday(message : types.Message, state : FSMContext):
    await FSM_zametka.zametka5.set()
    await bot.send_message(message.from_id, 'Нажмите на кномпу, Назад, чтобы закончить', reply_markup=kb_zametka_car)
    
async def friday_write(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
            data['zameta5'] = message.text
            a = str(data)
            with open('Пятница.txt', 'w', encoding="utf-8") as f:
                f.write(a[61:])
            await state.finish()

async def saturday(message : types.Message, state : FSMContext):
    await FSM_zametka.zametka6.set()
    await bot.send_message(message.from_id, 'Нажмите на кномпу, Назад, чтобы закончить', reply_markup=kb_zametka_car)
    
async def saturday_write(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
            data['zameta6'] = message.text
            a = str(data)
            with open('Суббота.txt', 'w', encoding="utf-8") as f:
                f.write(a[61:])
            await state.finish()

async def sunday(message : types.Message, state : FSMContext):
    await FSM_zametka.zametka7.set()
    await bot.send_message(message.from_id, 'Нажмите на кномпу, Назад, чтобы закончить', reply_markup=kb_zametka_car)
    
async def sunday_write(message : types.Message, state : FSMContext):
    async with state.proxy() as data:
            data['zameta7'] = message.text
            a = str(data)
            with open('Воскресенье.txt', 'w', encoding="utf-8") as f:
                f.write(a[61:])
            await state.finish()


    

def register_handlers_main (dp : Dispatcher):
    dp.register_message_handler(parser_dz, commands=['Парсер'])
    dp.register_message_handler(command_start, commands=['start'])
    dp.register_message_handler(command_help, commands=['help'])
    dp.register_message_handler(pogoda_tomorrow, commands=['Погода_завтра'])
    dp.register_message_handler(pogoda_today, commands=['Погода_сегодня'])
    dp.register_message_handler(pogoda_today_hr, commands=['Погода_по_часам'])
    dp.register_message_handler(nazad, commands=['Назад'])
    dp.register_message_handler(read_all_my_file, commands=['Прочитать_всё'])
    dp.register_message_handler(create_fail, commands=['Создать_заново'])
    dp.register_message_handler(zametka, commands=['Заметки'])
    dp.register_message_handler(opredelenni_day, commands=['Определенный_день'])
    dp.register_message_handler(nazad_v_zametka, commands=['Назад'])
    dp.register_message_handler(monday, commands=['Понедельник'], state=None)
    dp.register_message_handler(monday_write, state=FSM_zametka.zametka)
    dp.register_message_handler(cm_off, commands=['Назад'], state=FSMContext)
    dp.register_message_handler(tuesday, commands=['Вторник'], state=None)
    dp.register_message_handler(tuesday_write, state=FSM_zametka.zametka2)
    dp.register_message_handler(wednesday, commands=['Среда'], state=None)
    dp.register_message_handler(wednesday_write, state=FSM_zametka.zametka3)
    dp.register_message_handler(thursday, commands=['Четверг'], state=None)
    dp.register_message_handler(thursday_write, state=FSM_zametka.zametka4)
    dp.register_message_handler(friday, commands=['Пятница'], state=None)
    dp.register_message_handler(friday_write, state=FSM_zametka.zametka5)
    dp.register_message_handler(saturday, commands=['Суббота'], state=None)
    dp.register_message_handler(saturday_write, state=FSM_zametka.zametka6)
    dp.register_message_handler(sunday, commands=['Воскресенье'], state=None)
    dp.register_message_handler(sunday_write, state=FSM_zametka.zametka7)
    

    
    
    