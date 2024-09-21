import csv

# Step 1: Open the file in read mode
input_file = 'student_marks.csv'
output_file = 'student_Total.csv'
students = []

# Read the data from the input CSV file
with open(input_file, mode='r') as file:
    csv_reader = csv.DictReader(file)

    # Step 2: Create a dictionary
    for row in csv_reader:

        marks = {key: int(value) for key, value in row.items() if key != 'Name'}
        total_marks = sum(marks.values())
        average_marks = total_marks / len(marks)


        student_info = {
            'Name': row['Name'],
            'Total_Marks': total_marks,
            'Average': average_marks
        }

        students.append(student_info)

with open(output_file, mode='w', newline='') as file:
    fieldnames = ['Name', 'Total_Marks', 'Average']
    csv_writer = csv.DictWriter(file, fieldnames=fieldnames)

    csv_writer.writeheader()
    csv_writer.writerows(students)

print(f"Total marks and average marks Upgraded....'{output_file}'.")
