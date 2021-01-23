

import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import telegram

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

bot = telegram.Bot(token = '1472815090:AAERtN_sa3xL5oWPZEC_WIwt3FSmpKvzQcs')
updater = Updater('1472815090:AAERtN_sa3xL5oWPZEC_WIwt3FSmpKvzQcs', use_context=True)


dp = updater.dispatcher
info = dict()
def start(update, context):
    iD = update.message.chat_id
    bot_welcome = "سلام به ربات انجمن علمی مهندسی مواد و متالورژی خوش آمدید لطفا اطلاعات خود را به وارد کنید"
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
       info[iD] = [text + ",",1]
       

   print(info)
   print("got text message :", text)
   
   if info[iD][1] == 1:
       message = "شماره دانشجوئی خود را وارد کنید"
       bot.send_message(chat_id = iD,text = message)
       pass
   elif info[iD][1] == 2:
       message = " مقطع تحصیلی خود را وارد کنید"
       bot.send_message(chat_id = iD,text = message)
       pass
   elif info[iD][1] == 3:
       message = " ایمیل خود را وارد کنید"
       bot.send_message(chat_id = iD,text = message)
       pass
   elif info[iD][1] == 4:
       message = " لطفا شماره تماس خود را وارد کنید"
       bot.send_message(chat_id = iD,text = message)
       pass
   elif info[iD][1] == 5:
       message = " درسی که برای تدریس یار شدن درخواست دارین" + "\n" + "برای درس اصول تولید فلزات عدد 1 و برای درس کارگاه محاسبات مهندسی عدد 2 را وارد کنید"
       bot.send_message(chat_id = iD,text = message)
       pass
   elif info[iD][1] == 6:
       if text == "1" or text == "۱":
           message = "برای درس اصول تولید فلزات موارد پیشنهادی که بتوانید به عنوان تدریسیار در آن کمک کنید به صورت زیر است " + "\n" + "۱-برگزاری کلاس حل تمرین و تصحیح تکالیف" + "\n" +"۲-آموزش چهار ماژول اول نرم افزار HSC" + "\n" + "۳-تهیه تکلیف از HSCو تحویل پاسخ دانشجویان و راهنمایی برخط" + "\n" +"۴- جمع آوری فیلم ها و انیمیشن های مرتبط با استخراج و بازیابی فلزات از منابع مختلف" + "\n" + "۵-سایر موارد"
           bot.send_message(chat_id = iD,text = message)    
           pass
       elif text == "2" or text == "۲":
           message = "چه توانایی ها دارید که بتوانید به عنوان تدریسیار کمک کنید"
           bot.send_message(chat_id = iD,text = message)
       pass
   elif info[iD][1] == 7:
       message = "علت و انگیزه‌ی شما برای تدریسیار شدن در این درس چیست؟"
       bot.send_message(chat_id = iD,text = message)
       pass
   
   
   elif info[iD][1] == 8:
       message ="خیلی متشکر از توجه شما بررسی ها نسبت به درخواست شما انجام خواهد شد و در صورتی که انتخاب شدید با شما تماس گرفته می‌شود"
       bot.send_message(chat_id = iD,text = message)
       file = open("info.txt","a",encoding=('utf-8'))
       file.write(info[iD][0] + "\n")
       file.close()
       info[iD][1] = 0
       pass


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    """Start the bot."""
    
   

    
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

   
    updater.idle()


if __name__ == '__main__':
    main()