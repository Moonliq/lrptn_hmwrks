from emoji import emojize
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from random import randint, choice
from glob import glob
import settings
from ephem import *
import ephem
from datetime import date, datetime, timedelta
print(datetime.now())
logging.basicConfig(filename='bot.log', level=logging.INFO)

def main():
    mybot = Updater(settings.API_KEY, use_context=True)
    
    db = mybot.dispatcher
    db.add_handler(CommandHandler("start", greet_user))
    db.add_handler(CommandHandler("guess", guess_number))
    db.add_handler(CommandHandler("cat", send_cat_picture))
    db.add_handler(CommandHandler("planet", astro_user))
    db.add_handler(CommandHandler("wordcount", word_user))
    db.add_handler(CommandHandler("next_full_moon", moon_user))
    db.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    logging.info('Bot started')
    mybot.start_polling()
    mybot.idle()

def greet_user(update, context):
    print('Start pushed')
    context.user_data['emoji'] = get_smile(context.user_data)
    update.message.reply_text(f"Здравствуй, пользователь {context.user_data['emoji']}!")

def get_smile(user_data):
    if 'emoji' not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data['emoji']

def play_random_numbers(user_number):
    bot_number = randint(user_number-10, user_number+10)
    if user_number > bot_number:
        message = f"Ты загадал {user_number}, я загадал {bot_number}, ты выиграл!"
    elif user_number == bot_number:
        message = f"Ты загадал {user_number}, я загадал {bot_number}, ничья!"
    else:
        message = f"Ты загадал {user_number}, я загадал {bot_number}, я выиграл!"
    return message

def guess_number(update, context):
    print('Guess pushed')
    print(context.args)
    if context.args:
        try:
            user_number =int(context.args[0])
            message = play_random_numbers(user_number)
        except (TypeError, ValueError):
            message = 'Введите целое число'
    else:
        message = 'Введите число'
    update.message.reply_text(message)

def astro_user(update, context):
    print('Astro entrance')
    dt_now = datetime.now()
    user_txt = update.message.text.lower().split()
    if context.args[0].lower() == 'mars':
        m = ephem.Mars(dt_now.strftime("%Y/%m/%d"))
        update.message.reply_text(f'Сегодня {dt_now.strftime("%Y/%m/%d")} Марс в созвездии {ephem.constellation(m)[-1]}')
    elif context.args[0].lower() == 'neptune':
        m = ephem.Neptune(dt_now.strftime("%Y/%m/%d"))
        update.message.reply_text(f'Сегодня Нептун в созвездии {ephem.constellation(m)[-1]}')
    elif context.args[0].lower() == 'mercury':
        m = ephem.Mercury(dt_now.strftime("%Y/%m/%d"))
        update.message.reply_text(f'Сегодня Меркурий в созвездии {ephem.constellation(m)[-1]}')
    elif context.args[0].lower() == 'venus':
        m = ephem.Venus(dt_now.strftime("%Y/%m/%d"))
        update.message.reply_text(f'Сегодня Венера в созвездии {ephem.constellation(m)[-1]}')
    elif context.args[0].lower() == 'moon':
        m = ephem.Moon(dt_now.strftime("%Y/%m/%d"))
        update.message.reply_text(f'Сегодня Луна в созвездии {ephem.constellation(m)[-1]}')
    elif context.args[0].lower() == 'jupiter':
        m = ephem.Jupiter(dt_now.strftime("%Y/%m/%d"))
        update.message.reply_text(f'Сегодня Юпитер в созвездии {ephem.constellation(m)[-1]}')
    elif context.args[0].lower() == 'saturn':
        m = ephem.Saturn(dt_now.strftime("%Y/%m/%d"))
        update.message.reply_text(f'Сегодня Сатурн в созвездии {ephem.constellation(m)[-1]}')
    elif context.args[0].lower() == 'uranus':
        m = ephem.Uranus(dt_now.strftime("%Y/%m/%d"))
        update.message.reply_text(f'Сегодня Уран в созвездии {ephem.constellation(m)[-1]}')  
    else:
        update.message.reply_text(f'Корректная команда /planet *en название планеты*') 

def talk_to_me(update, context):
    context.user_data['emoji'] = get_smile(context.user_data)
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(f'{user_text} {context.user_data["emoji"]}')

def send_cat_picture(update, context):
    print('Cat pushed')
    cat_photos_list = glob('images/cat*.jp*g')
    cat_pic_filename = choice(cat_photos_list)
    chat_id = update.effective_chat.id
    context.bot.send_photo(chat_id=chat_id, photo=open(cat_pic_filename, 'rb'))

def moon_user(update, context):
    print('Moon entrance')
    # x = context.args[0].split('-')
    # if len(x[0]) != 4 or len(x[1]) != 2 or len(x[2]) != 2:
    #     update.message.reply_text(f'Ошибка! Корректная команда /next_full_moon YYYY-MM-DD') 
    # elif isinstance(int(x[0]), int) and isinstance(int(x[1]), int) and isinstance(int(x[2]), int):
    #     print('YES')
    # else:

    date_string = context.args[0].replace('-', '/')
    date_dt = datetime.strptime(date_string, '%Y/%m/%d')
    update.message.reply_text(f'Ближайшее полнолуние {ephem.next_full_moon(date_dt.strftime("%Y/%m/%d"))}')

def word_user(update, context):
    print('Word entrance')
    words = context.args
    if len(words) == 0:
        update.message.reply_text(f'Нужно ввести текст')
    else:
        update.message.reply_text(f'Количество слов = {len(words)}')


if __name__ == "__main__":
    main()
