from aiogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup
import config
from config import get_text


def markup_faq():
    inline_btn_1 = InlineKeyboardButton(text=config.faq_menu_button_1, callback_data='button1')
    inline_btn_2 = InlineKeyboardButton(text=config.faq_menu_button_2, callback_data='button2')
    inline_btn_3 = InlineKeyboardButton(text=config.faq_menu_button_3, callback_data='button3')
    inline_btn_4 = InlineKeyboardButton(text=config.faq_menu_button_4, callback_data='button4')
    inline_btn_5 = InlineKeyboardButton(text=config.faq_menu_button_5, callback_data='button5')

    inline_kb1 = InlineKeyboardMarkup().row(inline_btn_1).row(inline_btn_2).row(inline_btn_3).row(inline_btn_4)\
        .row(inline_btn_5)
    return inline_kb1


def markup_main():
    kb = [
            [
                KeyboardButton(text=config.start_menu_button_1),
                KeyboardButton(text=config.start_menu_button_2)
            ],
            [
                KeyboardButton(text=config.start_menu_button_3),
                KeyboardButton(text=config.start_menu_button_4)
            ],
            [
                KeyboardButton(text=config.start_menu_button_5)
            ],
        ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True,
    )
    return keyboard


def markup_admin():
    markup = InlineKeyboardMarkup(row_width=1)
    item1 = InlineKeyboardButton("Изменить курс", callback_data='setcourse')
    item2 = InlineKeyboardButton("Изменить текст", callback_data='setmessage')
    item3 = InlineKeyboardButton("Изменить кнопку", callback_data='setbuttons')
    item4 = InlineKeyboardButton("Изменить стартовую картинку", callback_data='setstartimage')
    item5 = InlineKeyboardButton("Перезапустить бота", callback_data='rebootbot')
    markup.add(item1, item2, item3, item4, item5)
    return markup


def markup_set_buttons():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton(get_text('start_menu_button_1')[0:25] + '..'
                             if len(get_text('start_menu_button_1')) > 18
                             else get_text('start_menu_button_1'),
                             callback_data='start_menu_button_1'),

        InlineKeyboardButton(get_text('start_menu_button_2')[0:25] + '..'
                             if len(get_text('start_menu_button_2')) > 18
                             else get_text('start_menu_button_2'),
                             callback_data='start_menu_button_2'),

        InlineKeyboardButton(get_text('start_menu_button_3')[0:25] + '..'
                             if len(get_text('start_menu_button_3')) > 18
                             else get_text('start_menu_button_3'),
                             callback_data='start_menu_button_3'),

        InlineKeyboardButton(get_text('start_menu_button_4')[0:25] + '..'
                             if len(get_text('start_menu_button_4')) > 18
                             else get_text('start_menu_button_4'),
                             callback_data='start_menu_button_4'),

        InlineKeyboardButton(get_text('start_menu_button_5')[0:25] + '..'
                             if len(get_text('start_menu_button_5')) > 18
                             else get_text('start_menu_button_5'),
                             callback_data='start_menu_button_5'),

        InlineKeyboardButton(get_text('faq_menu_text')[:25] + '..'
                             if len(get_text('faq_menu_text')) > 18
                             else get_text('faq_menu_text'),
                             callback_data='faq_menu_text'),

        InlineKeyboardButton(get_text('faq_menu_button_1')[0:25] + '..'
                             if len(get_text('faq_menu_button_1')) > 18
                             else get_text('faq_menu_button_1'),
                             callback_data='faq_menu_button_1'),

        InlineKeyboardButton(get_text('faq_menu_button_2')[:25] + '..'
                             if len(get_text('faq_menu_button_2')) > 18
                             else get_text('faq_menu_button_2'),
                             callback_data='faq_menu_button_2'),

        InlineKeyboardButton(get_text('faq_menu_button_3')[:25] + '..'
                             if len(get_text('faq_menu_button_3')) > 18
                             else get_text('faq_menu_button_3'),
                             callback_data='faq_menu_button_3'),

        InlineKeyboardButton(get_text('faq_menu_button_4')[:25] + '..'
                             if len(get_text('faq_menu_button_4')) > 18
                             else get_text('faq_menu_button_4'),
                             callback_data='faq_menu_button_4'),

        InlineKeyboardButton(get_text('faq_menu_button_5')[:25] + '..'
                             if len(get_text('faq_menu_button_5')) > 18
                             else get_text('faq_menu_button_5'),
                             callback_data='faq_menu_button_5'),
    )
    return keyboard


