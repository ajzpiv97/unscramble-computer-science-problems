"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
from typing import List

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts: List[str] = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
first_record_texts = texts[0]
last_record_calls = calls[-1]

first_record_print_msg = f"First record of texts, {first_record_texts[0]} texts {first_record_texts[1]} at time" \
                  f" {first_record_texts[2]}"
print(first_record_print_msg)

last_record_print_msg = f"Last record of calls, {last_record_calls[0]} calls {last_record_calls[1]}" \
                        f" at time {last_record_calls[2]}, lasting {last_record_calls[3]} seconds"
print(last_record_print_msg)


