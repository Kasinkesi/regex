"""
Большие целые числа удобно читать, когда цифры в них разделены на тройки запятыми.
Переформатируйте целые числа в тексте.
"""

import re


def repl(match_obj):
    fullnum = int(match_obj[0])
    return '{0:,}'.format(fullnum)


def nums_to_triads(text):
    return re.sub(r"\d+", repl, text)


if __name__ == '__main__':
    text = """
    12 мало 
    лучше 123 
    1234 почти 
    12354 хорошо 
    стало 123456 
    супер 1234567
    1123456789123.45678
    """

    print(nums_to_triads(text))
