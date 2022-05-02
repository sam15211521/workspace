import abc
from time import sleep


list = [1,2,3,4,5,6]

def adding_program(num1, num2):
    return num1 + num2

number1 = 'hello'

number2 = 4

take_number='1'

print(eval( f'list[{take_number}]' ))

num1 = 0

num2 = 1
for a in range(100):
    num3 = num1 + num2
    num1 = num2
    num2 = num3
print('\n',num1, '\n')
print(num2, '\n')

print(num2/num1)