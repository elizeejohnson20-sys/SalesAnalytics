
import pandas as pd

# Load the Superstore dataset
df = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1",
    parse_dates=["Order Date", "Ship Date"]
)

# Display the first 5 rows
print("FIRST 5 ROWS:")
print(df.head())

# Display all column names
print("\nCOLUMN NAMES:")
print(df.columns.tolist())

# Display dataset information
print("\nDATASET INFORMATION:")
print(df.info())

# Display number of rows and columns
print("\nDATASET SHAPE:")
print(df.shape)

# Check for duplicate rows
print("\nDUPLICATE ROWS:")
print(df.duplicated().sum())

# Basic business metrics
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
total_orders = df["Order ID"].nunique()
average_order_value = total_sales / total_orders

print("\n--- BUSINESS METRICS ---")
print("Total Sales:", round(total_sales, 2))
print("Total Profit:", round(total_profit, 2))
print("Total Quantity Sold:", total_quantity)
print("Total Orders:", total_orders)
print("Average Order Value:", round(average_order_value, 2))
# Category analysis
category_analysis = df.groupby("Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).sort_values("Sales", ascending=False)

print("\n--- CATEGORY ANALYSIS ---")
print(category_analysis.round(2).to_string())
# Calculate profit margin by category
category_analysis["Profit Margin (%)"] = (
    category_analysis["Profit"] / category_analysis["Sales"]
) * 100

print("\n--- CATEGORY PROFIT MARGIN ---")
print(category_analysis[["Sales", "Profit", "Profit Margin (%)"]].round(2).to_string())
# Sub-category analysis
subcategory_analysis = df.groupby("Sub-Category").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Quantity=("Quantity", "sum")
).sort_values("Profit")

print("\n--- SUB-CATEGORY ANALYSIS ---")
print(subcategory_analysis.round(2).to_string())
# Analyze discount impact
discount_analysis = df.groupby("Sub-Category").agg(
    Average_Discount=("Discount", "mean"),
    Total_Sales=("Sales", "sum"),
    Total_Profit=("Profit", "sum")
).sort_values("Average_Discount", ascending=False)

print("\n--- DISCOUNT ANALYSIS ---")
print(discount_analysis.round(3).to_string())
# Analyze relationship between discount and profit
discount_profit_correlation = df["Discount"].corr(df["Profit"])

print("\n--- DISCOUNT VS PROFIT ---")
print("Correlation between Discount and Profit:",
      round(discount_profit_correlation, 3))