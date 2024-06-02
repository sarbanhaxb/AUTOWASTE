import sqlite3
import pandas as pd


class DataBase:
    def __init__(self):
        self.database = sqlite3.connect('base.db')
        self.cursor = self.database.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS objects ("
                            "id INTEGER PRIMARY KEY, "
                            "num VARCHAR(100) NOT NULL, "
                            "title VARCHAR(100) NOT NULL"
                            ")")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS object("
                            "id INTEGER PRIMARY KEY,"
                            "id_object INTEGER,"
                            "codeFKKO VARCHAR(30),"
                            "wasteTitle VARCHAR(300),"
                            "quantity FLOAT,"
                            "FOREIGN KEY (id_object) REFERENCES objects(id)" 
                            ")")
        self.database.commit()
        if not self.cursor.execute("SELECT EXISTS(SELECT 1 FROM sqlite_master WHERE type='table' AND name='fkko');").fetchone()[0]:
            self.createFKKO()

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

    def getFKKO(self) -> list:
        return self.cursor.execute("SELECT * FROM fkko").fetchall()

    def createFKKO(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS fkko ("
                            "id INTEGER PRIMARY KEY, "
                            "num VARCHAR(30) NOT NULL, "
                            "title VARCHAR(300) NOT NULL"
                            ")")

        BDO = pd.read_excel("https://rpn.gov.ru/upload/iblock/22b/6kwwkka1n6d2r4yznwz2dqqlhlzrxy60/bank_dannykh_ob_otkhodakh-_3_.xlsx", skiprows=3)
        for row in BDO.itertuples():
            self.cursor.execute(f"INSERT INTO fkko (num, title) VALUES (?, ?)", (str(row[1]), str(row[2])))
            self.database.commit()


#################тут тренировачные команды
db = DataBase()
db.cursor.execute("DROP TABLE fkko")
