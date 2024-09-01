import pandas as pd
import os

# Define paths
PROCESSED_DATA_PATH = "data/processed/"
REPORTS_PATH = "reports/"

# Ensure the reports directory exists
os.makedirs(REPORTS_PATH, exist_ok=True)

# Load processed data
users = pd.read_csv(os.path.join(PROCESSED_DATA_PATH, "users_processed.csv"))
products = pd.read_csv(os.path.join(PROCESSED_DATA_PATH, "products_processed.csv"))
transactions = pd.read_csv(os.path.join(PROCESSED_DATA_PATH, "transactions_processed.csv"))

# Example analysis: Total revenue by product category
revenue_by_category = transactions.merge(products, on='Product_ID').groupby('Category')['Total_Price'].sum()

# Save analysis as HTML report
report_path = os.path.join(REPORTS_PATH, "analysis_report.html")
with open(report_path, 'w') as f:
    f.write("<h1>Revenue by Product Category</h1>\n")
    f.write(revenue_by_category.to_frame().to_html())

print(f"Analysis completed. Report saved as '{report_path}'.")
