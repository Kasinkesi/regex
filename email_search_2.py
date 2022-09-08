"""
На вход даётся текст. Необходимо вывести все e-mail адреса, которые в нём встречаются. При этом e-mail не может быть
частью слова, то есть слева и справа от e-mail'а должен быть либо конец строки, либо не-буква и при этом не один из
символов '._+-, допустимых в адресе
"""

import re


def email_search_2(text):
    res = []
    for m in re.finditer(r"[a-zA-Z0-9][a-zA-Z0-9'._+-]{,63}@[a-zA-Z0-9.-]{,254}[a-zA-Z0-9]", text):
        if re.fullmatch("[-'._+@]", text[m.start() - 1]) or re.fullmatch("['_+@]", text[m.end()]):
            continue
        else:
            dots_valid = re.search('\.\.', m[0])
            (local_part, domain_part) = m[0].split('@')
            lp_end_valid = re.fullmatch(r"[a-zA-Z0-9'._+-]*[a-zA-Z0-9'_]", local_part)
            dp_start_valid = re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9.-]*", domain_part)
            dp_one_dot_valid = re.search("\.", m[0])
            if not dots_valid and lp_end_valid and dp_start_valid and dp_one_dot_valid:
                res.append(m[0])
    return res


if __name__ == '__main__':
    text = """Иван Иванович! 
    Нужен ответ на письмо от ivanoff@ivan-chai.ru. 
    Не забудьте поставить в копию 
    serge'o-lupin@mail.ru- это важно.
    
    NO: foo.@ya.ru, foo@.ya.ru, foo@foo@foo
    NO: +foo@ya.ru, foo@ya-ru
    NO: foo@ya_ru, -foo@ya.ru-, foo@ya.ru+
    NO: foo..foo@ya.ru 
    YES: (boo1@ya.ru), boo2@ya.ru!, boo3@ya.ru
    """
    print(email_search_2(text))
