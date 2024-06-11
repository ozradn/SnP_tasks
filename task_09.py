def connect_dicts(dict1:dict,dict2:dict):
    merged_dict = {}
    result = {}
    if sum(dict1.values()) > sum(dict2.values()):
        dict1, dict2 = dict2, dict1
    for key, value in dict2.items():
        if dict2[key] >= 10:
            merged_dict[key] = value
    for key, value in dict1.items():
        if dict1[key] >= 10 and key not in merged_dict:
            merged_dict[key] = value
    sorted_list = sorted(merged_dict.items(), key = lambda item: item[1])
    for key, value in sorted_list:
        result[key] = value
    return result