import pandas as pd
import sys

def convert_xlsx_to_csv(input_file, output_file):
    """
    Converts an Excel file (.xls or .xlsx) to a CSV file.
    
    Args:
        input_file (str): Path to the input Excel file.
        output_file (str): Path to the output CSV file.
    """
    try:
        # Read the Excel file
        data = pd.read_excel(input_file)
        
        # Write to a CSV file
        data.to_csv(output_file, index=False)
        print(f"Successfully converted {input_file} to {output_file}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python xlsx-to-csv.py <input_file> <output_file>")
    else:
        input_file = sys.argv[1]
        output_file = sys.argv[2]
        convert_xlsx_to_csv(input_file, output_file)