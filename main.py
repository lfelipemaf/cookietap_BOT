from pprint import pprint

import telebot

API = "2030387825:AAHvXgImEyDcPkTYL4myTgsuBx8zg_CuN0w"

bot = telebot.TeleBot(API)

@bot.message_handler(commands=["atualizar"])
def invetory(message):
    text = """Qual o produto quer atualizar?
    /cookie
    /brownie
    /outros
    """

    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=["lancar"])
def invetory(message):
    print(message)
    text = """Qual é o pedido :
    """

    bot.reply_to(message, text)

@bot.message_handler(commands=["vendas"])
def invetory(message):
    text = """As vendas foram:
    
    """

    bot.reply_to(message, text)
def verify(message):
    return True


@bot.message_handler(func=verify)
def answer(message):
    text = f"""Olá {message.chat.first_name}, aqui é o bot do Cookie Therapy
    O que deseja fazer:
    /atualizar o estoque
    /lancar pedido
    /vendas do dia
    """
    print(message)
    bot.send_message(message.chat.id, text)


bot.polling()
