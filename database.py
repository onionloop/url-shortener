import sqlite3


def init_db():

    conn = sqlite3.connect("shortener.db")
    cursor = conn.cursor()

    sql_query = """CREATE TABLE IF NOT EXISTS URLS(
    
    id INTEGER PRIMARY KEY,
    url TEXT,
    short_code TEXT UNIQUE,
    click_count INTEGER DEFAULT 0
 
    
    );"""

    cursor.execute(sql_query)

    conn.commit()
    conn.close()

def save_url(original_url , short_code):
    conn = sqlite3.connect("shortener.db")
    cursor = conn.cursor()

    cursor.execute("INSERT INTO urls (url, short_code) VALUES(?, ?)", (original_url, short_code))

    conn.commit()
    conn.close()

def get_url(short_code):
    
    
    with sqlite3.connect('shortener.db') as conn:
    
    
        cursor = conn.cursor()

        
        cursor.execute("SELECT url from urls WHERE short_code = ?", (short_code,))

        result = cursor.fetchone()

        if result:
            cursor.execute("UPDATE urls SET click_count = click_count + 1 WHERE short_code = ?", (short_code,))
            return result
        
        return None
    
def get_stats(short_code):

    with sqlite3.connect("shortener.db") as conn:
        cursor = conn.cursor()

        cursor.execute("SELECT url, click_count from urls WHERE short_code = ?", (short_code,))
        result = cursor.fetchone()

        if result:
            return result
        
        


if __name__ == "__main__":
    init_db()