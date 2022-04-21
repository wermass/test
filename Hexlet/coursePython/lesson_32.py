# BEGIN (write your solution here)
def string_or_not(z): # созадл функцию, где переменная z вводимые символы
  
  y = isinstance(z, str) # определил, что у проверяет переданный параметр z через функцию insinstance
  
  return (y and 'yes' or 'no')
string_or_not('Hexlet') # 'yes' дальнейшие yes and no от создателей задачи
string_or_not(10) # 'no'
string_or_not('') # 'yes'
string_or_not(False) # 'no'
# END


# Реализуйте функцию string_or_not(), которая проверяет является ли переданный параметр строкой. Если да, то возвращается 'yes' иначе 'no'

# string_or_not('Hexlet') # 'yes'
# string_or_not(10) # 'no'
# string_or_not('') # 'yes'
# string_or_not(False) # 'no'
# Проверить, что значение является строкой, можно с помощью функции isinstance():

# isinstance(3, str) # False
# isinstance('Hexlet', str) # True
