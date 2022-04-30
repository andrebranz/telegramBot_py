# TELEGRAM BOT UPDATE WEB PAGE 
# Andrea 30/04/22 - 
# https://github.com/andrebranz/telegramBot_py
from telegram.ext import Updater, CommandHandler
import threading
import requests
import logging
import time

logging.basicConfig(level=logging.INFO)

token = ""      #token dof the bot, you can find it on the BotFather chat
target_url = "" #this site will be monitored by the bot

chat_ids = set()
updater = Updater(token) #create the updater, this will controll the chat 


def page_updated(): # called when the page will be updated
    interval = 5    # set the period of sleep to monitoring the site 
    older = requests.get(target_url).text

    while True:
        if len(chat_ids) > 0: # if someone started the bot
            page_data = requests.get(target_url).text # get the request 
            if page_data != older: # if the new page (HTML)  is different from the older
                older = page_data  # set the newest page to the "older" variable
                for chat_id in chat_ids: # loop every id, that's are using the bot
                    updater.bot.send_message(chat_id=chat_id, text="New Update!") # send this message on the bot chat 
        time.sleep(interval) # sleep 5 ms

# this function is called by "/start"
def start(update, context):
    chat_id = update.effective_chat.id # get the id of the client
    updater.bot.send_message(chat_id=chat_id, text="Bot Started")# print the message
    chat_ids.add(chat_id) # add to the chat_ids list the id that write"/end"
    logging.info("{}: start".format(chat_id))

# this function is called by "/end"
def end(update, context):
    chat_id = update.effective_chat.id # get the id of the client
    updater.bot.send_message(chat_id=chat_id, text="Bot Blocked") # print the message
    chat_ids.remove(chat_id) # remove from the chat_ids list the id that write"/end"
    logging.info("{}: stop".format(chat_id)) 

#this is the main of the program
def main():
    updater.dispatcher.add_handler(CommandHandler("start", start)) # when someone write "/start" --> call start()
    updater.dispatcher.add_handler(CommandHandler("end", end))     # when someone write "/end" --> call end()
    threading.Thread(target=page_updated).start()
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()