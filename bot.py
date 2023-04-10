import os
import sys
import logging
from aiogram import Bot, Dispatcher, executor
from aiogram.types import Message, CallbackQuery, ContentType
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import markup
import config

storage = MemoryStorage()


class UserInputState(StatesGroup):
    waiting_for_input = State()


class AdminInputState(StatesGroup):
    waiting_for_variable = State()
    waiting_for_input = State()
    waiting_for_conirmation = State()


API_TOKEN = config.token

# configure logging
logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=storage)


@dp.message_handler(commands=['start'])     # Start handler
async def send_welcome(message: Message):
    logger.info(message)
    photo = open('images/photo.jpg', 'rb')
    await message.answer_photo(photo)
    await message.answer(config.start_text_message, reply_markup=markup.markup_main())


@dp.message_handler(commands=['admin'])     # Start admin menu
async def admin(message: Message):
    logger.info(message)
    user_id = message.from_user.id
    logger.info(user_id)
    if user_id == config.admin_id:
        await message.answer('🔑 Вы авторизованы как Админ', reply_markup=markup.markup_admin())
    else:
        await message.answer('🚫 Эта команда доступна только администратору.')


@dp.callback_query_handler(text='setcourse', state=None)       # Start admin set setcourse
async def admin_set_course(callback_query: CallbackQuery):
    if callback_query.from_user.id == config.admin_id:
        await bot.answer_callback_query(callback_query.id)
        await callback_query.message.answer('Пришлите новый курс:')
        await dp.current_state().set_state('admin_set_course')


@dp.message_handler(state='admin_set_course')
async def set_curse(message: Message, state: FSMContext):
    data = await state.get_data()
    variable = data.get('variable')
    # Получаем текущее значение переменной
    current_value = config.course
    # Получаем новое значение переменной
    new_value = message.text.strip()
    # Формируем сообщение об успешном изменении
    conirmation_message = f'Вы изменили значение переменной "{variable}" с\n\n"{current_value}"\n\nна\n\n"{new_value}"'
    # Отправляем сообщение с запросом на подтверждение изменения
    await message.answer(conirmation_message + '\n\nПодтверждаете изменение?',
                         reply_markup=markup.markup_confirmation())
    # Сохраняем новое значение переменной в FSMContext
    await state.update_data(new_value=new_value, variable="course")
    # Меняем состояние на ожидание подтверждения
    await AdminInputState.waiting_for_conirmation.set()


@dp.callback_query_handler(text='setmessage', state=None)       # Start admin set message
async def admin_set_message(callback_query: CallbackQuery):
    if callback_query.from_user.id == config.admin_id:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,
                               'Выберите, какую переменную нужно изменить:',
                               reply_markup=markup.markup_set_message())
        await AdminInputState.waiting_for_variable.set()


@dp.callback_query_handler(text='setbuttons', state=None)       # Start admin set buttons
async def admin_set_message(callback_query: CallbackQuery):
    if callback_query.from_user.id == config.admin_id:
        await bot.answer_callback_query(callback_query.id)
        await bot.send_message(callback_query.from_user.id,
                               'Выберите, какую переменную нужно изменить:',
                               reply_markup=markup.markup_set_buttons())
        await AdminInputState.waiting_for_variable.set()


@dp.callback_query_handler(state=AdminInputState.waiting_for_variable)      # Admin set variable
async def process_callback_kb1btn1(callback_query: CallbackQuery, state: FSMContext):
    variable = callback_query.data
    if variable in ['setcourse', 'setmessage', 'setbuttons', 'setstartimage', 'rebootbot']:
        return
    # Сохраняем выбранную переменную в FSMContext
    await state.update_data(variable=variable)
    # Отправляем сообщение с запросом на новое значение переменной
    await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                message_id=callback_query.message.message_id,
                                text='Введите новое значение для переменной:')
    # Меняем состояние на ожидание нового значения
    await AdminInputState.waiting_for_input.set()


@dp.message_handler(state=AdminInputState.waiting_for_input)
async def set_new_message(message: Message, state: FSMContext):
    # Получаем выбранную переменную из FSMContext
    data = await state.get_data()
    variable = data.get('variable')
    # Получаем текущее значение переменной
    current_value = config.get_text(variable)
    # Получаем новое значение переменной
    new_value = message.text.strip()
    # Формируем сообщение об успешном изменении
    confirmation_message = f'Вы изменили значение переменной "{variable}" с\n\n"{current_value}"\n\nна\n\n"{new_value}"'
    # Отправляем сообщение с запросом на подтверждение изменения
    await message.answer(confirmation_message + '\n\nПодтверждаете изменение?', reply_markup=markup.markup_confirmation())
    # Сохраняем новое значение переменной в FSMContext
    await state.update_data(new_value=new_value)
    # Меняем состояние на ожидание подтверждения
    await AdminInputState.waiting_for_conirmation.set()


