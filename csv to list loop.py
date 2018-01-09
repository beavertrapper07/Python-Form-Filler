# Framework to import big list of names and addys and loop through


import csv, time

with open('test.csv', 'r') as f:
  reader = csv.reader(f)
  your_list = list(reader)

for person in your_list:
    print(person[0])
    print(person[1])
    time.sleep(2)
    

