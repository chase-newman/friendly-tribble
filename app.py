import csv

# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")

# name = input("What's your name? ")
# age = input("What's your age? ")
# city = input("What city do you live in? ")
# print("Name: " + name + " Age: " + age + " City: " + city)

with open('employees.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)
    line_count = 0
    for row in csv_reader:
        print(row)
        # if line_count == 0:
        #     print(f'Column names are {", ".join(row)}')
        #     line_count += 1
        # else:
        #     print("Not Applicable")
        #     line_count += 1
    print(f'Processed {line_count} lines.')