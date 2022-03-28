import logging
import requests
import json
import random
from telegram import ReplyKeyboardMarkup
from telegram.ext import Updater,CommandHandler,MessageHandler,filters,Filters,CallbackContext
from di import fetch_news, get_reply,topics_keyboard

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

TOKEN="5062762517:AAH94lqtKSSK8rki0Dy_cNN3KIDZE7ajC2Y"

def news(update,context):
    context.bot.send_message(chat_id=update.message.chat_id,text="Choose a category",
    reply_markup=ReplyKeyboardMarkup(keyboard=topics_keyboard,one_time_keyboard=True))

def start(update,context):
    author=update.message.from_user.first_name
    reply="Hi {} /n How may I help you".format(author)
    context.bot.send_message(chat_id=update.message.chat_id,text=reply)
def _help(update,context):
    author=update.message.from_user.last_name
    reply="Hi {} you got ".format(author)+update.message.text[1:]
    context.bot.send_message(chat_id=update.message.chat_id,text=reply)
def reply_text(update,context):
    intent,reply=get_reply(update.message.text,update.message.chat_id)
    if intent =="Topic_news":
        articles=fetch_news(reply)
        for a in articles:
            context.bot.send_message(chat_id=update.message.chat_id,text=a["link"])   
        
    else:
        
        context.bot.send_message(chat_id=update.message.chat_id,text=reply)        
           
def echo_sticker(update,context):
    
    reply=update.message.sticker.file_id
    context.bot.send_message(chat_id=update.message.chat_id,sticker=reply)
def error(bot,update):
    logger.error("Update'%s' caused error'%s' ",update,update.error)

def main():
    updater=Updater(TOKEN)  ## Receiving Updates
    dp=updater.dispatcher   ##Managing Updates

    dp.add_handler(CommandHandler("start",start))
    dp.add_handler(CommandHandler("news",news))
    dp.add_handler(CommandHandler("help",_help))
    dp.add_handler(MessageHandler(filters.Filters.text,reply_text))
    dp.add_handler(MessageHandler(filters.Filters.sticker,echo_sticker))

    dp.add_error_handler(error)
    updater.start_polling()
    logger.info("Started Polling.....")
    updater.idle()

if __name__ == "__main__" :
    main()  
    

