from periodictable  import formula
from time import sleep
def adding_chemical_compounds(): #creates a chemical compound object
    pass

def adding_chemical_formulas(): #creates a chemical fomrula string from input for CHOICE 2
    pass

def breaking_appart_chemical_formulas(): # breaks the fomula up into a list of chemical compounds objects.
    pass

def finding_element_atoms_from_formula(chemical_fomula = ''): #returns a dictionary of elements with number of them.
        return_dict ={}
        symbol = ''
        amount = '1'
        amount_builder = ''
        
        for character in chemical_fomula:
            if symbol == '':
                symbol = character
            else:
                if character.isalpha() == True:
                    
                    if character.isupper() ==True:
                        if amount_builder == '':
                            return_dict[symbol] = int(amount)
                            amount = '1'
                            symbol = character
                        
                        if amount_builder != '':
                            amount = amount_builder
                            return_dict[symbol] = int(amount)
                            amount = '1'
                            amount_builder =''
                            symbol = character
                    
                    else:
                        symbol += character

                elif character.isdigit() == True:
                    amount_builder += character

        if amount_builder != '':
            return_dict[symbol] = amount_builder
                             
        return return_dict


def compound_finding():
    pass


def exit_program():
    print('\nGood Bye\n')
    sleep(2)
    exit()

def inputing_compounds(): #initial inputing commands
    first_line_text = "What do you want to do?: \n1) add a compound \n2) add a formula \n3) find the mass of an element \n4) EXIT \n\n"
    first_line = input(first_line_text)
    
    while first_line not in {'1', '2', '3', '4'}:
        first_line_text_2 = "please enter the number of your choice:  \n1) add a compound \n2) add a formula \n3) find the mass of an element \n4) EXIT \n\n"
        first_line = input(first_line_text_2)
    
    if first_line == '1': #enters just a formula

        pass
    elif first_line == '2':
        pass
    elif first_line == '3':
        pass
    
    elif first_line == '4': #final command is exiting
        exit_program()
    

    
    


def main():
    inputing_compounds()

main()