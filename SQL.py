import sqlite3

class MainBase:
    def __init__(self):
        self.database = sqlite3.connect('base.db')
        self.cursor = self.database.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS objects ("
                            "id SERIAL PRIMARY KEY, "
                            "num INTEGER NOT NULL UNIQUE, "
                            "title VARCHAR(100) NOT NULL UNIQUE"
                            ")")
        self.database.commit()

    def add_object(self, num, title):
        self.cursor.execute(f"INSERT INTO objects VALUES ('{num}', {title})")

    def close(self):
        self.close()

    def execute(self, command):
        self.execute(command)

#####################тут тренировачные команды
# db = MainBase()