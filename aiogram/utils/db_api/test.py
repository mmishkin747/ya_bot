from user_db import Datebase

db = Datebase()

def test():
    

    users = db.count_users()
    
    print(f'Добавлено пользователей: {users=}')

test()