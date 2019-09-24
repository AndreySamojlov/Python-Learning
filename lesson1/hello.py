from telegram.ext import Updater, CommandHandler
PROXY = {'proxy_url': 'socks5://165.22.220.1:1080',
    'urllib3_proxy_kwargs': {'username': 'learn_python2', 'password': 'FGN7MGgdTznt'}}
def greet_user(bot, update):
    print('Вызван /start')
def main():
    mybot = Updater("753562634:AAF2WYF8aMg27-_t6ANIuln3-QU3ZJx8hyo",  request_kwargs=PROXY)
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    mybot.start_polling()
    mybot.idle()

main()