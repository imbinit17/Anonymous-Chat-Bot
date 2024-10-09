import sqlite3

def isAuthorised(chat_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    user = cursor.execute(f"SELECT * FROM users WHERE chat_id = '{chat_id}' ").fetchone()
    conn.close()

    if(user != None):
        return True
    else:
        return False
    
def getAllUsers():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    users = cursor.execute("SELECT * FROM users ").fetchall()
    conn.close()

    return users 

def addAuthorisedUser(chat_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"INSERT INTO users (chat_id) VALUES ('{chat_id}')")
    conn.commit()
    conn.close()

def removeAuthorisedUser(chat_id):
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    cursor.execute(f"DELETE FROM users WHERE chat_id = '{chat_id}' ")
    conn.commit()
    conn.close()

    