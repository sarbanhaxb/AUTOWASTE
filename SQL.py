import sqlite3

class DataBase:
    def __init__(self):
        self.database = sqlite3.connect('base.db')
        self.cursor = self.database.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS objects ("
                            "id SERIAL PRIMARY KEY, "
                            "num VARCHAR(100) NOT NULL UNIQUE, "
                            "title VARCHAR(100) NOT NULL UNIQUE"
                            ")")
        self.database.commit()

    def insertObject(self, num, title):
        self.cursor.execute(f"INSERT INTO objects (num, title) VALUES (?, ?)", (num, title))
        self.database.commit()

    def close(self):
        self.close()

    def execute(self, command):
        self.cursor.execute(command)

#####################тут тренировачные команды
db = DataBase()

db.execute("DROP TABLE objects")
# db.execute("DELETE FROM objects")