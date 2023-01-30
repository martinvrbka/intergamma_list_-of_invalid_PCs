import csv

def extract_invalid_ips(file1, file2, output_file):
    # Load data from first file into a dictionary
    valid_ips = {}
    with open(file1, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        for row in reader:
            valid_ips[row[0]] = row[1]

    # Write rows from second file to output file if corresponding IP is invalid
    with open(file2, 'r') as f, open(output_file, 'w') as out:
        reader = csv.reader(f)
        header = next(reader)
        writer = csv.writer(out)
        writer.writerow(header)  # write header to output file
        for row in reader:
            if row[header.index("IP Address")] in valid_ips and valid_ips[row[header.index("IP Address")]] == "invalid":
                writer.writerow(row)

# Example usage
extract_invalid_ips("file1.csv", "file2.csv", "output.csv")