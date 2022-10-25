"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from typing import List

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
total_telephone_numbers = []


def get_phone_records_count(records: List[List[str]]):
    for record in records:
        total_telephone_numbers.append(record[0])
        total_telephone_numbers.append(record[1])


get_phone_records_count(texts)

get_phone_records_count(calls)

msg = f"There are {len(set(total_telephone_numbers))} different telephone numbers in the records."
print(msg)
