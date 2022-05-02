import Element_class
from time import sleep


def electronegativities_prompt(): #this belongs not as a method but as a function
        print('This program compairs two elements and gives their electronegativity diffrences,\nas well as their predicted bond type')
        sleep(2)
        prompt1_1text = 'What do you want to do? (type the number):\n 1) Enter elements \n 2)Exit\n\n'
        prompt1_1 = input(prompt1_1text)

        while prompt1_1 != '1' and prompt1_1 != '2':
            prompt1_1 = input('Please enter a number: \n 1) Enter elements \n 2)Exit\n\n')
        else:
            if prompt1_1 == '1':
                prompt1_flag = True
                while prompt1_flag == True:
                    first_element = input('Please input the symbol or name of the first element you wish to compare.')
                    second_element = input('Please input the symbol or name of the second element you wish to compare.')
                    
                   #statment = f'The elements you have chosen are {}, ({}) and {}, ({})'

            elif prompt1_1 == '2':
                return False

def main():
    electronegativities_prompt()

#main()
#c = input('type an element symbol')

aaa = 'Mo'

for ele in Element_class.element_list:
    if aaa == ele.symbol:
        print(ele.name)
    else:
        continue
