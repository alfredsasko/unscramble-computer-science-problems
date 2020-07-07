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
def get_unique_numbers(record_list):
    unique_numbers = []
    for record in record_list:
        unique_numbers.extend([record[0], record[1]])
    return len(set(unique_numbers))

print('There are {:d} different telephone numbers in the records.'
      .format(get_unique_numbers(texts + calls)))
