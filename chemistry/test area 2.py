def repeating_atoms_of_elements(symbol, number_of_atoms): # makes a list of repeating atoms based on the symbol and number of atoms of an element
    list_of_atoms = []
    for i in range(number_of_atoms):
        list_of_atoms.append(symbol)
    return list_of_atoms


def assigning_atoms_to_elements_from_compound(compound): #takes a string of a compound and breaks it up and returns a list of atoms

    list_of_atoms = []
    i =0
    symbol = ''
    number = '1'
    for letter in compound: #takes a one (1) chemical formula and breaks it appart into its symbols
        try:
            if letter.isalpha():
                
                if letter.isupper():
                    
                    if symbol == '':
                        symbol = letter
                        i += 1
                    elif symbol != '':
                        for amount in range(int(number)):
                            list_of_atoms.append(symbol)
                

                elif letter.islower():
                    symbol += letter
                    i += 1

            elif letter.isdigit():
                if compound[i-1].isdigit() == False:
                    continue
                    
        
        except IndexError:
            list_of_atoms += letter[i]
    list_of_atoms.append(symbol)
    
    print(list_of_atoms)


assigning_atoms_to_elements_from_compound('CaO')





def extract_number(string):
    pass


def example(string):
    lib = ['He', 'O', 'Na', 'H']
    for i in string:
        pass


#print(extract_number('a2c3'))
