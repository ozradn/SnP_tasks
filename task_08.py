import re

def multiply_numbers(inputs):
    result = 1
    data = re.sub(r'\D', '', str(inputs))
    for num in data:
        result *= int(num)
    return result