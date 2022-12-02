"""
Assignment Integer to Roman Nils Marthiensen Python 3.10.4

Explanation

Plan

1) Check wether the integer is 0, as there is no roman numeral for that
2) Create dictionary with the necessary roman to integer conversions
3) Loop through the dictionary from big to small numerals
4) The nearest roman numeral that's smaller than the integer (or equal) gets appended to the result
5) The "integer-value" of the appended roman numeral gets substracted from the input integer
6) Loop starts again until the whole input integer is replaced by roman symbols
4) return roman letter
"""


def int_to_roman(integer):
    
    if integer == 0:
        return "There is no roman symbol for zero"

    roman = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1,
    }

    res_roman = ""
    while integer > 0:
        for key, value in roman.items():
            while integer >= value:
                res_roman += key
                integer -= value

    return res_roman


integer_to_convert = int(
    input("Type in the integer that you want to convert to roman symbols: ")
)
print(int_to_roman(integer_to_convert))