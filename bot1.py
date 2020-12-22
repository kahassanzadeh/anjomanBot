#!/usr/bin/env python
# -*- coding: utf-8 -*-
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.

First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.

Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram
# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

bot = telegram.Bot(token = 't')
updater = Updater('t', use_context=True)

 # Get the dispatcher to register handlers
dp = updater.dispatcher
info = dict()
# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update, context):
    iD = update.message.chat_id
    # print the welcoming message
    bot_welcome = "سلام به ربات انجمن علمی مهندسی مواد و متالورژی خوش آمدید لطفا اطلاعات خود را به وارد کنید"
    # send the welcoming message
    bot.send_message(chat_id = iD,text = bot_welcome)
    bot_welcome = "نام و نام خانوادگی خود را وارد کنید"
    bot.send_message(chat_id = iD,text = bot_welcome)
    pass


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(update, context):
    
   iD = update.message.chat_id
   text = update.message.text.encode('utf-8').decode()
   
   if (iD in info) and text != "/start":
       info[iD][1] += 1
       info[iD][0] += text + ","
       pass
   else:
       info[iD] = [text,1]
       

   print(info)
   # for debugging purposes only
   print("got text message :", text)
   # the first time you chat with the bot AKA the welcoming message
   
   if info[iD][1] == 1:
       message = "شماره دانشجوئی خود را وارد کنید"
       bot.send_message(chat_id = iD,text = message)
       pass
   elif info[iD][1] == 2:
       message = "معدل خود را وارد کنید"
       bot.send_message(chat_id = iD,text = message)
       pass
   elif info[iD][1] == 3:
       message = " مقطع تحصیلی خود را وارد کنید"
       bot.send_message(chat_id = iD,text = message)
       pass
   elif info[iD][1] == 4:
       message = " درسی که برای تدریس یار شدن درخواست دارین"
       bot.send_message(chat_id = iD,text = message)
       pass
   elif info[iD][1] == 5:
       message = "نمره‌ی درسی که برای تدریس یار شدن درخواست دارین"
       bot.send_message(chat_id = iD,text = message)
       pass
   elif info[iD][1] == 6:
       message =" لطفا شماره تماس خود را وارد کنید"
       bot.send_message(chat_id = iD,text = message)
       pass
   elif info[iD][1] == 7:
       message =  " ایمیل خود را وارد کنید"
       bot.send_message(chat_id = iD,text = message)
       pass
   elif info[iD][1] == 8:
       message = "تمایل به کمک در چه موردی از کار های تدریسیاری دارید؟"
       bot.send_message(chat_id = iD,text = message)
       pass
   elif info[iD][1] == 9:
       message ="خیلی متشکر از توجه شما بررسی ها نسبت به درخواست شما انجام خواهد شد و در صورتی که انتخاب شدید با شما تماس گرفته می‌شود"
       bot.send_message(chat_id = iD,text = message)
       file = open("info.txt","a",encoding=('utf-8'))
       file.write(info[iD][0] + "\n")
       file.close()
       pass


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    # Make sure to set use_context=True to use the new context based callbacks
    # Post version 12 this will no longer be necessary
   

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    # on noncommand i.e message - echo the message on Telegram
    dp.add_handler(MessageHandler(Filters.text, echo))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()