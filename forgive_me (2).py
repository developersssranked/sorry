import telebot 
from telebot import types
import random

bot = telebot.TeleBot ("5499870186:AAE2aT3J0pQ8em5xcYnaZRHWOgTKKrDLCq0")

x = ["Я искренне сожалею о своем поступке","Я не в силах исправить ошибку изменить прошлое","Мне невыносимо думать, что я причинил тебе боль ,заставил переживать","Очень надеюсь, что ты сменишь гнев на милость, простишь меня и позволишь доказать, как ты важна для меня"]
# random_index = random.randrange(len(x))

@bot.message_handler (commands= ["start"])
def help (hep):
    mrk = types.ReplyKeyboardMarkup( resize_keyboard=True )
    mrk.add  (types.KeyboardButton ("нажми"))
    mes = bot.send_message (hep.chat.id, "милион извенений для тебя", reply_markup= mrk) 
    bot.register_next_step_handler (mes , how)

@bot.message_handler (content_types= ["text"])
def how (mes):
    if mes.text == "нажми":
        mrk = types.ReplyKeyboardMarkup( resize_keyboard=True )
        mrk.add  (types.KeyboardButton ("нажми"))
        mess = bot.send_message (mes.chat.id , f"{random.choice(x)}", reply_markup= mrk)
        bot.register_next_step_handler ( mess , how2 )


def how2 (mes):
    if mes.text == "нажми":
        mrk = types.ReplyKeyboardMarkup( resize_keyboard=True )
        mrk.add  (types.KeyboardButton ("нажми"))
        mess = bot.send_message (mes.chat.id , f"{random.choice(x)}", reply_markup= mrk)
        bot.register_next_step_handler ( mess , how )





bot.polling (none_stop=True)

# import random

# test_list = ["1", "2", "3", "4", "5", "6"]
# random_index = random.randrange(len(test_list))

# print(test_list[random_index])

# Источник: https://egorovegor.ru/python-select-random-element