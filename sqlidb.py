import sqlite3

def save_to_sqlite(payload_str):
    conn = sqlite3.connect("sensor_data.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            payload TEXT
        )
    """)
    cursor.execute("INSERT INTO sensor_data (payload) VALUES (?)", (payload_str,))
    conn.commit()
    conn.close()

def show_db():
    conn = sqlite3.connect("sensor_data.db")
    cursor = conn.cursor()
    rows = cursor.execute("""
        SELECT * FROM sensor_data
    """)
    for row in rows:
        print(row)
    conn.commit()
    conn.close()

def test_insert():
    test_payload = '{"type": "temperature", "value": 23.5}'
    save_to_sqlite(test_payload)

def reset_db():
    conn = sqlite3.connect("sensor_data.db")
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS sensor_data")
    conn.commit()
    conn.close()
    print("Database reset")

#test_insert()
#reset_db()
#show_db()