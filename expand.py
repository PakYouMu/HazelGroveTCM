import os
import re
import csv
from glob import glob

def main():
    rows = []
    # Assuming your CSV file is named 'test_cases.csv' in the same directory
    # or is the only CSV file present.
    csv_files = glob("*.csv")
    if not csv_files:
        print("No CSV file found in the current directory.")
        return
    
    # Use the first CSV file found
    tcm_file_path = csv_files[0] 
    print(f"Processing file: {tcm_file_path}")

    with open(tcm_file_path, newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        header = next(reader) # Skip header row
        assert header == ["Test Cases", "TEST CASE ID", "Sample Summary"], "CSV header does not match expected format."
        rows = list(reader)

    SNAKECASE = re.compile(r"[^\w.]+")  # Keep dots for filenames if desired, otherwise remove
    SAFE_PATH = re.compile(r"[^a-zA-Z0-9\s\-_]") # Allow alphanumeric, space, hyphen, underscore for paths

    readme_lines = []
    readme_lines.append("# Visita Test Case Management") # Updated project name
    readme_lines.append(
        "> Web-based Store and Product Management Test Case Repository  \n\n" # Updated description
    )
    readme_lines.append("## Test Cases  \n\n")

    current_main_category = ""
    # No sub-categories in the new CSV structure, so path will be simpler

    for row_index, row in enumerate(rows):
        if len(row) != 3:
            print(f"Skipping row {row_index + 2}: Invalid number of columns. Expected 3, got {len(row)}. Row: {row}")
            continue

        category_or_test_case_name = row[0].strip()
        test_case_id = row[1].strip()
        test_case_summary = row[2].strip()

        # This row defines a main category
        if not test_case_id and not test_case_summary and category_or_test_case_name:
            current_main_category = SAFE_PATH.sub("", category_or_test_case_name).replace(" ", "-")
            if not os.path.exists(current_main_category):
                os.makedirs(current_main_category)
            readme_lines.append(f" * [{category_or_test_case_name}](<./{current_main_category}>)  ")
            print(f"Created directory: {current_main_category}")
            continue
        
        # This row defines a test case
        elif test_case_id and test_case_summary and category_or_test_case_name:
            if not current_main_category:
                print(f"Skipping test case '{category_or_test_case_name}' as no main category is set.")
                continue

            # Sanitize test case name for filename
            # Allow alphanumeric, underscore, hyphen. Replace other non-word chars with underscore.
            sanitized_tc_name = re.sub(r'[^\w\s-]', '', category_or_test_case_name).strip()
            filename_tc_part = SNAKECASE.sub("_", sanitized_tc_name.lower())
            
            filepath = f"{current_main_category}/{test_case_id}_{filename_tc_part}.md"
            
            # Normalize path separators for OS compatibility
            filepath = os.path.normpath(filepath)


            if os.path.exists(filepath):
                print(f"Skipping existing file: {filepath}")
                # Still add to README if it wasn't there before (e.g. manual creation)
                # For simplicity, we'll assume if file exists, README entry was also created.
                # If you want to ensure README is always up-to-date, you'd read existing README
                # and only add if not present. This script focuses on creation.
                readme_lines.append(
                    f"   * [{test_case_id}: {category_or_test_case_name}](<./{filepath}>)  "
                )
                continue
            
            # Add to README
            # Indentation for test cases under their category
            readme_lines.append(
                f"   * [{test_case_id}: {category_or_test_case_name}](<./{filepath}>)  "
            )
            print(f"Creating file: {filepath}")

            contents = (
                f"## **{test_case_id}:** {category_or_test_case_name}  \n\n"
                f"> **Summary:** {test_case_summary}  <br>\n\n"
                f"**Preconditions:** \n\n" # Changed "None" to a section
                f"- _Precondition 1_ \n"
                f"- _Precondition 2_ \n\n"
                f"**Test Steps:** \n\n" # Changed "Scenario 1" to "Test Steps"
                f"| \# | Step Description | Expected Result   | \n" # Renamed columns
                f"|----|------------------|-------------------| \n"
                f"| 1  |                  |                   | \n"
                f"| 2  |                  |                   | \n"
                f"| 3  |                  |                   |  \n\n"
                f"**Post-conditions:**  \n\n"
                f"- _Post-condition 1_ \n"
                f"- _Post-condition 2_ \n"
            )

            with open(filepath, "w", encoding="utf-8") as file: # Changed "w+" to "w"
                file.write(contents)
        
        elif category_or_test_case_name or test_case_id or test_case_summary: # Handle partially filled rows or malformed data
            print(f"Skipping malformed row {row_index + 2}: {row}. Expected either a category (col 1 filled, others empty) or a test case (all 3 cols filled).")


    with open("README.md", "w", encoding="utf-8") as file: # Changed "w+" to "w"
        file.write("\n".join(readme_lines))
    print("\nREADME.md updated.")

if __name__ == "__main__":
    main()