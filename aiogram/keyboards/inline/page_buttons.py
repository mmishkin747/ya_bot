from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


page_buttons = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Back page', callback_data='back_page'),
            InlineKeyboardButton(text='Next page', callback_data='next_page'),

        ],
        [
           InlineKeyboardButton(text = 'Close', callback_data='close') 
        ]
    ]
    
    )
