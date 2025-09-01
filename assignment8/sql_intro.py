import sqlite3 

def add_publisher(cursor, name):
    try:
        cursor.execute("INSERT INTO Publishers (name) VALUES (?)", (name,))
    except sqlite3.IntegrityError:
        print(f"Publisher '{name}' already exists.")

def add_magazine(cursor, name, publisher_id):
    try:
        cursor.execute("INSERT INTO Magazines (name, publisher_id) VALUES (?, ?)", (name, publisher_id))
    except sqlite3.IntegrityError:
        print(f"Magazine '{name} already exists or publisher id is invalid.")

def add_subscriber(cursor, name, address):
    try:
        cursor.execute("INSERT INTO Subscribers (name, address) SELECT ?, ? WHERE NOT EXISTS (SELECT 1 FROM Subscribers WHERE name = ? AND address = ?)", (name, address, name, address))
    except sqlite3.IntegrityError:
        print(f"Subscriber '{name}' at {address}' already exists.")

def add_subscription(cursor, subscriber_id, magazine_id, expiration_date):
    try:
        cursor.execute("""
            INSERT INTO Subscriptions (subscriber_id, magazine_id, expiration_date)
            VALUES (?, ?, ?)
            """, (subscriber_id, magazine_id, expiration_date))
    except sqlite3.IntegrityError:
        print(f"Subscription already exists or invalid foreign keys.")

with sqlite3.connect("../db/magazines.db") as conn:
    print("Database created and connected successfully.")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # create tables
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Publishers (
            publisher_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Magazines (
            magazine_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE,
            publisher_id INTEGER NOT NULL,
            FOREIGN KEY (publisher_id) REFERENCES Publishers(publisher_id)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscribers (
            subscriber_id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            address TEXT NOT NULL,
            UNIQUE(name, address)
        );
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Subscriptions (
            subscription_id INTEGER PRIMARY KEY AUTOINCREMENT,
            subscriber_id INTEGER NOT NULL,
            magazine_id INTEGER NOT NULL,
            expiration_date TEXT NOT NULL,
            FOREIGN KEY (subscriber_id) REFERENCES Subscribers(subscriber_id),
            FOREIGN KEY (magazine_id) REFERENCES Magazines(magazine_id)
        );
    """)
    print("Tables created.")

    add_publisher(cursor, "Jean Kim")
    add_publisher(cursor, "Danny Lee")
    add_publisher(cursor, "Edward woo")

    add_magazine(cursor, "magazine01", 1)
    add_magazine(cursor, "magazine02", 2)
    add_magazine(cursor, "magazine03", 3)

    add_subscriber(cursor, "Alex Wu", "111 main st")
    add_subscriber(cursor, "Soyoung Park", "210-12 northern blvd")
    add_subscriber(cursor, "Chris Wong", "34-12 princes st")

    add_subscription(cursor, 1, 1, "2025-10-30")
    add_subscription(cursor, 2, 2, "2025-12-01")
    add_subscription(cursor, 3, 3, "2026-01-01")

    conn.commit()
    print("Data inserted successfully.")


    # Write SQL Queries
    cursor.execute("SELECT * FROM Subscribers")
    subscribers = cursor.fetchall()
    for subscriber in subscribers:
        print(subscriber)
    
    cursor.execute("SELECT * FROM Magazines ORDER BY name")
    magazines = cursor.fetchall()
    for magazine in magazines:
        print(magazine)
    
    cursor.execute("""
        SELECT Magazines.name, Publishers.name 
        FROM Magazines 
        JOIN Publishers ON Magazines.publisher_id = Publishers.publisher_id
        WHERE Publishers.name = ?
    """, ("Jean kim",))
    publisher_magazines = cursor.fetchall()
    for i in publisher_magazines:
        print(i)

    



    
    