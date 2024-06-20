import re

def multiply_numbers(inputs = ''):
    result = 1
    data = re.sub(r'\D', '', str(inputs))
    if len(data) == 0:
        return None
    for num in data:
        result *= int(num)
    return result