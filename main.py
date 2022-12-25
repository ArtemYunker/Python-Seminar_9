from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import*
import sqlite3


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

app = ApplicationBuilder().token("5850663540:AAFZccc9POZInfj2tDUPtGqECF46RGyjyYw").build()

print("server start")
app.add_handler(CommandHandler("hi", hi_comands))
app.add_handler(CommandHandler("help", help_comands))
app.add_handler(CommandHandler("show", show_comands))
app.add_handler(CommandHandler("find", find_comands))
app.add_handler(CommandHandler("add", add_comands))
app.add_handler(CommandHandler("delite", delite_comands))




app.run_polling()