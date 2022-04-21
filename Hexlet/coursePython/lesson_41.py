from package.functions import greet
from package.names import NAME
# BEGIN (write your solution here)
GREETING = greet(NAME)
# END
#Добавьте в __init__.py константу GREETING, которая должна содержать результат применения функции greet() 
#к константе NAME (и та, и другая импортируются из модулей пакета в блоке импортов модуля __init__.py).