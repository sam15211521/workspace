#from time import sleep
#
#import Element_class as Ele
import inspect

#list = [1,2,3,4,5,6]

#def adding_program(num1, num2):
#    return num1 + num2

#number1 = 'hello'

#number2 = 4

#take_number='1'

#print(eval( f'list[{take_number}]' ))

#num1 = 0

#num2 = 1
#for a in range(100):
#    num3 = num1 + num2
#    num1 = num2
#    num2 = num3
#print('\n',num1, '\n')
#print(num2, '\n')

#print(num2/num1)


#first_element = 'H'


#second_element = 'C'
#second_elementeval = eval(eval('f"Ele.{second_element}.name"'))

#print(f'\n\n the elements you have chosen are: {first_elementeval} and {second_elementeval}')
#print(Ele.H.name)

class Part:
    def __init__(self, symbol, mass):
        self.symbol = symbol
        self.mass = mass

    def making_a_group(part_symbol_list):
        group_symbol = ''
        group_mass = 0
        #new_group_list = []
        for part in part_symbol_list:
            group_symbol+= eval(f'{part}.symbol')
            group_mass += eval(f'{part}.mass')
        New_group = Group(symbol = group_symbol, mass = group_mass)
        return New_group


class Group:
    def __init__(self, symbol, mass):
        self.symbol = symbol
        self.mass = mass



A = Part('A', 2.3)

B = Part('B', 4)

C = Part('C', 5.1)

list_of_parts = [A, B, C]

to_do = ['A', 'B', 'A']

new_object = Part.making_a_group(to_do)

print(isinstance(A, Part))

