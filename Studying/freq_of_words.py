"""
Word counter

1) iterate over given sequence
2) if new word is found, add to dictionary with value 1
3) if word is found again, add value 1 to given dictionary key
4) return the created dictionary as a table
"""

def word_counter(sequence):

    results = {}

    for word in sequence:
        if word not in results.keys():
            results[word] = 1
        else:
            results[word] += 1 

    return results

test = ["hi", "I", "am", "Alexa", "I", "would", "just", "like", "to", "say", "hi"]

import pandas as pd

word_counter_results = pd.DataFrame(word_counter(test), index=[""]).transpose()

print(word_counter_results.head(len(test)))