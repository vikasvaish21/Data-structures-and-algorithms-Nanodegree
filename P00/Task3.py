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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""
def code_called_by_bangalore():
    list_of_code = []
    for call in calls:
        if call[0].startswith('(080)'):
            code = None
            if call[1].startswith('('):
                closing_i = call[1].index(')')
                code = call[1][1:closing_i]
            elif ' ' in call[1]:
                code = call[1][:4]

            if code not in list_of_code:
                list_of_code.append(code)
    list_of_code.sort()
    return list_of_code

def perc_bangalore_to_bangalore():
    bangalore_calls = 0
    internal_bangalore_call = 0
    for call in calls:
        if call[0].startswith('(080)'):
            bangalore_calls += 1
            if call[1].startswith('(080)'):
                internal_bangalore_call += 1
    return internal_bangalore_call/float(bangalore_calls)*100

print("The numbers called by people in Bangalore have codes:")
print(*code_called_by_bangalore(), sep='\n')
print("\n{0:.2f} percent of calls from fixed lines in Bangalore are calls to other fixed lines in Bangalore."
      .format(perc_bangalore_to_bangalore()))