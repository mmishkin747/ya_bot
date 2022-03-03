from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


main_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Мой плейлист', callback_data='my_playlist'), 
            ],
            [
                InlineKeyboardButton(text='Случайно', callback_data='random_tracks')
            ],
            [
                InlineKeyboardButton(text='Хиты', callback_data='top')
            ],
            [
                InlineKeyboardButton(text='Поиск', callback_data='search')
            ],
            [
                InlineKeyboardButton(text='О проекте', callback_data='about')
            ],
                        ]
            )
main_top_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='Топ-100 недели', callback_data='top100weekly'), 
            ],
            [
                InlineKeyboardButton(text='Топ-100 месяца', callback_data='top100mouthly')
            ],
            [
                InlineKeyboardButton(text='По годам', callback_data='top_years')
            ],
            [
                InlineKeyboardButton(text='Назад', callback_data='back_top')
            ]
            ]
            )

main_top_years_kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton(text='2022', callback_data='top100_2022'), 
            ],
            [
                InlineKeyboardButton(text='2021', callback_data='top100_2021'), 
                InlineKeyboardButton(text='2020', callback_data='top100_2020'),
            ],
            [
                InlineKeyboardButton(text='2019', callback_data='top100_2019'), 
                InlineKeyboardButton(text='2018', callback_data='top100_2018'),
            ],
            [
                InlineKeyboardButton(text='2017', callback_data='top100_2017'), 
                InlineKeyboardButton(text='2016', callback_data='top100_2016'),
            ],
            [
                InlineKeyboardButton(text='2015', callback_data='top100_2015'), 
                InlineKeyboardButton(text='2014', callback_data='top100_2014'),
            ],
            [
                InlineKeyboardButton(text='2013', callback_data='top100_2013'), 
                InlineKeyboardButton(text='2012', callback_data='top100_2012'),
            ],
            [
                InlineKeyboardButton(text='2011', callback_data='top100_2011'), 
                InlineKeyboardButton(text='2010', callback_data='top100_2010'),
            ],
            [
                InlineKeyboardButton(text='2009', callback_data='top100_2009'), 
                InlineKeyboardButton(text='2008', callback_data='top100_2008'),
            ],
            [
                InlineKeyboardButton(text='Назад', callback_data='back_years'), 
            ],
 
            ]
            )

