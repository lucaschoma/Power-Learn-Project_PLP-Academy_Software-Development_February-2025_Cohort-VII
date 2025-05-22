# assignment.py

import pandas as pd
import matplotlib.pyplot as plt

# 1. Load Data
df = pd.read_csv("sales_data.csv")  # Make sure the CSV is in the same folder

# 2. Explore Data
print("=== First 5 Rows of the Dataset ===")
print(df.head())

print("\n=== Dataset Info ===")
print(df.info())

print("\n=== Summary Statistics ===")
print(df.describe())

# 3. Basic Analysis
total_revenue = df["Revenue ($)"].sum()
best_seller = df.groupby("Product")["Quantity Sold"].sum().idxmax()
top_day = df.groupby("Date")["Revenue ($)"].sum().idxmax()

print("\n=== Basic Analysis ===")
print(f"Total Revenue: ${total_revenue}")
print(f"Best-Selling Product: {best_seller}")
print(f"Day with Highest Revenue: {top_day}")

# 4. Visualizations
# Revenue over time
plt.figure(figsize=(8, 5))
df.groupby("Date")["Revenue ($)"].sum().plot(kind="line", marker='o')
plt.title("Revenue Over Time")
plt.xlabel("Date")
plt.ylabel("Revenue ($)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("revenue_over_time.png")
plt.show()

# Quantity Sold by Product
plt.figure(figsize=(6, 4))
df.groupby("Product")["Quantity Sold"].sum().plot(kind="bar", color="skyblue")
plt.title("Total Quantity Sold by Product")
plt.xlabel("Product")
plt.ylabel("Quantity Sold")
plt.tight_layout()
plt.savefig("quantity_by_product.png")
plt.show()

# 5. Observations
print("\n=== Observations ===")
print("- Widget A is the best-selling product.")
print("- The day with highest sales was likely due to a high sale of Widget A.")
print("- Sales are spread over three days and appear to increase on the final day.")
