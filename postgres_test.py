import get_db, psycopg2 as p
from get_db import getdb

class MyDatabase():

    def __init__(self, cred):
        self.conn = p.connect(cred)
        self.cur = self.conn.cursor()

    def query(self, query):
        self.cur.execute(query)

    def close(self):
        self.cur.close()
        self.conn.close()

db = MyDatabase()
db.query("""SELECT * FROM sierra_view.circ_trans LIMIT 10""")
db.close()


def db_init():
    db = getdb()
    conn = p.connect(db)

    cur = conn.cursor()
    cur.execute("""SELECT * FROM sierra_view.circ_trans LIMIT 10""")
    rows = cur.fetchall()
    return rows