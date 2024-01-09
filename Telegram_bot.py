from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from telegram.constants import DiceEmoji
import pymongo
import os
from dotenv import load_dotenv
import re
load_dotenv()

TOKEN=os.getenv('TOKEN')

try:
    client = pymongo.MongoClient('mongodb+srv://onlyplayxerath:iEEzRNyrBjaPPfTt@cluster0.00l13mt.mongodb.net/?retryWrites=true&w=majority')
    db = client["training-python"]
    collection = db['users']
    # ví dụ
    # user = {
    #     "name": "DuckY",
    #     "age": 30,
    # }
    # result = collection.insert_one(user).inserted_id
    # print(f"New user added with id: {result}")
    print("Connected to mongo!")
except Exception as e:
    print(e)

def write_to_file(text: str):
    with open("test.txt", 'a') as f:
        print(text, file = f)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    write_to_file(f"{update.effective_user.first_name} : {update.message.text}")
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    write_to_file(f"{update.effective_user.first_name} : {update.message.text}")
    await update.message.reply_dice(emoji=DiceEmoji.DICE)
    
async def add(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    write_to_file(f"{update.effective_user.first_name} : {update.message.text}")
    text = update.message.text[4:]
    word_list = text.split()
    name = word_list[0]
    age = word_list[1]
    new_user = {
        'name': name,
        'age': age,
    }
    await update.message.reply_text(f"New user added with id: {collection.insert_one(new_user).inserted_id}", reply_to_message_id=update.message.id, protect_content=True)

# chỉ tìm 1 người
# def search_name_with_keyboard(keyword):
#     result = collection.find_one({'name': keyword})
#     return result

# async def message_handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
#     text = update.message.text
#     await update.message.reply_text(f"{search_name_with_keyboard(text)}")

def search_name_with_keyboard(keyword):
    # chỉ tìm được đúng theo keyword
    # result = collection.find({'name': keyword})
    
    # tìm được miễn là chứa keyword (hoa hay thường cũng được)
    regex_pattern = re.compile(f'.*{re.escape(keyword)}.*', re.IGNORECASE)  
    result = collection.find({'name': {'$regex': regex_pattern}})
    return list(result)

async def message_handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    datas = search_name_with_keyboard(text)
    result = ""
    for data in datas:
        # cách 1
        # result += f"{data} \n"
        
        # cách 2
        result += data['name'] + " - " + str(data['age']) + "\n"
    await update.message.reply_text(f"{result}" if result != "" else "This user is not available!")

import requests
ACCESS_KEY = "UbqUvxTSI_Gy8ujVb30UDzOzPWChAPEXuSetKNZV7RU"
API_ADDRESS_RANDOM = f'https://api.unsplash.com/photos/random?client_id={ACCESS_KEY}'

async def random_image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response = requests.get(API_ADDRESS_RANDOM)
    if response.status_code == 200:
        image_url = response.json().get('urls', {}).get('regular')
        await update.message.reply_photo(photo = image_url, caption = "Random image from Unsplash")
    else:
         await update.message.reply_text("Somethings went wrong!")

API_ADDRESS_SEARCH = f'https://api.unsplash.com/search/photos?client_id={ACCESS_KEY}&query='
       
async def search_image(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    response = requests.get(API_ADDRESS_SEARCH)
    keyword = update.message.text[13:]
    print(keyword)
    if not keyword:
        await update.message.reply_text("Please enter a keyword!")
    else:
        response = requests.get(API_ADDRESS_SEARCH + keyword)
        if response.status_code == 200:
            search_results = response.json().get('results')[:4]
            for photo_info in search_results:
                image_url = photo_info.get('urls', {}).get('regular')
                await update.message.reply_photo(photo = image_url, caption = "Random image from Unsplash")
        else:
            await update.message.reply_text("Please enter a keyowrd!")
        
app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("dice", dice))
app.add_handler(CommandHandler("add", add))
app.add_handler(CommandHandler("randomimage", random_image))
app.add_handler(CommandHandler("searchimage", search_image))
app.add_handler(MessageHandler(filters.TEXT, message_handle))

print("polling")
app.run_polling()
