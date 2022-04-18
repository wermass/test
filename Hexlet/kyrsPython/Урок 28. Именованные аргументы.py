def capitalize(name):
  if len(name) > 0: # помнишь, была ошибка с пустой строкой, поправил на костылях+)))))
    name = f'{name[0].upper()}{name[1:]}'

    return name

print(capitalize('arya'))
print('')
print('Arya')

# Реализуйте функцию capitalize(), которая принимает непустую строку и приводит первую букву первого слова к верхнему регистру:

# name = 'arya'
# print(capitalize(name)) # => "Arya"