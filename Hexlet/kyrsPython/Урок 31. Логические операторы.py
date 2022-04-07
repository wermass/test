def is_leap_year(year):
  return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))





print(is_leap_year(2018))  # False
print(is_leap_year(2017))  # False
print(is_leap_year(2016))  # True



# Реализуйте функцию is_leap_year(), которая определяет, является ли год високосным. Год будет високосным, если он кратен 400, или он одновременно кратен 4 и не кратен 100:

# from solution import is_leap_year
# is_leap_year(2018)  # False
# is_leap_year(2017)  # False
# is_leap_year(2016)  # True
# В определении уже заложена вся необходимая логика, осталось только переложить её на код.