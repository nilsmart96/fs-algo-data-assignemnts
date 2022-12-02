"""
Find numbers in a sequence that add up to a given number

1) keep first number of sequence and iterate through the rest, if input number can be reached
2) repeat starting at the second number in the sequence
3) return combination when input number is reached
"""

def add_to_num(list_, number):
    
    i = 0
    while i < len(list_):
        for j in list_[i + 1:]:
            if list_[i] + j == number:
                return [list_[i], j]
        i += 1
    return "The numbers in the list don't add up to the given number"

test_list = [3, 4, 1, 7, 9, 17]

test_number = 8

print(add_to_num(test_list, test_number))