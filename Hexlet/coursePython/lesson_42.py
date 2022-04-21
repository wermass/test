from random import choice
text = "abcdef"

# BEGIN (write your solution here)
def choice_from_range(text, a, b):

  text1 = text[a: b+1]
  text2 = choice(text1)
  return text2
                        #!!!WARNING!!! немного тупил со строчками import и return, по жтому думал ошибка в переменных и функциях, из-за этого в 2 строки, так понимаю что можно в 1=)
# END
#Реализуйте функцию choice_from_range(), которая принимает строку-набор и выбирает случайный символ по индексу из ограниченного диапазона.

#Аргументы функции:

#строка-набор
#начальный индекс диапазона
#конечный индекс диапазона
#text = "abcdef"
#choice_from_range(text, 3, 5)  # d
#choice_from_range(text, 3, 5)  # f
#choice_from_range(text, 3, 5)  # e