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
TASK 1:
How many different telephone numbers are there in the records? 
Print a message:
"There are <count> different telephone numbers in the records."
"""
def different_number():
    numbers = []
    for records in texts:
        if records[0] not in numbers:
            numbers.append(records[0])
        if records[1] not in numbers:
            numbers.append(records[1])
    for records in calls:
        if records[0] not in numbers:
            numbers.append(records[0])
        if records[1] not in numbers:
            numbers.append(records[1])
    return len(numbers)
    
print("There are %(count)s different telephone numbers in the records."%{'count':different_number()})
