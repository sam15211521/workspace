def repeating_atoms_of_elements(symbol, number_of_atoms): # makes a list of repeating atoms based on the symbol and number of atoms of an element
    list_of_atoms = []
    for i in range(number_of_atoms):
        list_of_atoms.append(symbol)
    return list_of_atoms


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


def extract_number(string):
    return_value = ''
    index = 0
    for value in string:
        if value.isdigit() ==True:
            if return_value == '':
                return_value = value
                index +=1
            else:
                if string[index + 1] == return_value and value.isdigit() == True:
                    return_value += value
                    index += 1
                else:
                    return return_value
        else:
            continue




    return return_value


def example(string):
    lib = ['He', 'O', 'Na', 'H']
    for i in string:
        pass


print(extract_number('a2c3'))

#assigning_atoms_to_elements_from_compound(input('O12'))