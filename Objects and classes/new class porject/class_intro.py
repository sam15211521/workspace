from xml.dom.minidom import Element


class Elements:
    number_of_element = 0

    def __init__(self, symbol, name, mass):
        self.name = name
        self.symbol = symbol
        self.mass = mass
        Elements.number_of_element += 1
    
    def __del__(self):
        print(f'Element {self.name} deleted')
        Elements.number_of_element -= 1

def making_elements():
    lst_of_element_objects = {}
    flag = True
    while flag == True:
        element_name = input('What is the name of the element\n\n')
        element_symbol = input('What is the symbol of the element?\n\n')
        element_mass = input('what is the mass of the element?\n\n')
        while element_mass.replace('.', '', 1).isdigit() == False:
            element_mass = input('what is the mass of the element?\n\n')
        lst_of_element_objects[element_symbol] = Elements(element_symbol, element_name, float(element_mass))
        
        
        next_element = input('do you have another element?   Y/N')
        
        
        new_element = True
        while new_element ==True:
            if next_element.upper() == 'N':
                flag = False
                new_element = False
            elif next_element.upper() == 'Y':
                new_element = False
            else:
                continue
    print(lst_of_element_objects)
    return(lst_of_element_objects)

#def automatically_defining_elements():
#    list_of_elements = [Element('H', 'Hydrogen', 1.00194), ['He', 'Helium', 4.003], ['Li', 'Lithium', 6.941], ['Be', 'Beryllium', 9.012182], ['','','',''], ['','','',''],['','','',''],['','','',''],['','','',''],['','','',''],['','','',''],['','','',''],['','','',''],['','','',''],['','','',''],['','','',''],['','','',''],['','','',''],['','','',''],['','',''],['','',''],['','','','']]
    
def main():
    lst_of_elements = making_elements()

    print(lst_of_elements['He'].mass)

main()