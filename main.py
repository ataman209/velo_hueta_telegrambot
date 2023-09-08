import telebot
from telebot import types
import pathlib

bot = telebot.TeleBot('6513093796:AAETmVapmwHOkR0PplRxaUPOlTRI-lCLL2s')

src = None

@bot.message_handler(commands=['start'])
def start(message):
    murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("привіт")
    murkup.add(btn1)
    bot.send_message(message.chat.id,f'Привіт,{message.from_user.first_name}', reply_markup=murkup)

@bot.message_handler(content_types=['photo'])
def hander_file(message):
    global src
    from pathlib import Path
    Path(f'files/{message.chat.id}/').mkdir(parents=True, exist_ok=True)
    if message.content_type == 'photo':
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        downloaded_file = bot.download_file(file_info)
        src = f'files/{message.chat.id}/' + file_info.file_path.replace('photos/',  f'{message.from_user.first_name}')
        with open(src, 'wb') as new_file:
            new_file.write(downloaded_file)
        bot.send_message(message.chat.id,'фото збережено')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

       if message.text == 'привіт':
          murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
          btn1 = types.KeyboardButton('товар в наявності')
          btn2 = types.KeyboardButton('під замовлення')
          btn3 = types.KeyboardButton('викуп')
          btn4 = types.KeyboardButton('мої проекти')
          btn5 = types.KeyboardButton('купити')
          murkup.add(btn1, btn2)
          murkup.add(btn3,btn4)
          murkup.add(btn5)
          bot.send_message(message.chat.id, f'{message.from_user.first_name},оберіть що вас цікавить', reply_markup=murkup)

       elif message.text == 'товар в наявності':
           murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
           btn1 = types.KeyboardButton('купити')
           btn2 = types.KeyboardButton('головне меню')
           murkup.add(btn1, btn2)

           file = open('2023-09-06 16.06.57.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id, 'Перекидка\nShimano XT\nВізуально на 3/5\nПрацює справно\nЦіна- 1400грн')

           file = open('2023-09-06 16.13.42.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id, 'Сидіння Brooks B67 brown\nЦіна- 3540грн ')

           file = open('2023-09-06 16.15.07.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id, 'Сидіння Brooks B17 brown\nЦіна- 3700грн')

           file = open('2023-09-06 16.15.37.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id, 'Сидіння Brooks Cambium C19 black\nЦіна- 4220грн')

           file = open('2023-09-06 16.17.59.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id, 'Гріпси Brooks Cambium Comfort Grips 130mm/130mm Natural\nЦіна- 1000грн ')

           file = open('2023-09-06 16.46.20.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id, 'Ліхтарики Brooks Femto Copper \nПо факту Lizyne. Безтолковий фонарик на батарейках, певне чисто для стилю.\nЦіна- 600грн')

           file = open('2023-09-06 16.21.56.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id,'Продам такий шосер.\n Рама вилка картон, 2х10 трансміся, акісіуми, всі троси кошухи замінені,\n розмір S, свіщонамотана обмотка брукс.\nЦіна 800доларів але готовий до торгу')

           file = open('2023-09-06 16.24.50.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           file = open('2023-09-06 16.25.17.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           file = open('2023-09-06 16.25.38.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           file = open('2023-09-06 16.25.53.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id,'Вело туфлі Five ten, розмір 42, 27 см.\nСтан супер, тільки сліди від шипів.\nБез нюансів.Без шипів\nЦіна- 900 грн')

           file = open('2023-09-06 16.27.30.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           file = open('2023-09-06 16.27.47.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id,'Касета Shimano Ultegra 11s (11-34)\nНепоганий стан. З ланцюгом\nЦіна- 2500грн')

           file = open('2023-09-06 16.29.17.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           file = open('2023-09-06 16.30.03.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id, 'Перекидка і манетка Shimano XT 2s(11s)\nЦіна- 600грн')

           file = open('2023-09-06 16.31.20.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           file = open('2023-09-06 16.31.29.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           file = open('2023-09-06 16.31.38.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id, 'Сідло Selle San Marco Monza 142 мм\nВага: 250 грам\mЦіна- 800 грн')

           file = open('2023-09-06 16.33.39.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           file = open('2023-09-06 16.33.49.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           file = open('2023-09-06 16.34.01.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id, 'Сідло Giant Contact Neutral\nЦіна- 1000 грн')

           file = open('2023-09-06 16.37.06.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id,'Продам втулки Koozer XM390 Ceramic Special Edition\nРозміри: 148x12, 110x15 \nПід ротор на 6 болтів\nHg барабан (10s-11s-12s)\nПроїздили місяць \nЦіна- 2600грн')

           file = open('2023-09-06 16.39.33.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           file = open('2023-09-06 16.39.52.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           file = open('2023-09-06 16.40.07.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id, 'Продам занколан\nГарний стан\nЦіна- 50$',reply_markup=murkup)

       elif message.text == 'під замовлення':
           murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
           btn1 = types.KeyboardButton('замовти')
           btn2 = types.KeyboardButton('головне меню')
           murkup.add(btn1, btn2)

           file = open('2023-09-06 16.53.42.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           file = open('2023-09-06 16.54.15.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id, 'Копмоненти Garbaruk')

           file = open('Trailmech.png', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id, 'Втулки Trailmech')

           file = open('Unknown.png', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id, 'Покришки Panaracer')

           file = open('sigma.png', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id, 'Елeктроніка Sigma sport')

           file = open('Muс-Off.jpeg', 'rb')
           bot.send_photo(message.from_user.id, file)
           file = open('Juice Lubes.jpeg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id, 'Велохімія Muс-Off та Juice Lubes',reply_markup=murkup)

       elif message.text == 'викуп':
           murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
           btn1 = types.KeyboardButton('запропонувати товар')
           btn2 = types.KeyboardButton('головне меню')
           murkup.add(btn1, btn2)
           file = open('2023-09-06 18.59.49.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id, 'Куплю:\nВтулку трекову задню\nБажено чорну\nНа 24 спиці\nПо бюджету: впринципі розгляну всі варіанти',reply_markup=murkup)

       elif message.text == 'мої проекти':
           murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
           btn1 = types.KeyboardButton('головне меню')
           murkup.add(btn1)

           file = open('2023-09-06 20.08.58.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id, 'On One Pompetamine\nЗібрав щось незрозуміле на основі сіті рами\nвпринципі вийшов гарний комютер\nТрансмісія 1х11(Shimano deore)\nКолеса під безкамерку на основі втулок Shimano Deore XT\nПродав бо прросто кататись по місту мені було маловато, хотілось по офроду, а там ширини покришки гревел велосипеда замало для впевненого катання')
           file = open('2023-09-06 20.09.31.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id,'Мій перший серйозний FIXgear проект\nРаму ще давно почав робити @mykolych42 але виріший її продати\n Після першої збірки на компонентах які були\nхотів зібрати щось просте з вигляду але на хорошихкомпонетах\nвпринципі, мені здаєтся в менен це вийшлою\nШатуни Shimano Dura Ace 7600\nВтулки All City Sheriff\nСідло Selle San Marco Aspide\nВинос Zipp\nРуль PRO\nІнші деталі не дуже цікаві тому не буду їх розписувати\nПродав бо трохи змучився від фікса')
           file = open('2023-09-06 20.09.51.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id,'Old MTB Scott montana\nМій поки єдиний олд мтб\nХотів зібрати велосипед дівчині на якому буду виїжати в ліс,\nале моя дівчина не сильнона ньому каталась\nа через слікові покришки по лісу було дуже слизько їздити\nХоча це був чудовий комютер\nТрансмісія 1х11(Shiamano)\nКолеса зібрані на китайських втулка ZTTO і ободах DT swiss\nІнші деталі не дуже цікаві тому не буду їх розписувати\nПродав бо просто стояв в магазині без діла')
           file = open('2023-09-06 20.10.15.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id, 'Сандаль Trail SE\nМій перший дорослий мтб\nДовго йшов до мтб але з цим велосипедом зразу в нього закохався\nСпочатку думав що покатаюсь в стоці але не зміг стриматись\nНе буду поки розписувати по деталях бо якраз їх міняю')
           file = open('2023-09-06 20.07.12.jpg', 'rb')
           bot.send_photo(message.from_user.id, file)
           bot.send_message(message.chat.id,'Новий фікс проект\nРама по факту була почати в той самий час що і моя попередня на тих самих трубах\n але на жаль чи на щастя не була закінчена\nКоли придбав ті труби одразу написав @cryptolipisey і згодом відправив то все йому\nІдея була зробити щось цікаве і унікальне, що Олег зробив\nНа фото зібрана не на моїх деталях\nПоки не маю бажання це швидко збирати,тому буде стояти поки я потроху буду шукати запчастини',reply_markup=murkup)

       elif message.text == 'купити':
           murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
           btn1 = types.KeyboardButton('головне меню')
           murkup.add(btn1)
           bot.send_message(message.chat.id, 'напиши @jgjggdt', reply_markup=murkup)

       elif message.text == 'головне меню':
           murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
           murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
           btn1 = types.KeyboardButton('товар в наявності')
           btn2 = types.KeyboardButton('під замовлення')
           btn3 = types.KeyboardButton('викуп')
           btn4 = types.KeyboardButton('мої проекти')
           btn5 = types.KeyboardButton('купити')
           murkup.add(btn1, btn2)
           murkup.add(btn3, btn4)
           murkup.add(btn5)
           bot.send_message(message.chat.id,'обери щось', reply_markup=murkup)

       elif message.text == 'запропонувати товар':
           murkup = types.ReplyKeyboardMarkup(resize_keyboard=True)
           btn1 = types.KeyboardButton('головне меню')
           murkup.add(btn1)
           bot.send_message(message.chat.id, 'напиши @jgjggdt', reply_markup=murkup)

       elif message.text == 'фото':
           srt = f'files/{message.chat.id}/' + file_info.file_path.replace('photos/', f'{message.from_user.first_name}')
           bot.send_photo(message.chat.id, open(srt, 'rb'))

       #elif message.text == 'видалити':
           #bot.send_photo(message.chat.id, open(src, 'rb'))
           #file = pathlib.Path(f'{src}')
           #file.unlink()




bot.polling(none_stop=True)
