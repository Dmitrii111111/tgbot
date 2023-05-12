import telebot
from telebot import types
import config

token = config.BOT_TOKEN
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f'Добрый день!  {message.from_user.first_name} {message.from_user.last_name}')
    marcap = types.InlineKeyboardMarkup(row_width=2)
    btn1 = types.InlineKeyboardButton('📝Сeo оптимизация',callback_data='ceo')
    btn2 = types.InlineKeyboardButton('📊Аналитика', callback_data='analiyika')
    btn3 = types.InlineKeyboardButton('🚛Отгрузка', callback_data='otgruzka')
    btn4 = types.InlineKeyboardButton('📸Контент',callback_data='kontent')  # эта кнопка будет служить чтобы пользователь смог вписать свою пар валют
    btn5 = types.InlineKeyboardButton('📈Участие в акциях📈', callback_data='otgruzka')
    btn6 = types.InlineKeyboardButton('👩‍🏫мой курс', callback_data='consyltant')
    btn7 = types.InlineKeyboardButton('🤝Консультация по сотрудничеству🤝', callback_data='else')
    marcap.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7 )
    bot.send_message(message.chat.id, 'Выберите подходящию вам категорию', reply_markup=marcap)

@bot.callback_query_handler(func=lambda coll: True)
def collback(coll):
    if coll.data == 'ceo':
        bot.send_message(coll.message.chat.id, '<b>Что включает seo-оптимизация карточки?</b>\n'
                                               '📌<em>Анализ товара</em>\n'
                                               '📌<em>Поиск и сбор всех подходящих под товар ключевых слов, отсев нерелевантных ключевиков</em>\n'
                                               '📌<em>Изменения в характеристиках</em>\n'
                                               '📌<em>Изменения в описании</em>\n'
                                               '<b>Что вы получите на выходе?</b>\n'
                                               '✅ <em>Ваш товар начинает показываться по расширенному количеству ключевых слов</em>\n'
                                               '✅ <em>Вы попадаете в наибольшее кол-во категорий</em>\n'
                                               '✅ <em>Увеличение переходов в товар и каталог бренда</em>\n'
                                               '✅ <em>Увеличение покупаемости</em>\n'
                                               '✅ <em>Видимость товаров в поисковой системе wb</em>\n'
                                               '✅ <em>У вас хорошо настроенная карточка товара</em>', parse_mode="html")
        bot.send_message(coll.message.chat.id, '<b>Ceo одной карточки 1500 ₽</b>',parse_mode="html")
        marcap = types.InlineKeyboardMarkup()
        marcap.add(types.InlineKeyboardButton('Связь со мной',callback_data='else'))
        bot.send_message(coll.message.chat.id, '👇Сотрудничество👇', reply_markup=marcap)

    elif coll.data == 'analiyika':
        bot.send_message(coll.message.chat.id, '<b>Что включает Аналитика?</b>\n'
                                               '✅ <em>Проведу подробнейший анализ ниши!</em>\n'
                                               '✅ <em>Проведу анализ ниши и подбор товара на вход для начинающих селлеров</em>\n'
                                               '✅ <em>Предоставлю детальный анализ конкурентов</em>',parse_mode="html")
        bot.send_message(coll.message.chat.id, '<b>Анализ ниши (одна ниша) 4000 ₽ за услугу</b>',parse_mode="html")
        marcap = types.InlineKeyboardMarkup()
        marcap.add(types.InlineKeyboardButton('Связь со мной', callback_data='else'))
        bot.send_message(coll.message.chat.id, '👇Сотрудничество👇', reply_markup=marcap)

    elif coll.data == 'otgruzka':
        bot.send_message(coll.message.chat.id, '<b>Что включает Отгрузка?</b>\n'
                                               '✅ <em>Формирование поставок на склады марктеплейса Wildberries</em>\n'
                                               '✅ <em>Заказ транспорта для отгрузок на регионы (Деловые линии)</em>\n'
                                               '✅ <em>Отслеживание фактической отгрузки по кабинету, сверка со складом</em>\n'
                                               '✅ <em>Подготовка информации по приемкам для фулфилмента, сверка данных</em>\n'
                                               '✅ <em>Работа с возвратами, самовыкупами (организация отгрузок с ПВЗ на склад фулфилмента)</em>\n'
                                               '✅ <em>Заказ курьеров на доставку комплектующих (упаковка)</em>',parse_mode="html")

        bot.send_message(coll.message.chat.id, '<b>По цене за услугу пишите мне, внизу мои контакты </b>',parse_mode="html")
        marcap = types.InlineKeyboardMarkup()
        marcap.add(types.InlineKeyboardButton('Связь со мной', callback_data='else'))
        bot.send_message(coll.message.chat.id, '👇Сотрудничество👇', reply_markup=marcap)

    elif coll.data == 'kontent':
        bot.send_message(coll.message.chat.id, '<b>Что включает Контент?</b>\n'
                                               '✅ <em>Анализировать графику конкурентов на сайте Wildberries</em>\n'
                                               '✅ <em>Предлагаю новые идеи по улучшению вашей графики</em>\n'
                                               '✅ <em>Пишу ТЗ режиссеру на фотосессию по товарам</em>\n'
                                               '✅ <em>Контролирую работы по оформлению и изменению фотографий карточек товаров</em>\n'
                                               '✅ <em>Проверяю и принимаю работы фрилансеров: фотограф, модель, помощник дизайнера</em>',parse_mode="html")
        bot.send_message(coll.message.chat.id, '<b>По цене за услугу пишите мне, внизу мои контакты </b>',parse_mode="html")
        marcap = types.InlineKeyboardMarkup()
        marcap.add(types.InlineKeyboardButton('Связь со мной', callback_data='else'))
        bot.send_message(coll.message.chat.id, '👇Сотрудничество👇', reply_markup=marcap)

    elif coll.data == 'analiyika':
        bot.send_message(coll.message.chat.id, '<b>Что включает Участие в акциях?</b>\n'
                                               '<em>Расчет цены для участия в акции</em>\n'
                                               '<em>Расчет скидки для участия в акции</em>\n'
                                               '<em>отчет при участии в акции</em>')
        bot.send_message(coll.message.chat.id, '<b>По цене за услугу пишите мне, внизу мои контакты </b>',parse_mode="html")
        marcap = types.InlineKeyboardMarkup()
        marcap.add(types.InlineKeyboardButton('Связь со мной', callback_data='else'))
        bot.send_message(coll.message.chat.id, '👇Сотрудничество👇', reply_markup=marcap)


    elif coll.data == 'consyltant':
        bot.send_message(coll.message.chat.id, '<b>Мой курс "Менеджер Wildberries"</b>\n'
                                               '<u>Онлайн курс "Менеджер Wildberries" очень востребован, ведь его цена весьма доступна для всех, а наполненность не уступает курсам, которые значительно дороже. Так же, при покупке курса "Менеджер вайлдбериз" вы получите:</u>\n'
                                               '📌 чат поддержки, в котором можете задавать любые вопросы, касательно обучения, а так же процесса работы после окончания обучения\n'
                                               '📌 личного куратора, который будет с вами до тех пор, пока вы не устроитесь на должность менеджера Wildberries, а не только на период обучения\n'
                                               '📌 курс в записи. Не нужно подстраивать свой график под спикера, вы сами выбираете темп для учебы\n'
                                               '📌 доступ к курсу навсегда! Не нужно писать конспекты, в любой момент вы сможете открыть лекции и найти интересующую вас тему\n'
                                               '📌 домашние задания, которые будет проверять ваш личный куратор, а так же давать комментарии по теме и полезные советы\n'
                                               '📌 по окончанию курса выдается сертификат',parse_mode="html")
        bot.send_message(coll.message.chat.id, '<b>Цена за курс 10000 ₽</b>',parse_mode="html")
        marcap = types.InlineKeyboardMarkup()
        marcap.add(types.InlineKeyboardButton('Связь со мной для покупки курса', callback_data='svazi'))
        bot.send_message(coll.message.chat.id, '👇Сотрудничество👇', reply_markup=marcap)

    else:
        bot.send_message(coll.message.chat.id, '<b>Mail:</b> Nina432st@mail.ru\n'
                                               '<b>Telegram:</b> @Nina_tsaruic\n'
                                               '<b>WhatsApp:</b> https://wa.me/message/7377PULJS7BKL1',parse_mode="html")

bot.polling(none_stop=True)