from mody import Mody
import telebot
import requests
import re
from telebot import types
token = Mody.ELHYBA
bot = telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start(message):
    
            if message.chat.type == "private":
                ch = "TeAmDaiet"
                idu = message.chat.id
                join = requests.get(f"https://api.telegram.org/bot{token}/getChatMember?chat_id=@{ch}&user_id={idu}").text
                if '"status":"left"' in join:
                    bot.send_message(message.chat.id,f"🚸| عذرا عزيزي\n🔰| عليك الاشتراك بقناة البوت\nلتتمكن من استخدامه\n- https://t.me/{ch}\n‼️| اشترك ثم ارسل /start",disable_web_page_preview="true")
                else:
                	btn = types.InlineKeyboardButton(text='⦗ اضغط هنا للاشتراك ⦘',url='https://t.me/TeAmDaiet')
                	b = types.InlineKeyboardMarkup()
                	b.add(btn)
                	bot.reply_to(message,'تحدث معي',reply_markup=b)
	
                	

url = "https://bumcomingo.simsimi.com/simtalk/get_talk_set"
headers = {
    'accept': 'application/json, text/plain, */*',
    'os': 'a',
    'av': '8.4.4',
    'appcheck': '',
    'Content-Type': 'application/json',
    'Content-Length': '159',
    'Host': 'bumcomingo.simsimi.com',
    'Connection': 'Keep-Alive',
    'Accept-Encoding': 'gzip',
    'User-Agent': 'okhttp/4.9.1'
}
	
@bot.message_handler(content_types=['text'])
def sim(message):
    msg = message.text
    payload = {
        "uid": 414477568,
        "av": "8.4.4",
        "os": "a",
        "lc": "ar",
        "cc": "EG",
        "tz": "Africa/Cairo",
        "cv": "",
        "message": msg,
        "free_level": 10,
        "logUID": "414477568",
        "reg_now_days": 0
    }
    response = requests.post(url, json=payload, headers=headers)
    try:
        out = response.json()['sentence']
    except:
        out = response.json()['detail']

    out = re.sub('@[a-zA-Z]{3,}', '،', out)
    out = re.sub(r'[0-9]+', '', out)
    bot.reply_to(message, text = out)
                	
print('تم تشغيل البوت لواسطة : @VlVlVI')              	
bot.infinity_polling()