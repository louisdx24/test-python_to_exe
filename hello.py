import os
import csv

# Get the desktop path for the current user
desktop = os.path.join(os.path.expanduser("~"), "Desktop")

# Define the file path for the CSV file
file_path = os.path.join(desktop, "hello.csv")

# Write 'hello' to the CSV file
with open(file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['hello'])

print(f"CSV file created at: {file_path}")
