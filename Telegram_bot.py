from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler, filters
from telegram.constants import DiceEmoji
import pymongo
import os
from dotenv import load_dotenv
load_dotenv()

TOKEN=os.getenv('TOKEN')
try:
    client = pymongo.MongoClient("mongodb+srv://onlyplayxerath:iEEzRNyrBjaPPfTt@cluster0.00l13mt.mongodb.net/?retryWrites=true&w=majority")
    db = client["training-python"]
    collection = db['users']
    # user = {
    #     "name": "DuckY",
    #     "age": 30,
    # }
    # result = collection.insert_one(user).inserted_id
    # print(f"New user added with id: {result}")
    print("connected to mongo")
except Exception as e:
    print(e)

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_dice(emoji=DiceEmoji.DICE)
    
async def add(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text[4:]
    word_list = text.split()
    name = word_list[0]
    age = word_list[1]
    new_user = {
        'name': name,
        'age': age,
    }
    await update.message.reply_text(f"New user added with id: {collection.insert_one(new_user).inserted_id}", reply_to_message_id=update.message.id, protect_content=True)

def search_name_with_keyboard(keyword):
    result = collection.find_one({'name': keyword})
    return result

async def message_handle(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    await update.message.reply_text(f"{search_name_with_keyboard(text)}")

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("dice", dice))
app.add_handler(CommandHandler("add", add))
app.add_handler(MessageHandler(filters.TEXT, message_handle))

print("polling")
app.run_polling()
