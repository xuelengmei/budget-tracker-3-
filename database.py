import sqlite3

def init_db():
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS records (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user TEXT,
            date TEXT,
            type TEXT,
            category TEXT,
            amount REAL,
            note TEXT
        )
    ''')
    c.execute('''
         CREATE TABLE IF NOT EXISTS users (
             username TEXT PRIMARY KEY,
             password TEXT
         )
     ''')
    conn.commit()
    conn.close()

def add_record(user, date, type_, category, amount, note):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute('INSERT INTO records (user, date, type, category, amount, note) VALUES (?, ?, ?, ?, ?, ?)',
              (user, date, type_, category, amount, note))
    conn.commit()
    conn.close()

def get_user_records(user):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute('SELECT date, type, category, amount, note FROM records WHERE user = ?', (user,))
    data = c.fetchall()
    conn.close()
    return data

def clear_user_records(user):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute('DELETE FROM records WHERE user = ?', (user,))
    conn.commit()
    conn.close()

def register_user(username, password):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    try:
        c.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except sqlite3.IntegrityError:
        return False 
    finally:
        conn.close()

def validate_login(username, password):
    conn = sqlite3.connect("data.db")
    c = conn.cursor()
    c.execute("SELECT * FROM users WHERE username = ? AND password = ?", (username, password))
    result = c.fetchone()
    conn.close()
    return result is not None
