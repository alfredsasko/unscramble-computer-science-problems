# Runtime Analysis
## Task 1
### Function: get_unique_numbers
| Command               | Time Complexity     |
|-------------------    |:---------------:    |
| for loop              |       O(n)          |
|     list.extend()     |       O(k)          |
| set()                 |       O(n)          |
| len()                 |       O(1)          |
| Worst case            |       O(nk)         |

## Task 2
### Function: get_longest_call
| Command            | Time Complexity     |
|----------------    |:---------------:    |
| for loop           |       O(n)          |
| max()              |       O(n)          |
|     dict.get()     |       O(n)*         |
| Worst case         |      O(n^2)         |

\* Could be improved by using the list instead of the dictionary to O(n)

## Task 3
### Function: get_bangalore_codes
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
| Command                 | Time Complexity     |
|---------------------    |:---------------:    |
| for loop                |       O(n)          |
|     str.startwith()     |       O(k)          |
| Worst Total             |      O(n*k)         |

## Task 4
### Function: get_telemarketers
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
