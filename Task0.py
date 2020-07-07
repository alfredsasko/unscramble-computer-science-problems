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
def get_first_record(record_list):
    first_record = record_list[0]
    return first_record

def get_last_record(record_list):
    last_record = record_list[0]
    return last_record


print('First record of texts, {} texts {} at time {}'
      .format(*get_first_record(texts)))

print('Last record of calls, {} calls {} at time {}, lasting {} seconds'
      .format(*get_last_record(calls)))
