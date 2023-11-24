from pyrogram import Client, filters
from pyrogram.types import ReplyKeyboardMarkup
from config import api_hash, api_id, bot_token
from functions import *
user = Client("my_account")
bot = Client("my_bot",api_id=api_id,api_hash=api_hash,bot_token=bot_token )


# variables
is_new_category = False
new_category = {
    "name": "",
    "message": "",
    "interval": 0
}

delete_category_name = ""
is_delete_category = False

# Sending only id to me and deleting the message (/id)
@user.on_message(filters.regex("/id") & filters.me)
async def send_id(client, message):
    await client.delete_messages(message.chat.id, message.id)
    await client.send_message("me", "Name: " + message.chat.title + "\n ID: ```" +  str(message.chat.id) + "```")
    await bot.send_message(1292787687, "Name: " + message.chat.title + "\n ID: ```" +  str(message.chat.id) + "```")






# start bot
@bot.on_message(filters.regex("/start") & filters.private)
async def start(_, message):
    global is_new_category
    is_new_category = True
    await bot.send_message(message.chat.id, "Привет, Введите название новой категорию" ,reply_markup=ReplyKeyboardMarkup([["Отмена"]], resize_keyboard=True))




@bot.on_message(filters.text & filters.private)
async def add_group(_, message):
        global new_category , delete_category_name , is_delete_category , is_new_category
        # create new category
        if is_new_category:
            message_before = await bot.get_messages(message.chat.id, message.id-1)
            if message_before.text == "Выберите действие":
                if message.text == "Добавить категорию":
                    await bot.send_message(message.chat.id, "Введите название новой категорию" ,reply_markup=ReplyKeyboardMarkup([["Отмена"]], resize_keyboard=True))
                elif message.text == "Удалить категорию":
                    await bot.send_message(message.chat.id, "Выберите категорию для удаления", reply_markup=ReplyKeyboardMarkup([["Отмена"]], resize_keyboard=True))
            elif message_before.text == "Привет, Введите название новой категорию" or message_before.text == "Введите название новой категорию":
                new_category["name"] = message.text
                await bot.send_message(message.chat.id, "Введите сообщение для рассылки" ,reply_markup=ReplyKeyboardMarkup([["Отмена"]], resize_keyboard=True))
            elif message_before.text == "Введите сообщение для рассылки":
                new_category["message"] = message.text
                await bot.send_message(message.chat.id, "Введите интервал рассылки в минутах" ,reply_markup=ReplyKeyboardMarkup([["Отмена"]], resize_keyboard=True))
            elif message_before.text == "Введите интервал рассылки в минутах":
                new_category["interval"] = message.text
                create_category(new_category["name"], new_category["message"], new_category["interval"])
                await bot.send_message(message.chat.id, "Категория успешно создана:" + "\nНазвание: " + new_category["name"] + "\nСообщение: " + new_category["message"] + "\nИнтервал: " + new_category["interval"] + " минут", reply_markup=ReplyKeyboardMarkup([["Список команд"]], resize_keyboard=True))
            elif message.text == "Отмена":
                new_category = {
                    "name": "",
                    "message": "",
                    "interval": 0
                }
                await bot.send_message(message.chat.id, "Отменено")
        
        #delete category
        if message.text == "Удалить категорию":
            is_delete_category = True
            categories = get_categories()
            # list of categories from tuple
            categories = [category[0] for category in categories]
            await bot.send_message(message.chat.id, "Выберите категорию для удаления", reply_markup=ReplyKeyboardMarkup([categories,["Отмена"]], resize_keyboard=True))   
        elif is_delete_category:
            delete_category_name = message.text
            await bot.send_message(message.chat.id, "Вы уверены что хотите удалить категорию: " + delete_category_name, reply_markup=ReplyKeyboardMarkup([["Да", "Нет"]], resize_keyboard=True))
            if message.text == "Да":
                delete_category(delete_category_name)
                await bot.send_message(message.chat.id, "Категория успешно удалена", reply_markup=ReplyKeyboardMarkup([["Список команд"]], resize_keyboard=True))
            elif message.text == "Нет":
                is_delete_category = False
                await bot.send_message(message.chat.id, "Отменено", reply_markup=ReplyKeyboardMarkup([["Список команд"]], resize_keyboard=True))

        if message.text == "Список команд":
                    await bot.send_message(message.chat.id, "Выберите действие", reply_markup=ReplyKeyboardMarkup([["Список категорий","Добавить категорию", "Удалить категорию"]], resize_keyboard=True))
                

user.start()
bot.run()


