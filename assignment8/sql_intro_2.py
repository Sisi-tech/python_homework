import pandas as pd
import sqlite3 

conn = sqlite3.connect("../db/lesson.db")

query = """
SELECT 
    line_items.line_item_id,
    line_items.quantity,
    line_items.product_id,
    line_items.product_name,
    products.price
FROM line_items
JOIN products ON line_items.product_id = products.product_id
"""

df = pd.read_sql_query(query, conn)
print(df.head())

df['total'] = df['quantity'] * df['price']
print(df.head())

summary = df.groupby('product_id').agg({
    'line_item_id': 'count',
    'total': 'sum',
    'product_name': 'first'
}).rename(columns={
    'line_item_id': 'order_count',
    'total': 'total_price'
})

summary = summary.sort_values(by='product_name')
print(summary.head())

summary.to_csv("order_summary.csv")
print("saved to csv file")
