import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo
from aiogram.filters import Command

# Токен бота
API_TOKEN = '8077146960:AAG7q7j5Jf1sB1M8Uq-x1t4W4G21GM3-t_Q'

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()
router = Router()

# Обработчик команды /start
@router.message(Command("start"))
async def start_command(message: types.Message):
    # Создаем кнопку для запуска мини-приложения
    buttons = [
        [InlineKeyboardButton(
            text="🚀 Открыть мини-приложение",
            web_app=WebAppInfo(url="https://qewsob.github.io/my-telegram-webapp/")  # Укажи ссылку на веб-приложение
        )]
    ]
    keyboard = InlineKeyboardMarkup(inline_keyboard=buttons)
    await message.answer(
        "Привет! Нажми на кнопку ниже, чтобы открыть мини-приложение 🚀",
        reply_markup=keyboard
    )

# Основная функция для запуска
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
