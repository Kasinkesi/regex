"""
Если вы когда-нибудь пытались собирать номера мобильных телефонов, то наверняка знаете, что почти любые 10 человек
используют как минимум пяток различных способов записать номер телефона. Кто-то начинает с +7, кто-то просто с 7 или 8,
а некоторые вообще не пишут префикс. Трёхзначный код кто-то отделяет пробелами, кто-то при помощи дефиса, кто-то
скобками (и после скобки ещё пробел некоторые добавляют). После следующих трёх цифр кто-то ставит пробел, кто-то дефис,
кто-то ничего не ставит. И после следующих двух цифр — тоже. А некоторые начинают за здравие, а заканчивают… В общем
очень неудобно!


На вход даётся номер телефона, как его мог бы ввести человек. Необходимо его переформатировать в формат
+7 123 456-78-90. Если с номером что-то не так, то нужно вывести строчку Fail!.
"""

import re


def phone_formater(phone_num):
    match = re.fullmatch(r"\A\+?[78]?(?:\(| |-)?\d\d\d(?:\)| |\) |-)?\d\d\d(?: |-)?\d\d(?: |-)?\d\d", phone_num)
    if not match:
        return "Fail!"
    else:
        return re.sub(r"\A\+?[78]?(?:\(| |-)?(\d\d\d)(?:\)| |\) |-)?(\d\d\d)(?: |-)?(\d\d)(?: |-)?(\d\d)",
                      r"+7 \1 \2-\3-\4", phone_num)


if __name__ == '__main__':
    num_list = [
        "+7 123 456-78-90",
        "8(123)456-78-90",
        "7(123) 456-78-90",
        "1234567890",
        "+7(123 45678-90",
        "123456789",  # fails
        "+9 123 456-78-90",
        "+7 123 456+78=90",
        "8(123  456-78-90"
    ]
    for num in num_list:
        print(num, "===>", phone_formater(num))
