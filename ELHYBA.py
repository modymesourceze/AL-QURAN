from mody import Mody
import telebot
from telebot import types

token = Mody.ELHYBA
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def welcome(message):
    name = message.from_user.first_name
    bot.send_message(message.chat.id,"مرحبا بك {} الرجاء ارسال رقم الصفحة لتصفح صفحات القرآن الكريم".format(name))

@bot.message_handler(func=lambda message: True)
def all(message):
    try:
    	num = int(message.text)
    	url = "https://quran.ksu.edu.sa/png_big/" + str(num) + ".png"
    	
    	keyboard = types.InlineKeyboardMarkup()
    	cou = types.InlineKeyboardButton(text=f"• {num} •", callback_data="couu")
    	previous = types.InlineKeyboardButton(text="صفحة السابقة", callback_data=str(num - 1))
    	next = types.InlineKeyboardButton(text="صفحة التالية", callback_data=str(num + 1))
    	
    	keyboard.row(cou)
    	keyboard.row(previous,next)
    	
    	bot.send_photo(message.chat.id,url, reply_markup=keyboard)
    except:
    	pass
    	bot.reply_to(message,'error')
    
@bot.callback_query_handler(func=lambda call: True)
def alll(call):
    if call.data == 'couu':
     bot.answer_callback_query(call.id, text='هذا زر يعرض فيه العدد فقط')
     exit()
    num = int(call.data)
    url = "https://quran.ksu.edu.sa/png_big/" + str(num) + ".png"

    keyboard = types.InlineKeyboardMarkup()
    
    cou = types.InlineKeyboardButton(text=f"• {num} •", callback_data="couu")
    previous = types.InlineKeyboardButton(text="صفحة السابقة", callback_data=str(num - 1))
    next = types.InlineKeyboardButton(text="صفحة التالية", callback_data=str(num + 1))
    
    
    keyboard.row(cou)
    keyboard.row(previous,next)

    bot.edit_message_media(types.InputMediaPhoto(url), call.message.chat.id, call.message.message_id,reply_markup=keyboard)
    
print('تم التطوير بواسطة مودي الهيبه @ELHYBA')
bot.infinity_polling()