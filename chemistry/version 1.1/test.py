from periodictable  import formula
def abc():
    a = formula("CaCO3 + Cl2").atoms
    print(a)
    for i in a:
        print(type(a[i]))


def calculating_element_amounts(chemical_fomula = ''):
    return_dict ={}
    symbol = ''
    amount = '1'
    amount_builder = ''
    
    for character in chemical_fomula:
        if symbol == '':
            symbol = character
        else:
            if character.isalpha() == True:
                
                if character.isupper() ==True:
                    if amount_builder == '':
                        return_dict[symbol] = int(amount)
                        amount = '1'
                        symbol = character
                    
                    if amount_builder != '':
                        amount = amount_builder
                        return_dict[symbol] = int(amount)
                        amount = '1'
                        amount_builder =''
                        symbol = character
                
                else:
                    symbol += character

            elif character.isdigit() == True:
                amount_builder += character
    if amount_builder != ''
    return_dict[symbol] = amount_builder
                
                
    return return_dict
    
abc()
c = calculating_element_amounts('C6H12O6')

print(c)
