"""
Find all palindromes in a given sequence

1) Pick section of the input
2) check if its a palindrome
3) return it if true
"""

def check_palindrome(input_):
    
    input_ = str(input_).lower()
    input_rev = input_[::-1]

    if input_ == input_rev:
        return True
    else:
        return False

def all_palindromes(input_):

    input_ = str(input_).lower()
    res_list = []

    i = 0
    while i < len(input_) - 1:
        for iterations in range(i + 1):
            if check_palindrome(input_[iterations:iterations + len(input_) - i]) == True:
                res_list.append(input_[iterations:iterations + len(input_) - i])
        i += 1

    if len(res_list) == 0:
        return "No palindromic parts in the input"
    else:
        return res_list

print(all_palindromes("Ananas"))
print(all_palindromes(1234437666))
print(all_palindromes(1234))