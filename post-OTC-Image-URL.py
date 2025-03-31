import csv
import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# API endpoint and headers
API_URL = os.getenv("API_URL", "http://localhost:3000/v1/post-otc-image")
HEADERS = {
    "Authorization": os.getenv("AUTHORIZATION", ""),
    "Content-Type": "application/json"
}

# Path to the CSV file
CSV_FILE = "OTC-Image-URL.csv"

def post_data_from_csv(csv_file, start_row, end_row):
    """
    Reads data from a CSV file and posts it to the API for the specified row range.

    Args:
        csv_file (str): Path to the CSV file.
        start_row (int): Starting row number (1-based index).
        end_row (int): Ending row number (inclusive, 1-based index).
    """
    try:
        with open(csv_file, mode="r") as file:
            reader = list(csv.DictReader(file))
            for i, row in enumerate(reader, start=1):
                if start_row <= i <= end_row:
                    # Prepare the payload for the API
                    payload = {
                        "ID": row["ID"],
                        "NAME": row["NAME"],
                        "URL": [url.strip() for url in row["URL"].split("|")]  # Split by '|' and strip whitespace
                    }

                    # Make the POST request
                    response = requests.post(API_URL, headers=HEADERS, json=payload)

                    # Print the response
                    if response.status_code == 200:
                        print(f"Row {i} Success: {response.json()}")
                    else:
                        print(f"Row {i} Failed: {response.status_code}, {response.text}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    # Specify the row range to post
    start_row = int(input("Enter the starting row number: "))
    end_row = int(input("Enter the ending row number: "))
    post_data_from_csv(CSV_FILE, start_row, end_row)