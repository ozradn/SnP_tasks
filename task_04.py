def sort_list(lst = None):
    if lst == None:
        return []
    max_value = max(lst)
    min_value = min(lst)
    sorted_list = [max_value if i == min_value else min_value if i == max_value else i for i in lst]
    sorted_list.append(min_value)
    return sorted_list