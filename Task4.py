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

def get_telemarketers(record_list):
    text_num_list, caller_list, reciever_list = [], [], []
    for record in record_list:
        caller, reciever = record[0].strip(), record[1].strip()
        if is_text(record):
            text_num_list.extend([caller, reciever])
        elif is_call(record):
            caller_list.append(caller)
            reciever_list.append(reciever)
        else:
            raise Exception('Type of the record not recognized')

    telemarketer_set = (set(caller_list)
                        - (set(reciever_list)
                           | set(text_num_list)))

    return sorted(telemarketer_set)

def is_text(record):
    return len(record) == 3

def is_call(record):
    return len(record) == 4

print('These numbers could be telemarketers:\n',
      get_telemarketers(texts + calls))
