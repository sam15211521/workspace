def seperating_num_of_atoms_of_elements(compounds):
    elements_in_formula =[]
    symbol = ''
    number_of_atoms =''
    for compound in compounds:  #will make a list of elements
        for letter in compound:
            if type(letter) == int:
                elements_in_formula.append(symbol)            
            if letter.isupper() == True: 
                if symbol != '':
                    elements_in_formula.append(symbol)
                symbol = ''
                symbol = letter
            if letter.islower() == True:
                symbol += letter



            if number_of_atoms == '':

                try:    #if a number comes after the symbol, this will repeat the symbol
                    element_atom_amount =type(int(letter))
                    if  element_atom_amount== int:
                        number_of_atoms =number_of_atoms+(letter)
                except:
                    continue          
            #if isinstance(int(number_of_atoms), int) == True:
                



    return elements_in_formula



def origional():
    symbol = ''
    letter = ''
    try:    #if a number comes after the symbol, this will repeat the symbol
        element_atom_amount =type(int(letter))
        if  element_atom_amount== int:
            for ammount in range(int(letter)-1):
                elements_in_formula.append(symbol) 
    except:

        return symbol
   




print(seperating_num_of_atoms_of_elements([input('CaO12'), 'H12O1']))