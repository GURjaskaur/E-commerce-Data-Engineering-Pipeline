import pandas as pd
import os

# Define paths
RAW_DATA_PATH = "data/raw/"
PROCESSED_DATA_PATH = "data/processed/"

# Ensure the processed data directory exists
os.makedirs(PROCESSED_DATA_PATH, exist_ok=True)

# Load raw data
users = pd.read_csv(os.path.join(RAW_DATA_PATH, "users.csv"))
products = pd.read_csv(os.path.join(RAW_DATA_PATH, "products.csv"))
transactions = pd.read_csv(os.path.join(RAW_DATA_PATH, "transactions.csv"))

# Data transformation example: Add a 'Total_Price' column to transactions
transactions['Total_Price'] = transactions['Quantity'] * transactions['Product_ID'].map(
    products.set_index('Product_ID')['Price']
)

# Save processed data
users.to_csv(os.path.join(PROCESSED_DATA_PATH, "users_processed.csv"), index=False)
products.to_csv(os.path.join(PROCESSED_DATA_PATH, "products_processed.csv"), index=False)
transactions.to_csv(os.path.join(PROCESSED_DATA_PATH, "transactions_processed.csv"), index=False)

print("ETL process completed. Processed data saved in 'data/processed/' directory.")
