from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


pg_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Предыдущая страница', callback_data='back_page'),
            InlineKeyboardButton(text='Следующая страница', callback_data='next_page'),

        ],
        [
           InlineKeyboardButton(text = 'Закрыть', callback_data='close') 
        ]
    ]
    
    )
pg_button_mp = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Предыдущая страница', callback_data='back_page_mp'),
            InlineKeyboardButton(text='Следующая страница', callback_data='next_page_mp'),

        ],
        [
           InlineKeyboardButton(text = 'Редактировать плейлист', callback_data='create_playlist') 
        ],
        [
           InlineKeyboardButton(text = 'Закрыть', callback_data='close') 
        ]
    ]
    )

pg_button_close = InlineKeyboardMarkup(
    inline_keyboard=[
        
        [
           InlineKeyboardButton(text = 'Закрыть', callback_data='close') 
        ]
    ]
    
    )
