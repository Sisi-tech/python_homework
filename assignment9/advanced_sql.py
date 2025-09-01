import pandas as pd
import sqlite3

def main():
    conn = sqlite3.connect("../db/lesson.db")
    conn.execute("PRAGMA foreign_keys = 1")
    cursor = conn.cursor()

    # Task 1
    query = """
        SELECT o.order_id, SUM(p.price * l.quantity) AS total_price 
        FROM orders o
        JOIN line_items l ON o.order_id = l.order_id 
        JOIN products p ON l.product_id = p.product_id 
        GROUP BY o.order_id 
        ORDER BY o.order_id
        LIMIT 5;
        """
    
    cursor.execute(query)
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Task 2
    task2_query = """
        SELECT c.customer_name, AVG(order_totals.total_price) AS average_total_price 
        FROM customers c 
        LEFT JOIN (
            SELECT o.customer_id AS customer_id_b, SUM(p.price * l.quantity) AS total_price 
            FROM orders o
            JOIN line_items l ON o.order_id = l.order_id 
            JOIN products p ON l.product_id = p.product_id 
            GROUP BY o.order_id 
        ) AS order_totals 
        ON c.customer_id = order_totals.customer_id_b
        GROUP BY c.customer_name;
    """
    cursor.execute(task2_query)
    task2 = cursor.fetchall()
    for result in task2:
        print(result)
    
    # Task 3 
    cursor.execute("SELECT customer_id FROM customers WHERE customer_name = 'Perez and Sons';")
    row = cursor.fetchone()
    if row is None:
        print("Customer 'Perez and Sons' not found!")
        return
    customer_id = row[0]

    cursor.execute("SELECT employee_id FROM employees WHERE employee_name = 'Miranda Harris';")
    row = cursor.fetchone()
    if row is None:
        print("Employee 'Miranda Harris' not found!")
        return
    employee_id = row[0]

    cursor.execute("SELECT product_id FROM products ORDER BY price ASC LIMIT 5")
    product_ids = [row[0] for row in cursor.fetchall()]

    try:
        conn.execute("BEGIN")  

        cursor.execute("""
            INSERT INTO orders(customer_id, employee_id, order_date)
            VALUES (?, ?, DATE('now'))
            RETURNING order_id;
        """, (customer_id, employee_id))
        order_id = cursor.fetchone()[0]

        cursor.executemany("""
            INSERT INTO line_items(order_id, product_id, quantity)
            VALUES (?, ?, ?);
        """, [(order_id, pid, 10) for pid in product_ids])

        conn.commit()  
        print(f"Order {order_id} and line items inserted successfully.")

    except sqlite3.Error as e:
        conn.rollback()
        print("Transaction failed:", e)

    cursor.execute("""
        SELECT l.line_item_id, l.quantity, p.product_name
        FROM line_items l
        JOIN products p ON l.product_id = p.product_id
        WHERE l.order_id = ?
    """, (order_id,))

    for row in cursor.fetchall():
        print(row)
    
    # task 4
    task4_query = """
    SELECT e.employee_id, e.first_name, e.last_name, COUNT(o.order_id) AS order_count
    FROM employees e
    JOIN orders o ON e.employee_id = o.employee_id
    GROUP BY e.employee_id
    HAVING COUNT(o.order_id) > 5;
    """

    cursor.execute(task4_query)
    task4 = cursor.fetchall()

    print("Employees with more than 5 orders:")
    for row in task4:
        print(f"ID: {row[0]}, Name: {row[1]} {row[2]}, Orders: {row[3]}")


    conn.close()

if __name__ == "__main__":
    main()
