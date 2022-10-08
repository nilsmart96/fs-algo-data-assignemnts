def binary_search_tree(list_, query_):

    middle = len(list_) // 2

    if list_[middle]["no"] > query_:
        match = binary_search_tree(list_ = list_[:middle], query_ = query_)
    elif list_[middle]["no"] < query_:
        match = binary_search_tree(list_ = list_[middle:], query_ = query_)
    elif list_[middle]["no"] == query_:
        match = list_[middle]["name"]

    #git test JO

    return match