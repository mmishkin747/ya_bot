from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup




create_pl_button = InlineKeyboardMarkup(row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Удалить всё', callback_data='delete_all'),
 
        ],
        [
           InlineKeyboardButton(text = 'Назад', callback_data='close_create_pl') 
        ]
    ]
    


    )
