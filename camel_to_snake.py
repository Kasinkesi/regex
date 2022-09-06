"""
Владимир написал свой открытый проект, именуя переменные в стиле «ВерблюжийРегистр».
И только после того, как написал о нём статью, он узнал, что в питоне для имён переменных принято использовать
подчёркивания для разделения слов (under_score). Нужно срочно всё исправить, пока его не «закидали тапками».

Задача могла бы оказаться достаточно сложной, но, к счастью, Владимир совсем не использовал строковых констант и
классов.
Поэтому любая последовательность букв и цифр, внутри которой есть заглавные, — это имя переменной, которое нужно
поправить.
"""

import re


def upperC_to_lowerS(match_obj):
    if match_obj[1]:
        return match_obj[1].lower()
    elif match_obj[2]:
        return '_' + match_obj[2].lower()


def camel_to_snake(text):
    return re.sub(r"(\b[A-Z])|([A-Z])", upperC_to_lowerS, text)


if __name__ == '__main__':
    text = """
    MyVar17 = OtherVar + YetAnother2Var 
    TheAnswerToLifeTheUniverseAndEverything = 42
    """
    print(camel_to_snake(text))
