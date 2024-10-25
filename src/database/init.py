import sqlite3


def init_db():
    with sqlite3.connect("data.db") as conn:
        cur = conn.cursor()
        with open("./src/database/schema.sql") as in_f:
            sql_init_query = in_f.read()
            cur.executescript(sql_init_query)
