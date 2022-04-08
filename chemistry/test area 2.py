from numpy import number


def repeating_atoms_of_elements(symbol, number_of_atoms): # makes a list of repeating atoms based on the symbol and number of atoms of an element
    list_of_atoms = []
    for i in range(number_of_atoms):
        list_of_atoms.append(symbol)
    return list_of_atoms


def seperating_num_of_atoms_of_elements(compounds):
    elements_in_formula =[]
    symbol = ''                 # the chemical symbol
    number_of_atoms = ''         # gives the amount of 

    for compound in compounds:  #cycling through compounds
        index = 0
        for letter in compound: #cycling through the letter of the compounds

            if symbol =='' and letter.isdigit() == False:     #checks if symbol is blank if blank adds letter to symbol (should not be a number)
                symbol = letter

           
            else:               #if symbol  has a symbol already in it we need to now see if the symbol has any other compounents to it such as a lower case letter or a number
                if letter.islower() == True: #determines if symbol is lowercase, if it is, then adds it to the symbol
                    symbol += letter

                
                elif letter.isdigit() == True: # determines if a symbol is a number, if it is then adds it to number of atoms,
                    number_of_atoms += letter


                elif letter.isupper() == True: #checks if letter is upper, then 
                    elements_in_formula+=repeating_atoms_of_elements(symbol, int(number_of_atoms))
                    symbol = letter
                    number_of_atoms = ''
                
                
            index += 1
            print(f'index = {index}')
        print(index)
        symbol = ''
        number_of_atoms = ''
        index = 0



    return elements_in_formula

print(seperating_num_of_atoms_of_elements([input('Na2O2'), 'H2O']))

#print(repeating_atoms_of_elements('Ca', int('2')))