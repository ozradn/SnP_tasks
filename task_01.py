import re


def is_palindrome(string):
    text = re.sub(r'\W', '', str(string)).lower()
    reverse = text[::-1]
    return text == reverse
