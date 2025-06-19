import boto3
import pandas as pd
from io import StringIO

# Function to download a file from an S3 bucket and save it locally
# AWS credentials can be provided as parameters or set in the environment variables
# If not provided, boto3 will use the default credentials from the environment or AWS config file
# AWS S3
def load_csv_from_s3(bucket_name="bank-customer-churn-bucket", object_key="raw-bank-customer-churn/BankChurners dataset.csv", download_path="BankChurners dataset.csv", aws_access_key_id=None, aws_secret_access_key=None, region_name=None):
    """
    Download a file from an S3 bucket.

    :param bucket_name: Name of the S3 bucket
    :param object_key: Key of the object to download
    :param download_path: Local path to save the downloaded file
    :param aws_access_key_id: AWS access key ID (optional)
    :param aws_secret_access_key: AWS secret access key (optional)
    :param region_name: AWS region name (optional)
    """
    
    session = boto3.Session(region_name="eu-north-1")
    s3 = session.client("s3")
    response = s3.get_object(Bucket="bank-customer-churn-bucket", Key="raw-bank-customer-churn/BankChurners dataset.csv")
    content = response['Body'].read().decode('utf-8')
    df = pd.read_csv(StringIO(content))    
    return df

# Call the function to download the file

df = load_csv_from_s3("bank-customer-churn-bucket", "raw-bank-customer-churn/BankChurners dataset.csv", "eu-north-1")

# Show data
print(df.head())
print(df.shape)