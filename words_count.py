"""
Слово — это последовательность из букв (русских или английских), внутри которой могут быть дефисы.
На вход даётся текст, посчитайте, сколько в нём слов.
PS. Задача решается в одну строчку. Никакие хитрые техники, не упомянутые выше, не требуются.
"""

import re


def words_count(text):
    return len(re.findall(r'\b[\w-]+\b', text))


if __name__ == '__main__':
    text = """
    Он --- серо-буро-малиновая редиска!! 
    >>>:->
    
    А не кот.
    www.kot.ru
    """

print(wordsCount(text))
