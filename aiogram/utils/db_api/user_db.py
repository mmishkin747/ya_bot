from datetime import date
from os import name
import sqlite3
from sqlite3.dbapi2 import connect



class Datebase:
    def __init__(self, path_to_dp='data/main.db'):
        self.path_to_db = path_to_dp
        
    @property
    def connection(self):
        return sqlite3.connect(self.path_to_db)

    def execut(self, sql: str, parameters: tuple=None, fetchone=False,
                fetchall= True, commit=False):
        if not parameters:
            parameters = tuple()
        connection = self.connection
        connection.set_trace_callback(logger)
        cursor = connection.cursor()
        date = None
        cursor.execute(sql, parameters)
        if commit:
            connection.commit()
        if fetchone:
            date = cursor.fetchone()
        if fetchall:
            date = cursor.fetchall()
        connection.close()

        return date

    def create_table_users(self):
        sql='''
        CREATE TABLE Users(
            id int NOT NULL,
            Name varchar(255) NOT NULL,
            language_code varchar(10),
            date_add int NOT NULL,
            PRIMARY KEY (id)
        );
        '''
        self.execut(sql, commit=True)
    
    def create_table_playlist(self, name_playlist: str):
        sql = f"""CREATE TABLE {name_playlist}(
            id_track varchar(255) NOT NULL,
            uniq_id varchar(255) NOT NULL,
            name_track varchar(255),
            date_add int NOT NULL,
            PRIMARY KEY (uniq_id)
            );
        """
        self.execut(sql, commit=True)

    def create_table_history(self):
        sql = f"""CREATE TABLE History(
            user_id int NOT NULL,
            id_mes_control int NOT NULL,
            id_mes_track varchar(255) NOT NULL,
            name_playlist varchar(255) NOT NULL,
            page int NOT NULL,
            date_add int NOT NULL,
            PRIMARY KEY (id_mes_control),
            FOREIGN KEY (user_id) REFERENCES Users(id)
            );
        """
        self.execut(sql, commit=True)


    def add_history(self, user_id, id_mes_control, id_mes_track, name_playlist, page):
        date_add = date.today()
        sql = f'INSERT INTO History (user_id, id_mes_control, id_mes_track, name_playlist, page, date_add) VALUES(?, ?, ?, ?, ?, ?)'
        parameters = (user_id, id_mes_control, id_mes_track, name_playlist, page, date_add)
        self.execut(sql, parameters=parameters, commit=True)


    def get_history(self, user_id:int, id_mes_control:int):
        sql = f'SELECT * FROM History WHERE id_mes_control={id_mes_control} and user_id={user_id}'
        return self.execut(sql, fetchall=True)

    
    def del_history(self, user_id:int, id_mes_control:int):
        sql = f'DELETE FROM History WHERE id_mes_control={id_mes_control} and user_id={user_id}'
        return self.execut(sql, commit=True)


    def add_track (self, name_playlist, id_track: str, uniq_id: str,  name_track: str=None):
        date_add = date.today()
        sql = f'INSERT INTO {name_playlist} (id_track, uniq_id, name_track, date_add) VALUES(?, ?, ?, ?)'
        parameters = (id_track, uniq_id, name_track, date_add)
        self.execut(sql, parameters=parameters, commit=True)


    def select_myplaylist(self, user_id):
        name_playlist = f'Playlist_{user_id}'
        sql = f'SELECT id_track FROM {name_playlist}'
        return self.execut(sql, fetchall=True) 


    def count_track_playlist(self, name_playlist):
        return self.execut(f"SELECT COUNT(*) FROM {name_playlist};", fetchone=False)


    def add_user(self, id: int, name: str, language_code: str, date_add: int):
        sql = 'INSERT or IGNORE INTO Users(id, Name, language_code, date_add) VALUES(?, ?, ?, ?)'
        parameters = (id, name, language_code, date_add)
        self.execut(sql, parameters=parameters, commit=True)


    def select_all_users(self):
        sql = 'SELECT * FROM Users'
        return self.execut(sql, fetchall=True)
    
    @staticmethod
    def format_args( sql, parameters: dict):
        sql += " AND ".join([
            f'{item} = ?' for item in parameters
        ])
        return sql , tuple(parameters.values())

    def select_users(self, **kwargs):
        sql = "SELECT * FROM Users WHERE "
        sql, parameters = self.format_args(sql, kwargs)
        return self.execut(sql, parameters, fetchone=True)

    def count_users(self):
        return self.execut("SELECT COUNT(*) FROM Users;", fetchone=False)

    def update_email(self, email, id):
        sql = "UPDATE Users SET email=? WHERE id=?"
        return self.execut(sql, parameters=tuple(email, id), commit=True)

    def delete_users(self):
        return self.execut("DELETE FROM Users WHERE True", commit=True)
    
    def delete_all_tracks(self, name_playlist):
        return self.execut(f'DELETE FROM {name_playlist} WHERE True', commit=True)
    
    def delete_track(self, name_playlist, uniq_id: str):
        return self.execut(f"DELETE FROM {name_playlist} WHERE uniq_id = '{uniq_id}';", commit=True)


def logger(statement):
    print(f'''
    Executing:
    {statement}
    ________________________________________________________________
    ''')

