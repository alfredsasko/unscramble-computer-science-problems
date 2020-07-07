"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
import re

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

def get_bangalore_codes(record_list):

    # patterns matching diffrent number types
    fixed_pattern = re.compile(r'^\((\d+?)\)')
    mobile_pattern = re.compile(r'^([789]\d{3})')
    tele_pattern = re.compile(r'(^140)')

    code_list = []
    for record in record_list:
        caller, reciever = record[0].strip(), record[1].strip()
        if is_bangalore(caller):
            if is_fixed(reciever):
                reciever_code = get_reciever_code(fixed_pattern, reciever)
                code_list.append(reciever_code)
            elif is_mobile(reciever):
                reciever_code = get_reciever_code(mobile_pattern, reciever)
                code_list.append(reciever_code)
            elif is_telemarketer(reciever):
                reciever_code = get_reciever_code(tele_pattern, reciever)
                code_list.append(reciever_code)
            else:
                raise Exception('Unknown reciever number format', reciever)
        else:
            continue

    return sorted(set(code_list))

def is_bangalore(number):
    return number.startswith('(080)')

def is_fixed(number):
    return number.startswith('(')

def is_mobile(number):
    return re.match(r'^[789]', number)

def is_telemarketer(number):
    return number.startswith('140')

def get_reciever_code(pattern, number):
    return pattern.match(number).group(1)


def get_bangalore_call_ratio(record_list):

    bangalore_caller = 0
    bangalore_reciever = 0
    for record in record_list:
        caller, reciever = record[0].strip(), record[1].strip()
        if is_bangalore(caller):
            bangalore_caller +=1
            if is_bangalore(reciever):
                bangalore_reciever +=1

    return bangalore_reciever / bangalore_caller * 100

print('he numbers called by people in Bangalore have codes:\n',
      get_bangalore_codes(texts + calls))

print(('{:0.2f} percent of calls from fixed lines in Bangalore are calls '
       'to other fixed lines in Bangalore.')
       .format(get_bangalore_call_ratio(texts + calls)))
