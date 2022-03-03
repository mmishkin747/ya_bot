
from aiogram import types
from loader import dp
from aiogram.dispatcher.storage import FSMContext
from keyboards.inline import close_search_kb, back_search_kb
from states.state_search import Search_state
from search import search_scraping


@dp.callback_query_handler(lambda c: c.data=='search')
async def search_start(call: types.CallbackQuery):
        await call.message.answer(text='Что ищем?', reply_markup=close_search_kb)
        await Search_state.search_state_1.set()


@dp.message_handler(state=Search_state.search_state_1, content_types=types.ContentTypes.TEXT)
async def search_get_list(message: types.Message, state: FSMContext):
    search_text = message.text
    search_ls = search_scraping.get_search(search_text=search_text)
    text=str()
    search_dt=dict()
    number=1
    for track in search_ls:
        text+= f'{number}. {track[0]} - {track[1]}\n'
        search_dt[number] = track[2]
        number+=1

    await state.update_data(search_dt)
    await message.answer(text=text)
    await message.answer(text='Введи номер трека или нажми "Назад" что бы повторить поиск', reply_markup=back_search_kb)
    await Search_state.search_state_2.set()


@dp.message_handler(state=Search_state.search_state_2, content_types=types.ContentTypes.TEXT)
async def search_get_track(message: types.Message, state: FSMContext):
    try:
        number = int(message.text)
        search_dt = await state.get_data()
        audio = search_scraping.get_search_track(url=search_dt[number])
        await message.answer_audio(audio=audio, title="название трека")
        await message.answer(text='Введи номер трека или нажми "Назад" что бы повторить поиск', reply_markup=back_search_kb)
    except Exception as err:
        await message.answer(text='Отправь число! Например: 1')


@dp.callback_query_handler(lambda c: c.data=='back_search', state='*')
async def back_search(call: types.CallbackQuery):
    await search_start(call=call)
 


@dp.callback_query_handler(lambda c: c.data=='close_search', state='*')
async def close_search(call: types.CallbackQuery, state: FSMContext): 
    await state.reset_state()
    await call.message.answer(text='Поиск закрыт. Главное меню /main')