def markup_set_message():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton('Стартовое сообщение' + '- ' + (get_text('start_text_message')[0:70] + '..'
                             if len(get_text('start_text_message')) > 18
                             else get_text('start_text_message')),
                             callback_data='start_text_message'),

        InlineKeyboardButton(config.start_menu_button_1 + '- ' + (get_text('start_menu_button_1_text_message')[0:70] +
                             '..' if len(get_text('start_menu_button_1_text_message')) > 70
                             else get_text('start_menu_button_1_text_message')),
                             callback_data='start_menu_button_1_text_message'),

        InlineKeyboardButton(config.start_menu_button_2 + '- ' + (get_text('start_menu_button_2_text_message')[0:70] +
                             '..' if len(get_text('start_menu_button_2_text_message')) > 70
                             else get_text('start_menu_button_2_text_message')),
                             callback_data='start_menu_button_2_text_message'),

        InlineKeyboardButton('Сообщение после расчёта' + '- ' + (get_text('ready_to_buy')[0:70] +
                             '..' if len(
                             get_text('ready_to_buy')) > 70
                             else get_text('ready_to_buy')),
                             callback_data='ready_to_buy'),

        InlineKeyboardButton('Сообщение расчёта' + '- ' + (get_text('price_calculation')[0:70] +
                             '..' if len(
                             get_text('price_calculation')) > 70
                             else get_text('price_calculation')),
                             callback_data='price_calculation'),

        InlineKeyboardButton(config.faq_menu_button_1 + '- ' + (get_text('faq_menu_text_1')[:70] + '..'
                             if len(get_text('faq_menu_text_1')) > 70
                             else get_text('faq_menu_text_1')),
                             callback_data='faq_menu_text_1'),

        InlineKeyboardButton(config.faq_menu_button_2 + '- ' + (get_text('faq_menu_text_2')[:70] + '..'
                             if len(get_text('faq_menu_text_2')) > 70
                             else get_text('faq_menu_text_2')),
                             callback_data='faq_menu_text_2'),

        InlineKeyboardButton(config.faq_menu_button_3 + '- ' + (get_text('faq_menu_text_3')[:70] + '..'
                             if len(get_text('faq_menu_text_3')) > 70
                             else get_text('faq_menu_text_3')),
                             callback_data='faq_menu_text_3'),

        InlineKeyboardButton(config.faq_menu_button_4 + '- ' + (get_text('faq_menu_text_4')[:70] + '..'
                             if len(get_text('faq_menu_text_4')) > 70
                             else get_text('faq_menu_text_4')),
                             callback_data='faq_menu_text_4'),

        InlineKeyboardButton(config.faq_menu_button_5 + '- ' + (get_text('faq_menu_text_5')[:70] + '..'
                             if len(get_text('faq_menu_text_5')) > 70
                             else get_text('faq_menu_text_5')),
                             callback_data='faq_menu_text_5'),

        InlineKeyboardButton(config.reviews_text + '- ' + (get_text('reviews')[:70] + '..'
                             if len('reviews') > 70
                             else get_text('reviews')),
                             callback_data='reviews')
    )
    return keyboard


def markup_confirmation():
    keyboard = InlineKeyboardMarkup(row_width=2)
    keyboard.add(
        InlineKeyboardButton('Да', callback_data='confirm'),
        InlineKeyboardButton('Нет', callback_data='cancel'),
    )
    return keyboard


def markup_reviews():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
            InlineKeyboardButton(text='Отзывы', url=config.reviews)
    )
    return keyboard


def markup_support():
    keyboard = InlineKeyboardMarkup(row_width=1)
    keyboard.add(
        InlineKeyboardButton(text='Обратиться в поддержку', url=config.support_url)
    )
    return keyboard
