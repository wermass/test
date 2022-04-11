def capitalize(name):
  name = f'{name[0].upper()}{name[1:]}'
  while len(name) < 1: # пробовал if, одна и таже фигня, выдает invalid syntax при пустой строке, без пустой строки работает
    print('')
    break
  return name

print(capitalize('arya'))
print(capitalize('')
print('Arya')

# Реализуйте функцию capitalize(), которая принимает непустую строку и приводит первую букву первого слова к верхнему регистру:

# name = 'arya'
# print(capitalize(name)) # => "Arya"