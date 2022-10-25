"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv

with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

telemarketers = []
texters_and_receivers = []
for sender, receiver, timestamp in texts:
    texters_and_receivers.append(sender)
    texters_and_receivers.append(receiver)

for caller, receiver, timestamp, duration in calls:
    texters_and_receivers.append(receiver)

for caller, receiver, timestamp, duration in calls:
    if caller not in texters_and_receivers:
        telemarketers.append(caller)
telemarketers.sort()
print(f"These numbers could be telemarketers:\n", '\n'.join(set(telemarketers)))
