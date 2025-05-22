import pandas as pd

# Create sample sales data
sample_data = {
    "Date": ["2025-05-20", "2025-05-20", "2025-05-21", "2025-05-22", "2025-05-22"],
    "Product": ["Widget A", "Widget B", "Widget A", "Widget C", "Widget A"],
    "Quantity Sold": [10, 5, 20, 15, 25],
    "Revenue ($)": [100, 50, 200, 150, 250]
}

# Save to CSV
df_sample = pd.DataFrame(sample_data)
df_sample.to_csv("sales_data.csv", index=False)

import pandas as pd

# Load the CSV file
df = pd.read_csv("sales_data.csv")

# Calculate the total revenue
total_revenue = df["Revenue ($)"].sum()

# Find the best-selling product (based on Quantity Sold)
best_selling_product = df.groupby("Product")["Quantity Sold"].sum().idxmax()

# Identify the day with the highest total revenue
day_with_highest_sales = df.groupby("Date")["Revenue ($)"].sum().idxmax()

# Prepare summary text
summary = f"""
Sales Summary Report
====================
Total Revenue: ${total_revenue:.2f}
Best-Selling Product: {best_selling_product}
Day with Highest Sales: {day_with_highest_sales}
"""

# Save the summary to a text file
with open("sales_summary.txt", "w") as f:
    f.write(summary.strip())

# Print insights
print(summary)

