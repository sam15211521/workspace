from time import sleep
class Elements:
    number_of_element = 0

    def __init__(self, symbol, name, mass, Z, electronegativity):
        self.name = name
        self.symbol = symbol
        self.mass = mass
        self.atomic_number = Z
        self.electronegativity = electronegativity
        Elements.number_of_element += 1
    
    #def __del__(self):
    #    print(f'Element {self.name} deleted')
    #    Elements.number_of_element -= 1
    
    def compare_electronegativities(element1, element2): # prints out the electronegativities of two elements
        print(f'The elements {element1.name} and {element2.name} have a mass of {element1.electronegativity} and {element2.electronegativity}')
        
    def electronegativities_prompt():
        prompt0.1 = 'This '
        prompt_1.1 = input("what is your first element?")
        prompt_2 = input ('Do you want to do anything else with these elements?\n 1. Exit\n 2. Calculate the electronegativity diffrence and preditct type of chemical bond. \n\n')
        if prompt_2
