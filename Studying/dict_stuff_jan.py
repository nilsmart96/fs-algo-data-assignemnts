dict_list = [{"A": 1, "B": 2, "D": 3}, {"C": 10, "B": 20, "A": 30}, {"B": 11, "A": 22, "C": 33}]

"""
List of dictionaries contain same keys?

1) iterate over list of dictionaries, get key values
2) check the individual keys
3) return boolean
"""

def check_dict_keys(list_of_dicts):

    key_list = []
    for dict_ in list_of_dicts:
        key_list.append(list(dict_.keys()))
    
    i = 0
    while i < len(key_list) - 1:
        if set(key_list[i]) != set(key_list[i + 1]):
            return False  
        i += 1

    return True

print(check_dict_keys(dict_list))

"""
All keys in every dictionary

1) Create "Master" list of the keys of all dictionaries 
2) check for each dictionary if its missing any keys
3) Add those
"""

def superset_dict(list_of_dicts):

    key_list = []
    for dict_ in list_of_dicts:
        key_list.append(list(dict_.keys()))

    key_list = sum(key_list, [])
    key_list = list(dict.fromkeys(key_list))

    for dict_ in list_of_dicts:
        for key in key_list:
            if key not in dict_.keys():
                dict_[key] = "?"

    return list_of_dicts

#print(superset_dict(dict_list))

"""
Only intersecting keys in every dictionary

1) Create "Master" list of the keys contained in all dictionaries
2) Check for each dictionary if more than this is included
3) Delete the ones that are not in the list
"""

def intersect_dict(list_of_dicts):

    key_list = []
    for dict_ in list_of_dicts:
        key_list.append(list(dict_.keys()))

    key_list = sum(key_list, [])
    key_list_singles = list(dict.fromkeys(key_list))
    
    for dict_ in list_of_dicts:
        for key in key_list_singles:
            if key_list.count(key) != len(list_of_dicts):
                if key in dict_.keys():
                    del dict_[key]

    return list_of_dicts

print(intersect_dict(dict_list))