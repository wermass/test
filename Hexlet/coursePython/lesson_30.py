def has_upper_case(string):
  if string == '': 
    return False
    
  
  return not string.islower()




has_upper_case("python")  # False
has_upper_case("Hexlet")  # True



# Реализуйте функцию has_upper_case(), которая определяет, содержит ли строка заглавные буквы:

# from solution import has_upper_case
# has_upper_case("python")  # False
# has_upper_case("Hexlet")  # True
# Подсказка
# Воспользуйтесь методом из стандартной библиотеки, которая приводит строку к нижнему регистру. Чем отличается такая строка от исходной?