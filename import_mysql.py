import pandas as pd
import mysql.connector

# Read CSV
df = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1"
)

# Convert dates correctly
df["Order Date"] = pd.to_datetime(df["Order Date"], format="%m/%d/%Y")
df["Ship Date"] = pd.to_datetime(df["Ship Date"], format="%m/%d/%Y")

# Connect to MySQL
conn = mysql.connector.connect(
    host="localhost",
    port=3306,
    user="root",
    password="Elizabeth@20",
    database="salesanalyticsdb"
)

cursor = conn.cursor()

# Clear old data
cursor.execute("TRUNCATE TABLE sales")

# Insert data
query = """
INSERT INTO sales (
    row_id, order_id, order_date, ship_date, ship_mode,
    customer_id, customer_name, segment, country, city, state,
    postal_code, region, product_id, category, sub_category,
    product_name, sales, quantity, discount, profit
)
VALUES (
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,
    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
)
"""

for _, row in df.iterrows():
    cursor.execute(query, (
        int(row["Row ID"]),
        row["Order ID"],
        row["Order Date"].date(),
        row["Ship Date"].date(),
        row["Ship Mode"],
        row["Customer ID"],
        row["Customer Name"],
        row["Segment"],
        row["Country"],
        row["City"],
        row["State"],
        int(row["Postal Code"]),
        row["Region"],
        row["Product ID"],
        row["Category"],
        row["Sub-Category"],
        row["Product Name"],
        float(row["Sales"]),
        int(row["Quantity"]),
        float(row["Discount"]),
        float(row["Profit"])
    ))

conn.commit()

print("Data imported successfully!")
print("Rows imported:", len(df))

cursor.close()
conn.close()