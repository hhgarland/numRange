import csv

def read_numbers_from_csv(file_path):
    """Reads numbers from a CSV file and returns a list of them."""
    numbers = []
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            numbers.append(int(row[0]))  # Assuming one column with integers
    return numbers

def write_numbers_to_csv(numbers, output_file):
    """Writes a list of numbers to a CSV file."""
    with open(output_file, 'w', newline='') as file:
        writer = csv.writer(file)
        for number in numbers:
            writer.writerow([number])

def find_missing_numbers(full_range, given_range):
    """Finds numbers in the full range that are missing from the given range."""
    start, end = full_range
    full_set = set(range(start, end + 1))  # Full range of numbers
    given_set = set(given_range)           # Numbers provided from CSV
    missing_numbers = sorted(full_set - given_set)
    return missing_numbers

# Main script
input_csv = 'numbers.csv'  # Replace with the actual input CSV file
output_csv = 'missing_numbers.csv'  # Output CSV file for missing numbers

# Define the full range (8000 to 8999)
full_range = (8000, 8999)

# Read numbers from the input CSV
given_numbers = read_numbers_from_csv(input_csv)

# Find the missing numbers
missing_numbers = find_missing_numbers(full_range, given_numbers)

# Write the missing numbers to the output CSV
write_numbers_to_csv(missing_numbers, output_csv)

print(f"Missing numbers have been written to {output_csv}")

