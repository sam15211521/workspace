from itertools import count

from numpy import product


def seperating_num_of_atoms_of_elements(compounds):
    elements_in_formula =[]
    symbol = ''
    
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
                      
            try:    #if a number comes after the symbol, this will repeat the symbol
                element_atom_amount =type(int(letter))
                if  element_atom_amount== int:
                    for ammount in range(int(letter)-1):
                        elements_in_formula.append(symbol)   
            except:
                continue          
    elements_in_formula.append(symbol)

    return elements_in_formula


def counting_num_of_atoms_of_element(compounds): #makes a dict of each element present then combines them into a dict of elements present

    element_number ={}

    
    lst_of_elements = sorted(seperating_num_of_atoms_of_elements(compounds)) #sorts the elements alphabetically
    symbol=''
    count = 0
    for element in lst_of_elements:
        if symbol == '':
            symbol = element
            count  = 1
        elif symbol == element:
            count += 1
        if symbol != element:
            element_number[symbol] = count
            symbol = element
            count = 1
    element_number[symbol] = count
    

    return element_number

def combining_reactants_and_products(reactants, products): #combines dict of elements from both reactants and products
    dict_of_reactants_and_products ={}

    dict_of_ractants = counting_num_of_atoms_of_element(reactants)
    dict_of_products = counting_num_of_atoms_of_element(products)

    dict_of_reactants_and_products['Reactants'] = dict_of_ractants
    dict_of_reactants_and_products['Products'] = dict_of_products

    return dict_of_reactants_and_products





print(seperating_num_of_atoms_of_elements({'CaO' : 44.0095, 'H2SO4' : 18.01528}))
print(counting_num_of_atoms_of_element({'CaO' : 44.0095, 'H2SO4' : 18.01528}))
print(combining_reactants_and_products({'H2O': 18, 'CO2': 44},{'H2CO3': 52}))