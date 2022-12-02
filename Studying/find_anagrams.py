"""
Given two strings, find out if they are anagrams of each other

1) Check if more code is even necessary, by comparing the length of both words
2) If so, convert strings to lists and lowercase, so they are mutable
3) Sort the letters of both words alphabetically using a sorting algorithm from class
4) Compare if they are the same
5) Return boolean
"""

def check_anagram(word_one, word_two):

    if len(word_one) == len(word_two):
        letters_one = insertion_sort(list(word_one.lower()))
        letters_two = insertion_sort(list(word_two.lower()))

        if letters_one == letters_two:
            return True

    return False

def insertion_sort(list_):
    i = 1
    while i < len(list_):
        key = list_[i]
        j = i - 1
        while list_[j] > key and j >= 0:
            list_[j + 1] = list_[j]
            j = j - 1
        list_[j + 1] = key
        i = i + 1
    return list_

print(check_anagram("Anagram", "Maargan"))