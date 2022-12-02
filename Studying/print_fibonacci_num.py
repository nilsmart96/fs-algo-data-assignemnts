"""
Print out all fibonacci numbers smaller or equal to a given number

1) Calculate fibonacci numbers until given stop
2) print result

Note that they start at 0 when looking at wikipedia, so I start with 0 in my implementation
If this is not wanted just add "[1:]" at the back of the return statement in line 20
"""

def fibonacci_num(max_num):
    
    res_list = [0, 1]

    i = 1
    while res_list[i] + res_list[i - 1] <= max_num:
        res_list.append(res_list[i] + res_list[i - 1])
        i += 1
    
    return res_list #[1:]

test = 13

print(fibonacci_num(test))