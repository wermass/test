def get_age_difference(x, y):
 
  opsr = (f'The age difference is {abs(x - y)}')  
  
  return opsr


actual = get_age_difference(2001, 2018)
print(actual)  # => The age difference is 17


# Это задание не связано напрямую с уроком, это просто еще одно полезное упражнение по работе с функциями.

# Напишите функцию get_age_difference(), которая принимает два года рождения и возвращает строку с разницей в возрасте в виде The age difference is 11. Например:

# actual = get_age_difference(2001, 2018)
# print(actual)  # => The age difference is 17