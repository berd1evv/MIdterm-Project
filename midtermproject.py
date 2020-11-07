import telebot
import time
from telebot import types

bot = telebot.TeleBot("1449081953:AAHomtUCkuheMhHgT3a3xx7IOm1CIsxJ5Cc")

# Exchange rates
USD = 83.8064
EUR = 98.5731
RUB = 1.0682
KZT = 0.1941

# Inflation
inf = 5.4

# Purchase_Gold_Bars
purch_gold1 = 6703
purch_gold2 = 12304
purch_gold5 = 29465
purch_gold10 = 58085
purch_gold31 = 177779
purch_gold100 = 525674

# Sale_Gols_Bars
sale_gold1 = 6736
sale_gold2 = 12354
sale_gold5 = 29553
sale_gold10 = 58201
sale_gold31 = 180446
sale_gold100 = 541444

# Date
time_string = time.strftime("%d/%m/%Y")


@bot.message_handler(commands=['start'])
def welcome(message):
    # keyboard
    keyboard = types.ReplyKeyboardMarkup(True)
    keyboard.row("Exchange rate", "Converter", "Inflation")
    keyboard.row("Price for Gold bars")
    bot.send_message(message.chat.id, '''Welcome, {0.first_name}!\nI'm - <b>{1.first_name}</b>,
choose one of this buttons'''
                     .format(message.from_user, bot.get_me()),
                     parse_mode='html', reply_markup=keyboard)
# functions that used in convertion of currencies


def usdkgs(message):
    try:
        curr = message.text
        curr = float(curr)
        convert = USD * curr
        bot.send_message(message.from_user.id, "%s KGS" % convert)
        bot.register_next_step_handler(message, func)
    except ValueError:
        bot.send_message(message.from_user.id, 'It is not a number')


def eurkgs(message):
    try:
        curr = message.text
        curr = float(curr)
        convert = EUR * curr
        bot.send_message(message.from_user.id, "%s KGS" % convert)
        bot.register_next_step_handler(message,  func)
    except ValueError:
        bot.send_message(message.from_user.id, 'It is not a number')


def rubkgs(message):
    try:
        curr = message.text
        curr = float(curr)
        convert = RUB * curr
        bot.send_message(message.from_user.id, "%s KGS" % convert)
        bot.register_next_step_handler(message, func)
    except ValueError:
        bot.send_message(message.from_user.id, 'It is not a number')


def kztkgs(message):
    try:
        curr = message.text
        curr = float(curr)
        convert = KZT * curr
        bot.send_message(message.from_user.id, "%s KGS" % convert)
        bot.register_next_step_handler(message, func)
    except ValueError:
        bot.send_message(message.from_user.id, 'It is not a number')


def kgsusd(message):
    try:
        curr = message.text
        curr = float(curr)
        convert = curr / USD
        bot.send_message(message.from_user.id, "%s USD" % convert)
        bot.register_next_step_handler(message, func)
    except ValueError:
        bot.send_message(message.from_user.id, 'It is not a number')


def kgseur(message):
    try:
        curr = message.text
        curr = float(curr)
        convert = curr / EUR
        bot.send_message(message.from_user.id, "%s EUR" % convert)
        bot.register_next_step_handler(message, func)
    except ValueError:
        bot.send_message(message.from_user.id, 'It is not a number')


def kgsrub(message):
    try:
        curr = message.text
        curr = float(curr)
        convert = curr / RUB
        bot.send_message(message.from_user.id, "%s RUB" % convert)
        bot.register_next_step_handler(message, func)
    except ValueError:
        bot.send_message(message.from_user.id, 'It is not a number')


def kgskzt(message):
    try:
        curr = message.text
        curr = float(curr)
        convert = curr / KZT
        bot.send_message(message.from_user.id, "%s KZT" % convert)
        bot.register_next_step_handler(message, func)
    except ValueError:
        bot.send_message(message.from_user.id, 'It is not a number')


