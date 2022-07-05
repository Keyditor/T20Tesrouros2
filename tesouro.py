import sqlite3


class Search:
    def __init__(self, nd, dado):
        self.nd = nd
        self.db = sqlite3.connect('T20.db')
        self.cursor = self.db.cursor()
        self.dado = dado

        self.cursor.execute(f'SELECT * FROM Tesouro WHERE nd = "{self.nd}" AND {self.dado} >= DDMIN And {self.dado} <= DDmax')

        result = self.cursor.fetchall()
        self.result = result.__str__().replace("[(","")
        self.result = self.result.replace(")]", "")
#        self.result = self.result.replace(" ", "")
        #print(self.result)
        self.result = self.result.split(", ")
#        self.result = self.result.replace(" ", "")
        #print(self.result)
        self.dinheiro = self.result[4]
        self.item = self.result[7]
