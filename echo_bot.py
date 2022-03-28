import logging
import requests
import json
import random
from telegram.ext import Updater,CommandHandler,MessageHandler,filters,Filters,CallbackContext


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

TOKEN="5062762517:AAH94lqtKSSK8rki0Dy_cNN3KIDZE7ajC2Y"


def start(update,context):
    author=update.message.from_user.first_name
    reply="Hi {} /n How may I help you".format(author)
    context.bot.send_message(chat_id=update.message.chat_id,text=reply)
def _help(update,context):
    author=update.message.from_user.last_name
    reply="Hi {} you got ".format(author)+update.message.text[1:]
    context.bot.send_message(chat_id=update.message.chat_id,text=reply)
def echo_text(update,context):
    
    reply=update.message.text
    if reply.lower() =="i love you":
        context.bot.send_message(chat_id=update.message.chat_id,text="I love you too")
    elif reply.lower() =="i am good" or reply.lower()=="i am fine":
        context.bot.send_message(chat_id=update.message.chat_id,text="Great !!")
    elif reply.lower() =="fuck you" or reply.lower()=="fuck u":
        context.bot.send_message(chat_id=update.message.chat_id,text=reply+" "+update.message.from_user.first_name)
    elif reply.lower() =="how is the josh":
        context.bot.send_message(chat_id=update.message.chat_id,text="Highhh Sirrr...!!!")
    elif reply.lower() =="bye" :
        context.bot.send_message(chat_id=update.message.chat_id,text="Ok Bye")
    elif reply.lower() =="who made you" or reply.lower()=="who created you":
        context.bot.send_message(chat_id=update.message.chat_id,text="Soumyadip Bhattacharjee created me on 16/12/2021")
    elif reply.lower() =="how old are you" or reply.lower() =="what is your age?" or reply.lower() =="your age?" or reply.lower() =="what is your age" or reply.lower() =="your age" or reply.lower() =="how old you are" or reply.lower() =="when did you born":
        context.bot.send_message(chat_id=update.message.chat_id,text="I was born on 16/12/2021..you can guess my age")
    elif reply.lower() =="how are you" or reply.lower() =="how do you do":
        context.bot.send_message(chat_id=update.message.chat_id,text="I am fit and fine !!\nThanks for asking\nBtw, How are you?")
    elif reply.lower() =="hi" or reply.lower() =="hello" or reply.lower() =="hii":
        context.bot.send_message(chat_id=update.message.chat_id,text="Hello "+update.message.from_user.first_name)
    elif reply.lower() =="Bye" or reply.lower() =="byee" or reply.lower() =="by":
        context.bot.send_message(chat_id=update.message.chat_id,text="Ok Byee")
    elif reply.lower() =="what is your name" or reply.lower() =="what is ur name" or reply.lower() =="ur name?" or reply.lower() =="ur name" or reply.lower() =="your name":
        context.bot.send_message(chat_id=update.message.chat_id,text="My name is Pega Bot")
    elif reply.lower() =="Are you a robot?" or reply.lower() =="Are you a bot?":
        context.bot.send_message(chat_id=update.message.chat_id,text="Yes I am a Bot, but I'm a good one. Let me prove it. How can I help you?")
    elif reply.lower() =="good morning":
        context.bot.send_message(chat_id=update.message.chat_id,text=reply+" "+update.message.from_user.first_name)
    elif reply.lower() =="good night":
        context.bot.send_message(chat_id=update.message.chat_id,text=reply+" "+update.message.from_user.first_name)                                      
    elif reply.lower() =="good morning":
        context.bot.send_message(chat_id=update.message.chat_id,text=reply+" "+update.message.from_user.first_name)
    elif reply.lower() =="tell me a joke" or reply.lower() =="give me joke" or reply.lower() =="give joke" or reply.lower() =="tell a joke" or reply.lower() =="tell me joke":
        a=random.randint(1,500)
        url="http://api.icndb.com/jokes/{}".format(a)
        r=requests.get(url)
        j=json.loads(r.content)
        context.bot.send_message(chat_id=update.message.chat_id,text=j['value']['joke'])
    elif reply.lower().split(" ")[0]=="temperature" or reply.lower().split(" ")[0]=="weather":
        api="https://api.openweathermap.org/data/2.5/weather?q={}&appid=68e3d1030f79f97308dc244096020eb5".format(reply.split(" ")[2])
        r=requests.get(api)
        j=json.loads(r.content)
        context.bot.send_message(chat_id=update.message.chat_id,text=(j['main']['temp']-273))
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
    dp.add_handler(CommandHandler("help",_help))
    dp.add_handler(MessageHandler(filters.Filters.text,echo_text))
    dp.add_handler(MessageHandler(filters.Filters.sticker,echo_sticker))

    dp.add_error_handler(error)
    updater.start_polling()
    logger.info("Started Polling.....")
    updater.idle()

if __name__ == "__main__" :
    main()  
    

