import requests
from bs4 import BeautifulSoup


# Написать функцию currency_rates(), принимающую в качестве аргумента код валюты (например, USD, EUR, GBP, ...)
# и возвращающую курс этой валюты по отношению к рублю.
# Использовать библиотеку requests.
# В качестве API можно использовать http://www.cbr.ru/scripts/XML_daily.asp.
# Рекомендация: выполнить предварительно запрос к API в обычном браузере,
# посмотреть содержимое ответа.
# Можно ли, используя только методы класса str, решить поставленную задачу?
# Функция должна возвращать результат числового типа, например float.
# Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal?
# Сильно ли усложняется код функции при этом? Если в качестве аргумента передали код валюты,
# которого нет в ответе, вернуть None.
# Можно ли сделать работу функции не зависящей от того, в каком регистре был передан аргумент?
# В качестве примера выведите курсы доллара и евро.


def currency_rates(val):  # аргумент функции - код валюты
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp')  #  гет запрос (чтение данных с сайта)
    encodings = requests.utils.get_encoding_from_headers(response.headers)  #  декодируем страницу
    content = response.content.decode(encoding=encodings)  #  декодируем контент на странице для чтения

    soup = BeautifulSoup(response.content, 'html.parser')  # приминаем метод для более удобного парсинга страницы
    convert = soup.findAll('charcode')  # применяем метод для поиска тега на странице для кода
    soup_value = soup.findAll('value')  # применяем метод для поиска тега на странице для значения валюты

    diction_currency = {  # Словарь с кодом валюты и значением
        convert[0].text: soup_value[0].text,
        convert[1].text: soup_value[1].text,
        convert[2].text: soup_value[2].text,
        convert[3].text: soup_value[3].text,
        convert[4].text: soup_value[4].text,
        convert[5].text: soup_value[5].text,
        convert[6].text: soup_value[6].text,
        convert[7].text: soup_value[7].text,
        convert[8].text: soup_value[8].text,
        convert[9].text: soup_value[9].text,
        convert[10].text: soup_value[10].text,
        convert[11].text: soup_value[11].text,
        convert[12].text: soup_value[12].text,
        convert[13].text: soup_value[13].text,
        convert[14].text: soup_value[14].text,
        convert[15].text: soup_value[15].text,
        convert[16].text: soup_value[16].text,
        convert[17].text: soup_value[17].text,
        convert[18].text: soup_value[18].text,
        convert[19].text: soup_value[19].text,
        convert[20].text: soup_value[20].text,
        convert[21].text: soup_value[21].text,
        convert[22].text: soup_value[22].text,
        convert[23].text: soup_value[23].text,
        convert[24].text: soup_value[24].text,
        convert[25].text: soup_value[25].text,
        convert[26].text: soup_value[26].text,
        convert[27].text: soup_value[27].text,
        convert[28].text: soup_value[28].text,
        convert[29].text: soup_value[29].text,
        convert[30].text: soup_value[30].text,
        convert[31].text: soup_value[31].text,
        convert[32].text: soup_value[32].text,
        convert[33].text: soup_value[33].text
    }
    upper_val = val.upper()  # чтобы приводить любой вводимый код к верхнему регистру
    if upper_val in diction_currency.keys():  # если ключ есть - вывести значение
        print((diction_currency.get(upper_val)))
    else: print('Валюты такой нет')

#    return diction_currency.get(val, default=None) - С ДАННЫМ МЕТОДОМ ЗАПУТАЛАСЬ, НЕ ПОЛУЧИЛОСЬ, ЧТОБ NONE ВЫВЕЛ

if __name__ == '__main__':  # пишем этот скрипт, чтобы после импортирования не запустился код, который ниже
    currency_rates('aa')
    currency_rates('AUD')
    currency_rates('eur')
    currency_rates('usd')
