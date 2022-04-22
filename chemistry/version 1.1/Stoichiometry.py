#from periodictable import formula, elements
from time import sleep

class Chemical_Compounds:
    def __init__(self, formula, elements_present, mass):
        pass
    def find_mass():
        pass
    def break_into_elements():
        pass

    class elements:
        def __init__(self, symbol, number_of_atoms, mass):
            pass
        pass



def inputing_compounds():
    first_line_text = "What do you want to do?: \n1) add a compound \n2) add a formula \n3) find the mass of an element \n4) EXIT \n\n"
    first_line = input(first_line_text)
    
    while first_line not in {'1', '2', '3', '4'}:
        first_line_text_2 = "please enter the number of your choice:  \n1) add a compound \n2) add a formula \n3) find the mass of an element \n4) EXIT \n\n"
        first_line = input(first_line_text_2)
    
    if first_line == '1':
        pass
    elif first_line == '2':
        pass
    elif first_line == '3':
        pass
    elif first_line == '4':
        print('\nGood Bye')
        sleep(2)
        exit()
    

    print(first_line)
    


def main():
    inputing_compounds()

main()