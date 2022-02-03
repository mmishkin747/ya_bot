from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Мой плейлист', callback_data='my_playlist'), 
            ],
            [
                InlineKeyboardButton(text='Новинки', callback_data='new_track')
            ],
            [
                InlineKeyboardButton(text='Хиты', callback_data='top100')
            ],
            [
                InlineKeyboardButton(text='Потборки', callback_data='hit_playlist')
            ],
            [
                InlineKeyboardButton(text='Поиск', callback_data='search')
            ],
            [
                InlineKeyboardButton(text='О проекте', callback_data='about')
            ],
            [
                InlineKeyboardButton(text='Test', callback_data='test')
            ]
                        ]
            )
