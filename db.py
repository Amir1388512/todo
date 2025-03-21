import sqlite3
import json  # Import json module to handle JSON data

class Db:
    def __init__(self, fileName):
        self._db = fileName
        self.connect = sqlite3.connect(fileName)
        self.cursor = self.connect.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS user (
            username TEXT NOT NULL UNIQUE PRIMARY KEY,
            password TEXT NOT NULL,
            todo JSON
        );
        """)

        self.connect.commit()  # Commit the changes to the database
        self.cursor.close()

    def insert_into_db(self, username, password):
        self.connection = sqlite3.connect(self._db)
        self.cursor = self.connection.cursor()

        # Check if the username already exists
        self.cursor.execute('SELECT username FROM user WHERE username = ?', (username,))
        if self.cursor.fetchone() is not None:
            print(f"Username '{username}' already exists. Skipping insertion.")
            raise ValueError
            self.connection.close()
            return

        # If the username doesn't exist, insert the new user
        self.cursor.execute("""
        INSERT INTO user (username, password, todo)
        VALUES (?, ?, ?);
        """, (username, password, json.dumps([])))  # Initialize todo as an empty list
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
        self.cursor.execute('SELECT * FROM user WHERE username = ?', (username,))
        value = self.cursor.fetchone()
        self.connection.close()
        return value

    def remove_user(self, username):
        self.connection = sqlite3.connect(self._db)
        self.cursor = self.connection.cursor()
        self.cursor.execute('DELETE FROM user WHERE username = ?', (username,))
        self.connection.commit()
        self.connection.close()

    def add_todo(self, username, todo):
        self.connection = sqlite3.connect(self._db)
        self.cursor = self.connection.cursor()

        # Fetch the current user data
        self.cursor.execute('SELECT * FROM user WHERE username = ?', (username,))
        user = self.cursor.fetchone()

        if user:
            # Parse the existing todo (if any)
            existing_todo = json.loads(user[2]) if user[2] else []
            # Add the new todo to the list
            existing_todo.append(todo)
            # Convert the updated list back to JSON
            updated_todo = json.dumps(existing_todo)

            # Update the database with the new todo
            self.cursor.execute('UPDATE user SET todo = ? WHERE username = ?', (updated_todo, username))
            self.connection.commit()
            print(f"Todo added for user '{username}'.")
        else:
            print(f"User '{username}' not found.")

        self.connection.close()

    def remove_todo(self, username, todo):
        self.connection = sqlite3.connect(self._db)
        self.cursor = self.connection.cursor()

        # Fetch the current user data
        self.cursor.execute('SELECT * FROM user WHERE username = ?', (username,))
        user = self.cursor.fetchone()

        if user:
            # Parse the existing todo (if any)
            existing_todo = json.loads(user[2]) if user[2] else []
            # Check if the todo exists in the list
            if todo in existing_todo:
                # Remove the todo from the list
                existing_todo.remove(todo)
                # Convert the updated list back to JSON
                updated_todo = json.dumps(existing_todo)

                # Update the database with the modified todo list
                self.cursor.execute('UPDATE user SET todo = ? WHERE username = ?', (updated_todo, username))
                self.connection.commit()
                print(f"Todo '{todo}' removed for user '{username}'.")
            else:
                print(f"Todo '{todo}' not found for user '{username}'.")
        else:
            print(f"User '{username}' not found.")

        self.connection.close()


