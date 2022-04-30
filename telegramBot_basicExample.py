from telegram.ext import Updater, CommandHandler

token = "" #token of the bot, you can find it on BotFather chat 

#command /start
def start(update, context): 
    chat_id = update.effective_chat.id
    update.message.reply_text("start") #print on the bot "start"
    print("start called from chat with id = {}".format(chat_id))

#comando /end
def end(update, context):
    chat_id = update.effective_chat.id
    update.message.reply_text("end") #print on the bot "end"
    print("end called from chat with id = {}".format(chat_id))

#main d
def main(): 
    updater = Updater(token) #updater listen the chat 
   #dispatcher, manage payload (words after "/")
    updater.dispatcher.add_handler(CommandHandler("start", start))  #if write  /start --> call start()
    updater.dispatcher.add_handler(CommandHandler("end", end))      #if write /end --> call end()
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()