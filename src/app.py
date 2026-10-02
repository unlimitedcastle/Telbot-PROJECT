import telebot
from time import sleep

import app_api

bot = telebot.TeleBot('8753651858:AAE5wgN_t5-noxjPGAhxackInfYbqDyenCg')

print('created...............')

@bot.message_handler(commands=['start'])
def say_hello(message):
    bot.send_message(message.chat.id, text=' خوشامدید')

@bot.message_handler(commands=['help', 'support'])
def show_help_msg(message):
    bot.reply_to(message, text='اگر مشکل یا سوالی دارید به بخش درباره ما مراجعه کنید و به شماره داخل ان پیام دهید و مشکلتان را ذکر کنید')



@bot.message_handler(commands=['menu'])
def show_menu(message):

    markup = telebot.types.ReplyKeyboardMarkup(row_width=2)


    btn1=telebot.types.KeyboardButton(text='about us')
    btn2=telebot.types.KeyboardButton(text='movies')
    btn3=telebot.types.KeyboardButton(text='back')

    markup.add(btn1,btn2, btn3 )
    bot.send_message(message.chat.id, text='یک گزینه انتخاب کنید', reply_markup=markup)

def get_movie_info(message):
    
    bot.send_message(message.chat.id, text='درحال دریافت اطلاعات فیلم....')
    bot.send_chat_action(message.chat.id, action='typing')
    sleep(2)
    movie_id = message.text
    try:
        result = app_api.get_movie_info_by_id(movie_id)
        bot.send_message(message.chat.id, text=f'{result[0]}/ {result[1]} / {result[-2]} / {result[-1]}')
    except:
     bot.send_message("ایدی صحیح نیست")


@bot.message_handler(func=lambda message:True)
def handle_all_messages(message):
    if message.text == 'about us' :
        phone = '09xxxxxxxx'
        info = f'شماره من: {phone}'
        bot.send_message(message.chat.id, text=info)
    elif message.text == 'back' :
        markup = telebot.types.ReplyKeyboardRemove()
        bot.send_message(message.chat.id, text='بازگشت انجام شد', reply_markup=markup)
    elif message.text == 'movies' :
    
        msg = bot.send_message(message.chat.id, text='ایدی فیلم را وارد کنید')
        bot.register_next_step_handler(msg, get_movie_info)
            
    else:
        bot.send_message(message.chat.id, text='متوجه منظورتان نشدم')






if __name__ == '__main__':
    bot.infinity_polling()