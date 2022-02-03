from aiogram import types
from aiogram.dispatcher import FSMContext
from states import Top100_state
from loader import dp
import logging

# Эхо хендлер, куда летят текстовые сообщения без указанного состояния
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"Эхо без состояния."
                         f"Сообщение:\n"
                         f"{message.text}")


# Эхо хендлер, куда летят ВСЕ сообщения с указанным состоянием
#@dp.message_handler(state="*", content_types=types.ContentTypes.ANY)
async def bot_echo_all(message: types.Message, state: FSMContext):
    state = await state.get_state()
    await message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{message}</code>")

# Для тестирования и анализы
#@dp.callback_query_handler(lambda c: c.data=='next_page', state=Top100_state.top100_st)
async def bot_echo_all_call(call: types.CallbackQuery, state: FSMContext):
    state = await state.get_state()
    await call.message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{call}</code>"
                         f"\n"
                         f"<code>{call.message}</code>")
    logging.info(call)


# Для тестирования и анализы
#@dp.callback_query_handler(lambda c: c.data=='back_page', state=Top100_state.top100_st)
async def bot_echo_all_call(call: types.CallbackQuery, state: FSMContext):
    state = await state.get_state()
    await call.message.answer(f"Эхо в состоянии <code>{state}</code>.\n"
                         f"\nСодержание сообщения:\n"
                         f"<code>{call}</code>"
                         f"\n"
                         f"<code>{call.message}</code>")
    logging.info(call)
