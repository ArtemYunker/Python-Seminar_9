from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes,MessageHandler
import sqlite3



conn = sqlite3.connect('spravochnic.db')
cursor = conn.cursor()


async def hi_comands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hi {update.effective_user.first_name}!')

async def help_comands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi\n/help\n/show\n/find\n/add\n/delite')


async def show_comands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    cursor.execute("select * from book")
    results = cursor.fetchall()
    await update.message.reply_text(f'{results}')


async def find_comands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    temp = update.message.text
    surname = temp.split()
    cursor.execute(f"select * from book where surname like '%{surname[1]}%'")
    results = cursor.fetchall()
    await update.message.reply_text(f'{results}')


async def add_comands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    temp = update.message.text
    surname1 = temp.split()

    surname = surname1[1]
    name = surname1[2]
    phone_number = int(surname1[3])

    cursor.execute(
    f"insert into book (surname, name, phone_number) "
    f"values ('{surname}', '{name}', {phone_number})")
    conn.commit()

    cursor.execute("select * from book")
    results = cursor.fetchall()
    await update.message.reply_text(f'{results}')

async def delite_comands(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # удалить студента
    cursor.execute("select * from book")
    results = cursor.fetchall()
    await update.message.reply_text(f'{results}')

    temp = update.message.text
    number = temp.split()
    id = int(number[1])
    print(id)

    cursor.execute(f"delete from book where id={id}")
    conn.commit()

    cursor.execute("select * from book")
    results = cursor.fetchall()
    await update.message.reply_text(f'{results}')
