
import pandas as pd

# Load the Superstore dataset
df = pd.read_csv(
    "data/Sample - Superstore.csv",
    encoding="latin1",
    parse_dates=["Order Date", "Ship Date"]
)

df.to_csv("data/Superstore_Cleaned.csv", index=False)
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

      # REGIONAL ANALYSIS

region_analysis = df.groupby("Region").agg({
    "Sales": "sum",
    "Profit": "sum",
    "Quantity": "sum"
}).sort_values("Sales", ascending=False)

print("\n--- REGIONAL ANALYSIS ---")
print(region_analysis.round(2))
# MONTHLY SALES TREND

df["YearMonth"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("YearMonth").agg({
    "Sales": "sum",
    "Profit": "sum"
})

print("\n--- MONTHLY SALES TREND ---")
print(monthly_sales.round(2))
# MONTHLY SALES CHART

import matplotlib.pyplot as plt

monthly_sales["Sales"].plot(kind="line", figsize=(12, 6))

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("images/monthly_sales_trend.png")
plt.show()
# TOP 10 PRODUCTS BY PROFIT

top_products = df.groupby("Product Name").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).sort_values("Profit", ascending=False).head(10)

print("\n--- TOP 10 PRODUCTS BY PROFIT ---")
print(top_products.round(2).to_string())
# TOP 10 LOSS-MAKING PRODUCTS

loss_products = df.groupby("Product Name").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum")
).sort_values("Profit").head(10)

print("\n--- TOP 10 LOSS-MAKING PRODUCTS ---")
print(loss_products.round(2).to_string())

# CUSTOMER ANALYSIS

customer_analysis = df.groupby("Customer Name").agg(
    Sales=("Sales", "sum"),
    Profit=("Profit", "sum"),
    Orders=("Order ID", "nunique")
).sort_values("Sales", ascending=False).head(10)

print("\n--- TOP 10 CUSTOMERS BY SALES ---")
print(customer_analysis.round(2).to_string())

import matplotlib.pyplot as plt

# 1. Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8, 5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("visuals/sales_by_category.png")
plt.close()


# 2. Profit by Category
category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8, 5))
category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.tight_layout()
plt.savefig("visuals/profit_by_category.png")
plt.close()


# 3. Monthly Sales Trend
monthly_sales = df.groupby("YearMonth")["Sales"].sum()

plt.figure(figsize=(12, 5))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals/monthly_sales_trend.png")
plt.close()


# 4. Regional Sales
region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")
plt.title("Sales by Region")
plt.xlabel("Region")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("visuals/sales_by_region.png")
plt.close()


print("\nVISUALIZATIONS CREATED SUCCESSFULLY")