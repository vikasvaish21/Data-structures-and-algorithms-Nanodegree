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
TASK 0:
What is the first record of texts and what is the last record of calls?
Print messages:
"First record of texts, <incoming number> texts <answering number> at time <time>"
"Last record of calls, <incoming number> calls <answering number> at time <time>, lasting <during> seconds"
"""
def first_text():
    if not texts:
        return None
    return texts[0]
def last_call():
    if not calls:
        return None
    return calls[-1]

text = first_text()
print("first record of the texts, %(incoming)s texts %(answering)s at time %(time)s" %{'incoming':text[0],'answering': text[1],'time': text[2]})
call = last_call()
print("last record of the texts, %(incoming)s texts %(answering)s at time %(time)s,lasting %(during)s seconds" %{'incoming': call[0],'answering': call[1],'time': call[2],'during': call[3]})
