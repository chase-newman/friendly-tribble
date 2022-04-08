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



file = open("DealSiteUpdates.csv")
csvreader = csv.reader(file)

header = []
header = next(csvreader)
print(header)

rachel = []
for row in csvreader:
    if(row[1] == "Rachel R Cuomo"):
        rachel.append(row)

print(rows)
print(len(rows))

file.close()

# with open('dailyibmstock.csv') as csv_file:
#     csv_reader = csv.reader(csv_file, delimiter=',')
#     print(csv_reader)
#     line_count = 0
#     list = 0
#     print(csv_reader)
#     for row in csv_reader:
#         print(row[3])
#         if(row[3] != "low"):
#             num = int(row[3])
#             if (num > 120):
#                 list = row[3]
#                 print(list)
#             else:
#                 print("Number is less than 100")
    # for row in csv_reader:
    #     print(row[0])
    #     line_count += 1
    #     print(line_count)
    # print(f'Processed {line_count} lines.')


# connection = http.client.HTTPSConnection("test-project-d14cc-default-rtdb.firebaseio.com")
# connection.request("GET", "/private.json")
# response = connection.getresponse()
# print(response.headers)
# data = response.read()
# print("Status: {} and reason: {}".format(response.status, response.reason))

# print(data)

# connection.close()




# conn = http.client.HTTPSConnection('test-project-d14cc-default-rtdb.firebaseio.com')

# headers = {'Content-type': 'application/json'}

# foo = {'text': 'Hello HTTP #1 **cool**, and #1!'}
# json_data = json.dumps(foo)

# conn.request('POST', '/post.json', json_data, headers)

# response = conn.getresponse()
# print(response.read().decode())
