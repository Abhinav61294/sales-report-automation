import pandas as pd
import matplotlib.pyplot as plt
# Load dataset
df = pd.read_csv("input/sales_data.csv")

# Display first 5 rows
print("\nFirst 5 Rows:\n")
print(df.head())

# Clean missing values
df = df.dropna()

# Total sales
total_sales = df["Total Revenue"].sum()

# Total orders
total_orders = len(df)

# Top-selling product category
top_category = (
    df.groupby("Product Category")["Total Revenue"]
    .sum()
    .idxmax()
)

# Region with highest sales
top_region = (
    df.groupby("Region")["Total Revenue"]
    .sum()
    .idxmax()
)

# Monthly sales summary
df["Date"] = pd.to_datetime(df["Date"])

df["Month"] = df["Date"].dt.strftime("%Y-%m")

monthly_sales = (
    df.groupby("Month")["Total Revenue"]
    .sum()
)

# Print business insights
print("\n===== SALES SUMMARY =====")

print(f"\nTotal Sales: {total_sales}")

print(f"\nTotal Orders: {total_orders}")

print(f"\nTop Product Category: {top_category}")

print(f"\nTop Region: {top_region}")

print("\nMonthly Sales:\n")
print(monthly_sales)

# Create figure
plt.figure(figsize=(10, 5))

# Create monthly sales chart
monthly_sales.plot(kind="bar")

# Chart title and labels
plt.title("Monthly Sales Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue")

# Rotate month labels
plt.xticks(rotation=45)

# Adjust layout
plt.tight_layout()

# Save chart
plt.savefig("charts/monthly_sales.png")

# Close figure
plt.close()

print("\nChart saved successfully.")

# Create summary dataframe
summary_data = {
    "Metric": [
        "Total Sales",
        "Total Orders",
        "Top Product Category",
        "Top Region"
    ],
    "Value": [
        total_sales,
        total_orders,
        top_category,
        top_region
    ]
}

summary_df = pd.DataFrame(summary_data)

# Export to Excel
with pd.ExcelWriter("output/final_report.xlsx") as writer:
    summary_df.to_excel(writer, sheet_name="Summary", index=False)
    monthly_sales.to_excel(writer, sheet_name="Monthly Sales")

print("\nExcel report exported successfully.")