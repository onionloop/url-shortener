import sqlite3


def init_db():

    conn = sqlite3.connect("shortener.db")
    cursor = conn.cursor()

    sql_query = """CREATE TABLE IF NOT EXISTS URLS(
    
    id INTEGER PRIMARY KEY,
    url TEXT,
    short_code TEXT,
    click_count INTEGER DEFAULT 0
 
    
    );"""

    cursor.execute(sql_query)

    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()