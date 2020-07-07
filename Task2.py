"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
from collections import defaultdict
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

def get_longest_call(record_list):
    record_dict = defaultdict(int)
    for record in record_list:
        num1, num2, duration = record[0], record[1], record[3]
        record_dict[num1] += int(duration)
        record_dict[num2] += int(duration)

    number = max(record_dict, key=record_dict.get)
    duration = record_dict[number]

    return number, duration

print(('{} spent the longest time, {} seconds, on the phone '
       'during September 2016.'.format(*get_longest_call(calls))))
