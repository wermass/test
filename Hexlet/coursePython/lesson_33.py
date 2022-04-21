def normalize_url(addres):
  https = 'https://'
  http = 'http://'
  if addres[:6] == http[:6]: # если адрес 'http://' ,то меняем его на 'https://' пример: меняем 'http://ai.fi' на 'https://ai.fi'
    addres = https + adres[7:]
    return addres
  elif addres[:7] == https[:7]: # если адрес 'https://' , то не трогаем пример: входящий 'http://ai.fi'  не трогаем 'https://ai.fi'
    return addres

  else :    # в любом другом случаее обавляем 'https://' перед адресом  пример: 'google.com'  меняем на 'https://google.com'
    return https+addres  



#     Реализуйте функцию normalize_url(), которая выполняет так называемую нормализацию данных. Она принимает адрес сайта и возвращает его с https:// в начале.

# Функция принимает адреса в виде:

# АДРЕС
# http://АДРЕС
# https://АДРЕС (уже нормализованный)
# и всегда возвращает адрес в виде https://АДРЕС.

# normalize_url('https://ya.ru')  # 'https://ya.ru'
# normalize_url('google.com')  # 'https://google.com'
# normalize_url('http://ai.fi')  # 'https://ai.fi'
# Подсказка
# Можно сравнить первые 7 символов адреса со строкой http://. Для этого потребуется получить кусок строки или отбросить ненужный. Мы рассматривали способ получения части строки её начала:

# # Берём 2 символd от начала
# print('Python'[:2])  # 'Py'
 
# # Отбрасываем первые 2 символа
# print('Python'[2:])  # 'thon'
