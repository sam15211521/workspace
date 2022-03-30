from periodictable import formula
import periodictable

def find_molar_mass(compound): #finds the molar mass of a compound in grams
    compound_mass = formula(str(compound)).mass
    return compound_mass

def compounds_entered(i, reactants_or_products): #used to add the compounds to Enter_compounds
    compound_string=f"Type the formula of the {i} {reactants_or_products} in your chemical equation. "
    compound = input(compound_string)
    compound_upper = compound.upper()
    compound_mass = find_molar_mass(compound_upper)
    return {compound_upper: compound_mass}
    

def Enter_compounds(reactants_or_products = 'reactants'): #creates a dictionary of compounds present in the reaction equation
    reactant_flag = True
    product_flag = False
    dict_of_compounds = {}
    j = 1
    while reactant_flag == True:
        compounds=compounds_entered(j, reactants_or_products)
        dict_of_compounds.update(compounds)
        j += 1
        add_more = input('Do you have more to add? Y/N')
        add_more1 = add_more.upper()
        print(add_more1)
        if add_more1 != 'Y' and add_more1 !='N':
            add_more = input('Invalad Input!! \n do you have more to add? Y/N')
        if add_more1 == 'N':
            reactant_flag =False 
            return dict_of_compounds
        if add_more1 == 'Y':
            continue








def main():
    reactants = []
    products = []
    print(Enter_compounds())

    

main()