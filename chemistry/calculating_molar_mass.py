
from logging import exception
from periodictable import formula
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








def main():
    reactants = Enter_compounds('reactants')
    print(reactants)
    print('\n Lets now enter products \n')
    products = Enter_compounds('products')
    
    print(f'{reactants}\n \n{products}')
    
    chemical_formula_unballanced = making_chemical_equations(reactants, products)
    print(chemical_formula_unballanced)

    

main()