@dp.callback_query_handler(text=['confirm', 'cancel'], state=AdminInputState.waiting_for_conirmation)
async def process_conirmation(callback_query: CallbackQuery, state: FSMContext):
    # Получаем выбранную опцию из callback_query.data
    choice = callback_query.data
    logger.info(choice)
    # Получаем сохраненные значения переменной и ее новое значение
    data = await state.get_data()
    new_value = data.get('new_value')
    variable = data.get('variable')
    # Если выбрана опция "Да", сохраняем новое значение переменной
    if choice == 'confirm':
        config.edit_text(variable, new_value)
        config.save()
        setattr(config, variable, new_value)
        config.save()
        # Отправляем сообщение об успешном изменении
        success_message = f'Вы успешно изменили значение переменной "{variable}" на "{new_value}".'
        await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                    message_id=callback_query.message.message_id,
                                    text=success_message)
    # Если выбрана опция "Нет", отменяем изменение переменной
    elif choice == 'cancel':
        cancel_message = f'Вы отменили изменение значения переменной "{variable}".'
        await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                    message_id=callback_query.message.message_id,
                                    text=cancel_message)
    # В любом случае завершаем состояние FSM
    await state.finish()


@dp.callback_query_handler(text='setstartimage', state=None)        # Start admin set image
async def admin_set_start_image(callback_query: CallbackQuery):
    if callback_query.from_user.id == config.admin_id:
        await callback_query.message.answer('Send me a new image to set as start image')
        await dp.current_state().set_state('admin_set_start_image')


@dp.message_handler(content_types=ContentType.PHOTO, state='admin_set_start_image')     # Start admin set image
async def set_start_image(message: Message):
    file_id = message.photo[-1].file_id
    file = await message.bot.get_file(file_id)
    file_path = file.file_path

    # Create the `images` directory if it doesn't exist
    if not os.path.exists('images'):
        os.makedirs('images')

    # Download the file and save it to the `images` directory with a new name
    file_name = f'images/photo.jpg'
    async with message.bot.session.get(f'https://api.telegram.org/file/bot{config.token}/{file_path}') as response:
        with open(file_name, 'wb') as f:
            f.write(await response.content.read())

    await message.answer('Start image has been updated!')
    await dp.current_state().reset_state(with_data=False)


@dp.callback_query_handler(text='reboot')       # Start admin reboot
async def admin_reboot(callback_query: CallbackQuery):
    if callback_query.from_user.id == config.admin_id:
        # выполняем перезапуск бота
        await bot.send_message(callback_query.from_user.id, 'Бот перезапускается...')
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        # отправляем сообщение, если пользователь не является админом
        await bot.answer_callback_query(callback_query.id, text='У вас нет прав на перезапуск бота')


@dp.message_handler(content_types=['text'])     # Nav handler
async def echo(message: Message):
    if message.text.isdigit():
        await message.answer(text=config.price_calculation.format(round(float(config.course) * int(message.text))))
        await message.answer(text=config.ready_to_buy)
    elif message.text == config.start_menu_button_1:
        await message.answer(text=config.start_menu_button_1_text_message.format(config.course))
    elif message.text == config.start_menu_button_2:
        await message.answer(text=config.start_menu_button_2_text_message.format(config.course))
    elif message.text == config.start_menu_button_3:
        await message.answer(text=config.faq_menu_text, reply_markup=markup.markup_faq())

    elif message.text == config.start_menu_button_4:
        await message.answer(text=config.support_text, reply_markup=markup.markup_support())
    elif message.text == config.start_menu_button_5:
        await message.answer(text=config.reviews_text, reply_markup=markup.markup_reviews())
    else:
        await message.answer(text='Ошибка! Нужно отправить число, чтобы мы могли расчитать')


@dp.callback_query_handler(lambda call: call.data, state="*")
async def process_callback_kb1btn1(callback_query: CallbackQuery):
    code = callback_query.data

    if code == 'button1' and callback_query.message.text != config.faq_menu_text_1:
        await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                    message_id=callback_query.message.message_id,
                                    text=config.faq_menu_text_1,
                                    reply_markup=markup.markup_faq())
    elif code == 'button2' and callback_query.message.text != config.faq_menu_text_2:
        await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                    message_id=callback_query.message.message_id,
                                    text=config.faq_menu_text_2,
                                    reply_markup=markup.markup_faq())
    elif code == 'button3' and callback_query.message.text != config.faq_menu_text_3:
        await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                    message_id=callback_query.message.message_id,
                                    text=config.faq_menu_text_3,
                                    reply_markup=markup.markup_faq())
    elif code == 'button4' and callback_query.message.text != config.faq_menu_text_4:
        await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                    message_id=callback_query.message.message_id,
                                    text=config.faq_menu_text_4,
                                    reply_markup=markup.markup_faq())
    elif code == 'button5' and callback_query.message.text != config.faq_menu_text_5:
        await bot.edit_message_text(chat_id=callback_query.from_user.id,
                                    message_id=callback_query.message.message_id,
                                    text=config.faq_menu_text_5,
                                    reply_markup=markup.markup_faq())
    return
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
