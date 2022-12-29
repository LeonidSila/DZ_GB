from aiogram.utils import executor
from create_bot import dp
import main
import mat

async def on_startup(_):
    print('Бот работает')
    
main.register_handlers_main(dp)
mat.register_handlers_mat(dp)

executor.start_polling(dp, skip_updates=True, on_startup=on_startup)

