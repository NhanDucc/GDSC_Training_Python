from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from telegram.constants import DiceEmoji

import os
from dotenv import load_dotenv
load_dotenv()

TOKEN=os.getenv('TOKEN')

async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def dice(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_dice(emoji=DiceEmoji.DICE)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("hello", hello))
app.add_handler(CommandHandler("dice", dice))

print("polling")
app.run_polling()
