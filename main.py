import telegram
import requests, json
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Bot = telegram.bot(token='1640440860:AAGi01YFA5bJ9LKLOGABW0FAOzShJZ6kL-U')
updater = Updater(token='TOKEN', use_context=True)
dispatcher = updater.dispatcher

def hello(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Hello World")

def summary(update, context):
    resp = requests.get('https://api.covid19api.com/summary')
    if(resp.status_code == 200):
        data = resp.json()
        context.bot.send_message(chat_id = update.effective_chat.id, text = data['Global'])
    else:
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'Error, Something went wrong.')

def India(update, context):
    resp = requests.get('https://api.covid19api.com/summary')
    data = resp.json()
    context.bot.send_message(chat_id=update.effective_chat.id, text = data['Countries'][76])

corona_summary_handler = CommandHandler('Summary', summary)
India_hander = CommandHandler('India', India)
hello_handler = CommandHandler('hello', hello)
dispatcher.add_handler(hello_handler)
dispatcher.add_handler(corona_summary_handler)
dispatcher.add_handler(India_hander)

updater.start_polling()
