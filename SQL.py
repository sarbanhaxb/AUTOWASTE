import sqlite3

class DataBase:
    def __init__(self):
        self.database = sqlite3.connect('base.db')
        self.cursor = self.database.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS objects ("
                            "id INTEGER PRIMARY KEY, "
                            "num VARCHAR(100) NOT NULL, "
                            "title VARCHAR(100) NOT NULL"
                            ")")
        self.database.commit()

    def insertObject(self, num, title):
        self.cursor.execute(f"INSERT INTO objects (num, title) VALUES (?, ?)", (num, title))
        self.database.commit()

    def close(self):
        self.close()

    def getObjectNum(self, id):
        return self.cursor.execute(f"SELECT num FROM objects WHERE id={id}").fetchall()[0][0]

    def getObjectTitle(self, id):
        return self.cursor.execute(f"SELECT title FROM objects WHERE id={id}").fetchall()[0][0]

    def update_object(self, num, title, id):
        self.cursor.execute("UPDATE objects SET num=?, title=? WHERE id=?", (num, title, id))


    def deletePosition(self, id):
        self.cursor.execute("DELETE FROM objects WHERE id=?", (id, ))

    def DBcommit(self):
        self.database.commit()

#################тут тренировачные команды
# db = DataBase()
# db.cursor.execute("DROP TABLE objects")