# Runtime Analysis

## Task 0
### Function: get_first_record
```
def get_first_record(record_list):
    first_record = record_list[0]
    return first_record
```

| Command             | Time Complexity   |
|-------------------  |:---------------:  |
| list.getitem()      |       O(1)        |
| Worst case          |       O(1)        |

### Function: get_last_record
```
def get_last_record(record_list):
    last_record = record_list[0]
    return last_record
```

| Command             | Time Complexity   |
|-------------------  |:---------------:  |
| list.getitem()      |       O(1)        |
| Worst case          |       O(1)        |

## Task 1
### Function: get_unique_numbers
```
def get_unique_numbers(record_list):
    unique_numbers = []
    for record in record_list:
        unique_numbers.extend([record[0], record[1]])
    return len(set(unique_numbers))
```

| Command               | Time Complexity     |
|-------------------    |:---------------:    |
| for loop              |       O(n)          |
|     list.extend()     |       O(k)          |
| set()                 |       O(n)          |
| len()                 |       O(1)          |
| Worst case            |       O(nk)         |

## Task 2
### Function: get_longest_call
```
def get_longest_call(record_list):
    record_dict = defaultdict(int)
    for record in record_list:
        num1, num2, duration = record[0], record[1], record[3]
        record_dict[num1] += int(duration)
        record_dict[num2] += int(duration)

    number = max(record_dict, key=record_dict.get)
    duration = record_dict[number]

    return number, duration
```

| Command            | Time Complexity     |
|----------------    |:---------------:    |
| for loop           |       O(n)          |
| max()              |       O(n)          |
|     dict.get()     |       O(n)*         |
| Worst case         |      O(n^2)         |

\* Could be improved by using the list instead of the dictionary to O(n)

## Task 3
### Function: get_bangalore_codes
```
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
```

| Command            | Time Complexity     |
|----------------    |:---------------:    |
| for loop           |       O(n)          |
|     re.match()     |      O(C^k)         |
| sorted()           |   O(n*log(n))*      |
|     set()          |       O(n)          |
| Worst Total        |     O(n*C^k)        |

- n - number of items in the record_list
- k - length of regular expression
- C - regular expression alternations

\* Could be improved to O(n*k), k being the length of a matching pattern by using str.startwith() and slicing which time complexity is O(k). In case of more complicated patterns following could help to reduce real re.match time complexity:
- reusing compiled patterns
- extract a common part of the alternation
- shortcut alternation,
- using non-capturing groups,
- being more specific
- bing not greedy

### Function: get_bangalore_call_ratio
```
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
```

| Command                 | Time Complexity     |
|---------------------    |:---------------:    |
| for loop                |       O(n)          |
|     str.startwith()     |       O(k)          |
| Worst Total             |      O(n*k)         |

## Task 4
### Function: get_telemarketers
```
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
```

| Command              | Time Complexity     |
|------------------    |:---------------:    |
| for loop             |       O(n)          |
|     len()            |       O(1)          |
|     extend()         |       O(2)          |
|     append()         |       O(1)          |
| set()                |       O(n)          |
| set.union()          |    O(k1 + k2)       |
| set.difference()     |       O(k)          |
| sorted()             |    O(k*ln(k))       |
| Worst Total          |    O(k*ln(k))       |

k1, k2, k = number of items in set k <= n,
