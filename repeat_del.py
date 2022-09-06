"""
Довольно распространённая ошибка ошибка — это повтор слова.
Вот в предыдущем предложении такая допущена. Необходимо исправить каждый такой повтор (слово, один или несколько
пробельных символов, и снова то же слово).
"""

import re

def repeat_del(text):
    return re.sub(r"(\w+)\s+(?=\b\1\b)", '', text)


if __name__ == '__main__':
    text = """
    Довольно распространённая ошибка ошибка ошибка — это лишний повтор повтор слова слова. Смешно, не 
    не правда ли? Не нужно портить хор хоровод.
    """
    print(repeat_del(text))