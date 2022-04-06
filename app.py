import csv
import http.client
import json

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


connection = http.client.HTTPSConnection("test-project-d14cc-default-rtdb.firebaseio.com")
connection.request("GET", "/private.json")
response = connection.getresponse()
print(response.headers)
data = response.read()
print("Status: {} and reason: {}".format(response.status, response.reason))

print(data)

connection.close()




conn = http.client.HTTPSConnection('test-project-d14cc-default-rtdb.firebaseio.com')

headers = {'Content-type': 'application/json'}

foo = {'text': 'Hello HTTP #1 **cool**, and #1!'}
json_data = json.dumps(foo)

conn.request('POST', '/post.json', json_data, headers)

response = conn.getresponse()
print(response.read().decode())
