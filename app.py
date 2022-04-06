import csv
import http.client

# print("Hello World")
# print("Hello World")
# print("Hello World")
# print("Hello World")

# name = input("What's your name? ")
# age = input("What's your age? ")
# city = input("What city do you live in? ")
# print("Name: " + name + " Age: " + age + " City: " + city)

with open('dailyibmstock.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    print(csv_reader)
    # line_count = 0
    # for row in csv_reader:
    #     print(row)
    #     line_count += 1
    # print(f'Processed {line_count} lines.')

connection = http.client.HTTPSConnection("https://test-project-d14cc-default-rtdb.firebaseio.com/private.json")
connection.request("GET", "/")
response = connection.getresponse()
print("Status: {} and reason: {}".format(response.status, response.reason))

connection.close()