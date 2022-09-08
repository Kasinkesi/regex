"""
Допустимый формат e-mail адреса регулируется стандартом RFC 5322.
Если говорить вкратце, то e-mail состоит из одного символа @ (at-символ или собака), текста до собаки (Local-part) и
текста после собаки (Domain part). Вообще в адресе может быть всякий беспредел (вкратце можно прочитать о нём в
википедии). Довольно странные штуки могут быть валидным адресом, например:
"very.(),:;<>[]\".VERY.\"very@\\ \"very\".unusual"@[IPv6:2001:db8::1]
"()<>[]:,;@\\\"!#$%&'-/=?^_`{}| ~.a"@(comment)exa-mple
Но большинство почтовых сервисов такой ад и вакханалию не допускают. И мы тоже не будем :)


Будем рассматривать только адреса, имя которых состоит из не более, чем 64 латинских букв, цифр и символов '._+-, а
домен — из не более, чем 255 латинских букв, цифр и символов .-. Ни Local-part, ни Domain part не может начинаться или
заканчиваться на .+-, а ещё в адресе не может быть более одной точки подряд.
Кстати, полезно знать, что часть имени после символа + игнорируется, поэтому можно использовать синонимы своего адреса
(например, shаshkоv+spam@179.ru и shаshkоv+vk@179.ru), для того, чтобы упростить себе сортировку почты. (Правда не все
сайты позволяют использовать "+", увы)


На вход даётся текст. Необходимо вывести все e-mail адреса, которые в нём встречаются. В общем виде задача достаточно
сложная, поэтому у нас будет 3 ограничения:
две точки внутри адреса не встречаются;
две собаки внутри адреса не встречаются;
считаем, что e-mail может быть частью «слова», то есть в boo@ya_ru мы видим адрес boo@ya,
а в foo№boo@ya.ru видим boo@ya.ru.
"""

import re


def email_search(text):
    res = []
    raw_mail_list = re.findall(r"[a-zA-Z0-9][a-zA-Z0-9'._+-]{,63}@[a-zA-Z0-9.-]{,254}[a-zA-Z0-9]", text)
    for raw_mail in raw_mail_list:
        dots_valid = re.search('\.\.', raw_mail)
        (local_part, domain_part) = raw_mail.split('@')
        lp_end_valid = re.fullmatch(r"[a-zA-Z0-9'._+-]*[a-zA-Z0-9'_]", local_part)
        dp_start_valid = re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9.-]*", domain_part)
        if not dots_valid and lp_end_valid and dp_start_valid:
            res.append(raw_mail)
    return res


if __name__ == '__main__':
    text = """Иван Иванович! 
    Нужен ответ на письмо от ivanoff@ivan-chai.ru. 
    Не забудьте поставить в копию 
    serge'o-lupin@mail.ru- это важно.
    
    NO: foo.@ya.ru, foo@.ya.ru 
    PARTLY: boo@ya_ru, -boo@ya.ru-, foo№boo@ya.ru"""
    print(email_search(text))
