def clearing_blank_spaces(element_list):
    sorted_element_list =sorted(element_list)
    for character in sorted_element_list:
        if character == '':
            sorted_element_list.remove(character)
    return sorted_element_list


def assigning_atoms_to_elements_from_compound(compound):
    list_of_atoms = []
    i =0
    symbol = ''
    for letter in compound: #takes a one (1) chemical formula and breaks it appart into its symbols
        try:
            if letter.isalpha():
                
                if letter.isupper():
                    list_of_atoms.append(symbol)
                    symbol = letter
                    i += 1
                
                elif letter.islower():
                    symbol += letter
                    i += 1

            elif letter.isdigit():
                for character in range(len(letter)):
                    list_of_atoms.append(symbol)
        
        except IndexError:
            list_of_atoms += letter[i]
    list_of_atoms.append(symbol)
    
    return list_of_atoms

def seperating_compound_in_equation(reacatnts_or_products):  #takes the list of either products or reactant and breaks them up into their compounds
    
    for compound in reacatnts_or_products:
        pass


def main(formula):
 

    print(clearing_blank_spaces(assigning_atoms_to_elements_from_compound(formula)))

    #print(chemical_formula_atom_list)
    

        


#    letters.append(symbol)  
#    print(letters)

main(['Ca2O2'])







  #          print(f'{compound} length is {len(compound)}')


           ##### 
#            if index == len(compound): #checks if a letter is the last in a symbol in the compound
#                if letter.islower() == True: #determines if symbol is lowercase, if it is, then adds it to the symbol
#                    symbol += letter
#                    elements_in_formula+= symbol

                
            #    elif letter.isdigit() == True: # determines if a symbol is a number, if it is then adds it to number of atoms,
            #        number_of_atoms += letter
            #        elements_in_formula+=repeating_atoms_of_elements(symbol, int(number_of_atoms))
                    


            #    elif letter.isupper() == True: #checks if letter is upper, then 
            #        elements_in_formula += letter
            #####