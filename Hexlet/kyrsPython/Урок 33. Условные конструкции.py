def normalize_url(adres):
  https = 'https://'
  http = 'http://'
  if adres[:6] == http[:6]:
    adres = https + adres[7:]
    return adres
  elif adres[:7] == https[:7]:
    return adres

  else :    
    return https+adres  



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
