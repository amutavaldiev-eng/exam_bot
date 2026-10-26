from aiogram import Bot, Dispatcher,F
from aiogram.filters import Command, CommandStart, CommandObject
from aiogram.types import Message,ReplyKeyboardMarkup,KeyboardButton
from dotenv import load_dotenv 
from service import *
from connection import *
import asyncio
import os

load_dotenv()

token = os.getenv("BOT_TOKEN")
bot = Bot(token = token)
dp=Dispatcher()


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="🛠️ Catalog"),
            KeyboardButton(text="📦 My Rentals")
        ],
    ],
    resize_keyboard=True
)



@dp.message(CommandStart())
async def start(message:Message):
    await get_user_by_id(message.from_user.id)
    await message.answer(
        f"👋 Welcome, {message.from_user.full_name}!\n\n"
        "🛠️ This bot helps you rent and return equipment easily.\n"
        "📦 Check available items and manage your rentals.",
        reply_markup=main_kb
    )


@dp.message(Command("help"))
async def help(message: Message):
    await message.answer("""
==========MENU HELP❓==========

📌 Commands:
➕ /add_item  — Add equipment
🛠️ /items — Show available equipment
📥 /rent  — Rent equipment
📤 /return_item  — Return equipment
📦 /my_rentals — Show my rentals
❓ /help — Show help

⚠️Alert:

💰 Late fee: 5000 somoni per overdue day.
""")



@dp.message(Command("add_item"))
async def add_items(message: Message, command: CommandObject):
    data = command.args
    if not data:
        await message.answer("❌ Please enter an item name!\nExample: /add_item something...")
        return
    data = await add_item(data)
    if data:
        await message.answer("Item added successfully ✅")
    else:
        await message.answer("Item added failed ❌")
  