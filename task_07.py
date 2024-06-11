

def combine_anagrams(words_array):

    result = []
    for example_word in words_array:
        elem = [word for word in words_array if sorted(list(word.lower())) == sorted(list(example_word.lower()))]
        if elem not in result:
            result += [elem]
    return result
