"""
Determine if sequence (or part of a sequence) of numbers is increasing

1) Iterate through the sequence and check if the next value is larger than the previous one
2) If the end is reached its True, otherwise its false
3) Check this for just parts of the initital sequence
"""

def num_increase(sequence):
    
    i = 0
    while sequence[i] < sequence[i + 1] and i <= len(sequence) - 2:
        if i + 2 == len(sequence):
            return True
        i += 1

    return False

def num_longest_increase(sequence):

    i = 0
    while i < len(sequence) - 1:
        for iterations in range(i + 1):
            if num_increase(sequence[iterations:iterations + len(sequence) - i]) == True:
                return sequence[iterations:iterations + len(sequence) - i]
        i += 1

    return "Decreasing list"

def num_increase_info(sequence):
        
    res_list = []
    res_dict = {}

    i = 0
    while i < len(sequence) - 1:
        for iterations in range(i + 1):
            if num_increase(sequence[iterations:iterations + len(sequence) - i]) == True:
                res_list.append(sequence[iterations:iterations + len(sequence) - i])
        i += 1

    list_ = 0
    while list_ < len(res_list):
        increasing_streak = "length " + str(len(res_list[list_]))
        if increasing_streak not in res_dict.keys():
            res_dict[increasing_streak] = 1
        else:
            res_dict[increasing_streak] += 1
        list_ += 1

    if len(res_list) == 0:
        return "Decreasing list"
    else:
        return res_dict

test = [1, 2, 5, 8, 7, 13, 24, 36, 45, 55, 60]
test2 = test[::-1]

import pandas as pd

increasing_streaks = pd.DataFrame(num_increase_info(test), index=[""]).transpose()

print(increasing_streaks)
print(num_longest_increase(test))