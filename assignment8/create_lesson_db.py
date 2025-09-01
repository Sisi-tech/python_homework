import sqlite3

def create_and_populate_db():
    conn = sqlite3.connect("../db/lesson.db")
    cursor = conn.cursor()

    # Enable foreign key constraints
    cursor.execute("PRAGMA foreign_keys = ON;")

    # Drop tables if they exist (for clean rerun)
    cursor.execute("DROP TABLE IF EXISTS line_items;")
    cursor.execute("DROP TABLE IF EXISTS products;")

    # Create products table
    cursor.execute("""
    CREATE TABLE products (
        product_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_name TEXT NOT NULL UNIQUE,
        price REAL NOT NULL
    );
    """)

    # Create line_items table
    cursor.execute("""
    CREATE TABLE line_items (
        line_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        product_id INTEGER NOT NULL,
        product_name TEXT NOT NULL,
        quantity INTEGER NOT NULL,
        FOREIGN KEY (product_id) REFERENCES products(product_id)
    );
    """)

    # Insert sample products
    products = [
        ("Widget", 9.99),
        ("Gadget", 19.99),
        ("Doodad", 4.99)
    ]
    cursor.executemany("INSERT INTO products (product_name, price) VALUES (?, ?);", products)

    # Insert sample line_items
    line_items = [
        (1, "Widget", 3),
        (2, "Gadget", 1),
        (3, "Doodad", 7),
        (1, "Widget", 2)
    ]
    cursor.executemany("INSERT INTO line_items (product_id, product_name, quantity) VALUES (?, ?, ?);", line_items)

    conn.commit()
    conn.close()
    print("lesson.db created and populated successfully!")

if __name__ == "__main__":
    create_and_populate_db()
