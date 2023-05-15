import sqlite3

class Database:
    def __init__(self, db_name):
        self.db_name = db_name
        self.con = sqlite3.connect(db_name)
        self.cur = self.con.cursor()

    def create_database(self):
        self.cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT,
            email TEXT, 
            password TEXT, 
            register_date TEXT #в sqlite3 нету тип данных DATA поэтому TEXT написал
            )''')

    def select_database(self):
        data = self.cur.execute('SELECT * FROM users')
        list = []
        for i in data.fetchall():
            list.append({'id': i[0], 'username': i[1], 'email': i[2], 'register_date': i[4]})
        return list







