import pandas as pd
from src.download_data import load_csv_from_s3

# Load the data using the function
df = load_csv_from_s3(
    bucket_name="bank-customer-churn-bucket",
    object_key="raw-bank-customer-churn/BankChurners dataset.csv",
    region_name="eu-north-1"
)

# 👇 Example: Show column names
print("Columns in dataset:")
print(df.columns.tolist())
