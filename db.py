import sqlite3

from gevent.time import sleep


class Db:
    def __init__(self, fileName):

        self._db = fileName

        self.connect = sqlite3.connect(fileName)
        self.cursor = self.connect.cursor()

        self.cursor.execute("""
        
        CREATE TABLE IF NOT EXISTS user (
            username TEXT NOT NULL UNIQUE PRIMARY KEY
            password TEXT NOT NULL
            todo JSON
        
            );
        """)

        self.cursor.close()

    def insert_into_db(self, username , password):
        self.connection = sqlite3.connect(self._db)
        self.cursor = self.connection.cursor()
        self.cursor.execute("""
        INSERT INTO user (username, password)
        VALUES (?, ?);
        """, (username, password))
        self.connection.commit()
        self.connection.close()


    def see_data(self):
        self.connection = sqlite3.connect(self._db)
        self.cursor = self.connection.cursor()
        self.cursor.execute('SELECT * FROM user')
        value = self.cursor.fetchall()
        self.connection.close()
        return value

    def select_user(self, username):
        self.connection = sqlite3.connect(self._db)
        self.cursor = self.connection.cursor()
        self.cursor.execute('SELECT * FROM user WHERE username = ?', (username, ))
        value = self.cursor.fetchone()
        self.connection.close()
        return value

    def remove_user(self, username):
        self.connection = sqlite3.connect(self._db)
        self.cursor = self.connection.cursor()
        self.cursor.execute('DELETE FROM user WHERE username = ?', (username,))
        self.connection.commit()
        self.connection.close()



