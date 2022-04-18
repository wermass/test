def join_numbers_from_range(start, finish):
  result = ''

  for i in range(start, finish+1):
    result = f'{result}{i}'
    i += 1
  return result
  
#   Реализуйте функцию join_numbers_from_range(), которая объединяет все числа из диапазона в строку:
print(join_numbers_from_range(5, 10))
# join_numbers_from_range(1, 1)  # '1'
# join_numbers_from_range(2, 3)  # '23'
# join_numbers_from_range(5, 10)  # '5678910'
