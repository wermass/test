def get_hidden_card(text, base=4):
    nomber_card = text.replace(text[:12], '*' * base)
    print(nomber_card)
    return nomber_card



# Реализуйте функцию get_hidden_card(), которая принимает на вход номер кредитки (состоящий из 16 цифр) в виде строки и возвращает его скрытую версию, которая может использоваться на сайте для отображения. Если исходная карта имела номер 2034399002125581, то скрытая версия выглядит так ****5581. Другими словами, функция заменяет первые 12 символов, на звездочки. Количество звездочек регулируется вторым необязательным параметром. Значение по умолчанию — 4.

# # Кредитка передается внутрь как строка
# get_hidden_caard('2034399002121100', 1)  # "*1100"
# get_hidden_card("1234567812345678", 2)  # "**5678"
# get_hidden_card("1234567812345678", 3)  # "***5678"
# get_hidden_card('1234567812345678')     # "****5678"
# Для выполнения задания вам понадобится размножить строку repeat. В Python это можно сделать так:

# "+" * 5  # "+++++"
# "o" * 5  # "ooooo"
