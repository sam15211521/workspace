def clearing_blank_spaces(element_list):
    sorted_element_list =sorted(element_list)
    for character in sorted_element_list:
        if character == '':
            sorted_element_list.remove(character)
    return sorted_element_list


def assigning_atoms_to_elements_from_compound(compound): #takes a string of a compound and breaks it up and returns a list of atoms
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

#print(assigning_atoms_to_elements_from_compound('CO2'))





def seperating_compound_in_equation(reacatnts_or_products):  #takes the list of either products or reactant and breaks them up into their compounds 
    list_of_elements = []
    for compound in reacatnts_or_products:
        elemental_list = assigning_atoms_to_elements_from_compound(compound = compound)
        list_of_elements += clearing_blank_spaces(elemental_list)
    return list_of_elements



print(seperating_compound_in_equation(['H22O10', 'CO2']))




