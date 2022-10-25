"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during 
September 2016.".
"""

phone_dict = {}

for record in calls:
    phone_dict[record[0]] = int(record[3]) + phone_dict.get(record[0], 0)
    phone_dict[record[1]] = int(record[3]) + phone_dict.get(record[1], 0)


max_value = 0
phone_number = 0
for key, value in phone_dict.items():
    if value > max_value:
        max_value = value
        phone_number = key

print(f"{phone_number} spent the longest time, {max_value} seconds, on the phone during September 2016.")