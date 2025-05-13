import os
import re
import csv
from glob import glob

def main():
    input_csv_files = glob("*.csv")
    if not input_csv_files:
        print("No input CSV file found in the current directory.")
        return

    # Assuming the first CSV found is the one to process
    input_tcm_file_path = input_csv_files[0]
    output_csv_file_path = "Test Plan.csv" # Name of the output file

    print(f"Processing input file: {input_tcm_file_path}")
    print(f"Output will be saved to: {output_csv_file_path}")

    # Expected header for the old CSV format
    expected_header_old = ["Test Cases", "TEST CASE ID", "Sample Summary"]
    # Header for the new output CSV
    output_header = ["Test Cases", "Test Schedule", "Assigned Tester", "Date of Execution", "Status", "Bug IDs"]

    input_rows = []
    try:
        with open(input_tcm_file_path, newline="", encoding="utf-8") as infile:
            reader = csv.reader(infile)
            header = next(reader)
            if header != expected_header_old:
                print(f"Input CSV header does not match expected 'old' format.")
                print(f"Expected (Old): {expected_header_old}")
                print(f"Got:            {header}")
                return
            input_rows = list(reader)
    except FileNotFoundError:
        print(f"Error: Input file '{input_tcm_file_path}' not found.")
        return
    except Exception as e:
        print(f"Error reading input CSV: {e}")
        return

    output_rows = [output_header] # Start with the new header

    for row_index, row in enumerate(input_rows):
        if len(row) != 3:
            print(f"Skipping row {row_index + 2} from input: Invalid number of columns. Expected 3, got {len(row)}. Row: {row}")
            continue

        raw_test_case_col = row[0].strip()
        test_case_id_col = row[1].strip()
        sample_summary_col = row[2].strip() # We won't use this directly in the new CSV per your request

        # Determine if it's a category line (old format: ID and Summary are empty)
        is_category_line = not test_case_id_col and not sample_summary_col and raw_test_case_col

        if is_category_line:
            # For category lines, just copy the name to the first column, others empty
            new_row = [raw_test_case_col, "", "", "", "", ""]
            output_rows.append(new_row)
        elif test_case_id_col and raw_test_case_col: # It's a test case line
            # Format the first column as "{TEST CASE ID}: {Test Case Name from old first col}"
            # In the old format, raw_test_case_col IS the descriptive name for test cases
            formatted_test_case_name = f"{test_case_id_col}: {raw_test_case_col}"
            
            # Create the new row with empty strings for the new columns
            new_row = [formatted_test_case_name, "", "", "", "", ""]
            output_rows.append(new_row)
        elif raw_test_case_col or test_case_id_col or sample_summary_col: # Partially filled or malformed
             print(f"Skipping malformed row {row_index + 2} from input: {row}. Expected category or full test case.")


    try:
        with open(output_csv_file_path, mode="w", newline="", encoding="utf-8") as outfile:
            writer = csv.writer(outfile)
            writer.writerows(output_rows)
        print(f"\nSuccessfully created '{output_csv_file_path}' with {len(output_rows) -1} data rows.")
    except Exception as e:
        print(f"Error writing output CSV: {e}")


if __name__ == "__main__":
    main()