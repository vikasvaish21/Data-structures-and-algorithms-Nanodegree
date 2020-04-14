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

def telemarketing():
    possible_number = []
    for call in calls:
        if call[0] not in possible_number:
            possible_number.append(call[0])
    for call in calls:
        if call[1] in possible_number:
            possible_number.remove(call[1])

    for msg in texts:
        if msg[0] in possible_number:
            possible_number.remove(msg[0])
        if msg[1] in possible_number:
            possible_number.remove(msg[1])
    possible_number.sort()
    return possible_number

print("These numbers are doing telemarketing:")
print(*telemarketing(),sep='\n')
        
