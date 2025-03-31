import csv
import requests

# API endpoint and headers
API_URL = "http://localhost:3000/v1/post-otc-image"
HEADERS = {
    "Authorization": "Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJsb2dpblJlc3VsdCI6eyJzdGF0dXMiOnRydWUsIm1lc3NhZ2UiOiJSZXF1ZXN0IFByb2Nlc3NlZCBTdWNjZXNzZnVsbHkiLCJyZXNwb25zZSI6eyJNT0JJTEUiOiIxMjM0NTY3ODkwIiwiQ0lUWSI6Ik5ldyBZb3JrIiwiRk5BTUUiOiJLYXJ0aWtleSIsIkRPQiI6IjE5OTItMDMtMTUiLCJDVVNUT01FUl9JRCI6IjE3NjI3MTQ0NjdDIiwiR0VOREVSIjoiRmVtYWxlIiwiTE5BTUUiOiJHdXB0YSIsIkVQT0NIIjoxNzM4NzkxMTIyMTMzLCJFTUFJTCI6IlAwYWxpY2Uuam9obnNvbkBnbWFpbC5jb20ifX0sImlhdCI6MTczODc5MTIxM30.g8uap3VaJmogWMo4v1me4iD3BZnHd1EIcnNs3s0OsE0Fy_5BL9KAxPwYmKKU1GL6hA8N-Z71w6U7DttZDyVNzHE_B5iflj__xL5XA0EZVoXxEd4Y53mfGYo1hTpgvNt7jaVChlJx72u4zFE95AqcUxplZXLGY4iIDGg7accMyjOU5JM2pLz1rOJzMyMn5s42HiK5iErFHx_tXVGYCMvP1jJ6JQkDtI8Rf_bQHzTA4-QnmIYxY1pzPQ_a3R31_-rIWF3A6INC12uEedKFnroJq0Ugx1IaIWbJohbxBhGEbRik2h1LxPnq8g-n2tM1cADWNxDKA5G-xQ9SBSGt2KGEXHV8h7cDW8IF4honP3hzcYnxj2YN-YRgpAMBEoIyZANzDbi8B3TZ64GrK1ZDoNcp1GtS4Tl31xjn2KltK9p7FFYhvGbrnzYZwpLdbhuf7RoqyOl4qpz0s1jwC1g8U02sfSvQmaqAHYRHwStSs_I4H-nRZJZjFG67eQ9lyYtjvByK",
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