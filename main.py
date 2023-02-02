from beem.account import Account
import telebot
from acces import TELEGRAM_TOKEN
from telebot.types import ForceReply





bot = telebot.TeleBot(TELEGRAM_TOKEN)


@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, 'Hola bienvenido estos son los comandos que actualmente puedes utilizar \n/balance luego colocar el usuario que deseas ver su balance y te dara como respuesta el balance y reward pendiente')


@bot.message_handler(commands=['balance'])
def balance(message):
    markup = ForceReply()
    msg = bot.send_message(message.chat.id, 'Coloca el nombre de usuario', reply_markup=markup)
    bot.register_next_step_handler(msg, registrar_valor)


def registrar_valor(message):
    nombre = message.text
    account = Account(f"{nombre}")
    bot.send_message(message.chat.id, f'Balance {account.balances["available"][0]}  {account.balances["available"][1]} \nReward pending {account.balances["rewards"][0]} {account.balances["rewards"][1]}.')
  


if __name__ == '__main__':
    print('iniciando')
    bot.infinity_polling()
    print('termino')