@bot.message_handler(content_types=['text'])
def func(message):
    get_message = message.text.strip()
    if message.text == 'Converter':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row("USD to KGS", "EUR to KGS")
        keyboard.row("RUB to KGS", "KZT to KGS")
        keyboard.row("KGS to USD", "KGS to EUR")
        keyboard.row("KGS to RUB", "KGS to KZT")
        keyboard.row("Back")
        bot.send_message(message.chat.id, 'Choose one of this buttons',
                         reply_markup=keyboard)
    elif message.text == 'Back':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row("Exchange rate", "Converter", "Inflation")
        keyboard.row("Price for Gold bars")
        bot.send_message(message.chat.id, 'Choose one of this buttons',
                         reply_markup=keyboard)
    # Exchage rates
    elif message.text == 'Exchange rate':
        bot.send_message(message.chat.id, "Exchange rates on %s" % time_string)
        bot.send_message(message.chat.id, "USD - %s" % USD)
        bot.send_message(message.chat.id, "EUR - %s" % EUR)
        bot.send_message(message.chat.id, "RUB - %s" % RUB)
        bot.send_message(message.chat.id, "KZT - %s" % KZT)
    # Inflation
    elif message.text == 'Inflation':
        bot.send_message(message.chat.id, "Inflation is %s percent" % inf)
    # Price for gold bars
    elif message.text == 'Price for Gold bars':
        keyboard = types.ReplyKeyboardMarkup(True)
        keyboard.row("Purchase", "Sale")
        keyboard.row("Back")
        bot.send_message(message.chat.id, 'Choose one of this buttons',
                         reply_markup=keyboard)

    elif message.text == 'Purchase':
        bot.send_message(message.chat.id, "Purchase:")
        bot.send_message(message.chat.id, "1.0 gramm - %s KGS" % purch_gold1)
        bot.send_message(message.chat.id, "2.0 gramm - %s KGS" % purch_gold2)
        bot.send_message(message.chat.id, "5.0 gramm - %s KGS" % purch_gold5)
        bot.send_message(message.chat.id, "10.0 gramm - %s KGS" % purch_gold10)
        bot.send_message(message.chat.id, "31.10035 gramm - %s KGS" %
                         purch_gold31)
        bot.send_message(message.chat.id, "100.0 gramm - %s KGS" %
                         purch_gold100)

    elif message.text == 'Sale':
        bot.send_message(message.chat.id, "Sale:")
        bot.send_message(message.chat.id, "1.0 gramm - %s KGS" % sale_gold1)
        bot.send_message(message.chat.id, "2.0 gramm - %s KGS" % sale_gold2)
        bot.send_message(message.chat.id, "5.0 gramm - %s KGS" % sale_gold5)
        bot.send_message(message.chat.id, "10.0 gramm - %s KGS" % sale_gold10)
        bot.send_message(message.chat.id, "31.10035 gramm - %s KGS" %
                         sale_gold31)
        bot.send_message(message.chat.id, "100.0 gramm - %s KGS" %
                         sale_gold100)
    # Convert
    elif get_message == 'USD to KGS':
        currency = 'How much dollar you want to convert?'
        bot.send_message(message.chat.id, currency)
        bot.register_next_step_handler(message, usdkgs)

    elif get_message == 'EUR to KGS':
        currency = 'How much euro you want to convert?'
        bot.send_message(message.chat.id, currency)
        bot.register_next_step_handler(message, eurkgs)

    elif get_message == 'RUB to KGS':
        currency = 'How much ruble you want to convert?'
        bot.send_message(message.chat.id, currency)
        bot.register_next_step_handler(message, rubkgs)
    elif get_message == 'KZT to KGS':
        currency = 'How much tenge you want to convert?'
        bot.send_message(message.chat.id, currency)
        bot.register_next_step_handler(message, kztkgs)

    elif get_message == 'KGS to USD':
        currency = 'How much som you want to convert?'
        bot.send_message(message.chat.id, currency)
        bot.register_next_step_handler(message, kgsusd)

    elif get_message == 'KGS to EUR':
        currency = 'How much som you want to convert?'
        bot.send_message(message.chat.id, currency)
        bot.register_next_step_handler(message, kgseur)

    elif get_message == 'KGS to RUB':
        currency = 'How much som you want to convert?'
        bot.send_message(message.chat.id, currency)
        bot.register_next_step_handler(message, kgsrub)

    elif get_message == 'KGS to KZT':
        currency = 'How much som you want to convert?'
        bot.send_message(message.chat.id, currency)
        bot.register_next_step_handler(message, kgskzt)
# RUN
bot.polling(none_stop=True, interval=0)
