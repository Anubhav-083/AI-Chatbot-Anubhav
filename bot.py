import sqlite3

def get_bot_response(user_input):
    user_input = user_input.lower()
    if "hello" in user_input:
        return "Hi there! How can I help you today?"
    elif "help" in user_input:
        return "Sure, I'm here to help. Tell me more."
    else:
        return "Sorry, I didn't understand that. Can you rephrase?"

def log_message(user_input, bot_response):
    conn = sqlite3.connect("chat_logs.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS chat_log 
                      (user_input TEXT, bot_response TEXT)""")
    cursor.execute("INSERT INTO chat_log (user_input, bot_response) VALUES (?, ?)", (user_input, bot_response))
    conn.commit()
    conn.close()
