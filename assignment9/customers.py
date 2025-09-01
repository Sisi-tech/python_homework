import sqlite3 

def setup_customers():
    conn = sqlite3.connect("../db/lesson.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS customers (
            customer_id INTEGER PRIMARY KEY,
            customer_name TEXT
        );
    """)

    cursor.execute("SELECT COUNT(*) FROM customers;")
    if cursor.fetchall()[0] == 0:
        cursor.executemany(
            "INSERT OR IGNORE INTO customers(customer_id, customer_name) VALUES (?, ?);",
            [(101, 'Alx'), (102, 'Danny'), (103, 'Chris'), (104, 'Ally'), (105, 'Debbie')]
        )

    conn.commit()
    conn.close()

setup_customers()
