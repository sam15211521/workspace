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
                    i += 1
        
        except IndexError:
            list_of_atoms += letter[i]
    list_of_atoms.append(symbol)
    
    print( list_of_atoms)

assigning_atoms_to_elements_from_compound('H22O3')