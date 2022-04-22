from periodictable import formula, elements
import periodictable

def find_molar_mass(compound): #finds the molar mass of a compound in grams
    compound_mass = formula(str(compound)).mass
    return compound_mass

def compounds_entered(i, reactants_or_products): #used to add the compounds to Enter_compounds
    compound_string=f"Type the formula of the {i} {reactants_or_products} in your chemical equation. \n"
    compound = input(compound_string)
    while True:
        try:            
            compound_mass = find_molar_mass(compound)
        except Exception:
            compound = input(f'Error! Watch your capitlization of Element Symbols \n \n Please type the formula of the {i} {reactants_or_products} in your chemical equation. \n')
        else:
            return {compound: compound_mass}


    
    

def Enter_compounds(reactants_or_products = 'reactants'): #creates a dictionary of compounds present in the reaction equation
    reactant_flag = True
    product_flag = False
    dict_of_compounds = {}
    j = 1
    while reactant_flag == True:
        compounds=compounds_entered(j, reactants_or_products)
        dict_of_compounds.update(compounds)
        j += 1
        add_more = input('Do you have more to add? Y/N \n')
        add_more1 = add_more.upper()
        if add_more1 != 'Y' and add_more1 !='N':
            add_more = input('Invalad Input!! \n do you have more to add? Y/N \n')
        elif add_more1 == 'N':
            reactant_flag =False 
            return dict_of_compounds
        elif add_more1 == 'Y':
            continue
 
def making_chemical_equations(reactant_dictionary, product_dictionary):
    equation_string =''
    
    for key in reactant_dictionary:
        equation_string += key
        equation_string += ' + '
    equation_string = equation_string[:-2] + '-> '
    
    for key in product_dictionary:
        equation_string += key +' + '
    equation_string = equation_string[:-2]

    return equation_string

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

def combining_reactants_and_products(reactants, products): #combines dict of elements from both reactants and products and gives a layered dict with number of atoms of each element in the chemical equation
    dict_of_reactants_and_products ={}

    dict_of_ractants = counting_num_of_atoms_of_element(reactants)
    dict_of_products = counting_num_of_atoms_of_element(products)

    dict_of_reactants_and_products['Reactants'] = dict_of_ractants
    dict_of_reactants_and_products['Products'] = dict_of_products

    return dict_of_reactants_and_products


def balancing_chemical_equations(reactants, products):
    pass

def converting_grams_into_moles(reactants, products):
    pass

def repeating_objectives():
    pass


def what_to_do(prompt, reactants, products, unbal_formula):
    flag = True
    while flag == True:

        if prompt == '1':
            print()
            return combining_reactants_and_products(reactants=reactants, products=products)
        elif prompt == '0':
            print('\nHave a nice day\n')
            exit()
        


def main():
    reactants = Enter_compounds('reactants')
    print(reactants)
    print('\n Lets now enter products \n')
    products = Enter_compounds('products')
    
    print(f'{reactants}\n \n{products}')
    
    chemical_equation_unballanced = making_chemical_equations(reactants, products)
    print(chemical_equation_unballanced)

    prompt = input('\n \n type the number of what you want to do now?:  \n 1: determine number of atoms of each element\n 0: quit program ')
    
    a=what_to_do(prompt, reactants = reactants, products = products, unbal_formula = chemical_equation_unballanced)
    print(a)


    

main()