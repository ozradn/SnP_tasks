import re


def count_words(string:str):
    result = {}
    words = re.split(r'\W+', string.lower())
    for word in words:
        if word in result:
            result[word] += 1
        else:
            result[word] = 1
    return result