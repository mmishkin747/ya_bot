from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


close_search_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Закрыть поиск', callback_data='close_search'), 
            ],
            ]
            )



back_search_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Назад', callback_data='back_search'), 
            ],
            [
                InlineKeyboardButton(text='Закрыть поиск', callback_data='close_search'), 
            ]
                        ]
            )

