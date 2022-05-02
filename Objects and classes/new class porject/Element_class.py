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
    
    def compare_electronegativities(element1, element2): # prints out the electronegativities of two elements as well as the type of bond they form
        
        name1 = eval(f'{element1}.name')
        name2 = eval(f'{element2}.name')
        electro1 = eval(f'{element1}.electronegativity')
        electro2 = eval(f'{element2}.electronegativity')
        electrodiff = abs(electro1-electro2)
        
        if electrodiff < 0.4:           # determines the type of bond
            type_of_bond = 'non-polar covalent'
        if electrodiff >= 0.4 and electrodiff <= 1.8:
            type_of_bond = 'polar covalent'
        if electrodiff > 1.8:
            type_of_bond = 'ionic'
        
        print(f'\nThe elements {name1} and {name2} have an electronegativity of {electro1} and {electro2} respectivly\nAs well as an electronegativity difrence of {electrodiff}, making the bond {type_of_bond}\n')
    
    def finding_elements_symbols_by_name(element_name='Hydrogen'): #returns the string symbol of the element chosen
        for ele in element_list:
            if element_name == ele.name:
                return ele.symbol
            else:
                continue

    def finding_elements_name_by_symbol(element_symbol = 'Hydrogen'): #returns the string name of the element chosen
        for ele in element_list:
            if element_symbol == ele.symbol:
                return ele.name
            else:
                continue

    def calling_atomic_number(element_name = 'None', element_symbol = 'N/a'):
        for element in element_list:
            if element_name == element.name or element_symbol == element.symbol:
                return element.atomic_number

    def calling_atomic_mass(element_name = 'None', element_symbol = 'N/a'):
        for element in element_list:
            if element_name == element.name or element_symbol == element.symbol:
                return element.mass
        
    def calling_electronegativity(element_name = 'None', element_symbol = 'N/a'):
        for element in element_list:
            if element_name == element.name or element_symbol == element.symbol:
                return element.atomic_number

    #def element_look_up(elementname, elementsymbol):

### below are the diffrent elements of the periodic table

H = Elements('H', 'Hydrogen', 1.01, 1, 2.20)

He = Elements('He','Helium',4.003,2, 0)

Li = Elements('Li', 'Lithium', 6.941, 3, 0.98)

Be = Elements('Be', 'Berylium' ,9.012182 , 4, 1.57)

B = Elements('B', 'Boron' , 10.811, 5, 2.04)

C = Elements('C', 'Carbon' ,12.0107 , 5, 2.55)

N = Elements('N', 'Nitrogen' , 14.00674, 7, 2.04)

O = Elements('O', 'Oxygen' , 15.9994, 8, 3.44)

F = Elements('F', 'Florine' , 18.9984032, 9, 3.98)

Ne = Elements('Ne', 'Neon' , 20.1797, 10, 0)

Na = Elements('Na', 'Sodium' , 22.989770, 11, 0.93)

Mg = Elements('Mg', 'Magnesium' , 24.3050, 12, 1.31)

Al = Elements('Al', 'Alumnium' ,26.981538 , 13, 1.61)

Si = Elements('Si', 'Silicon' , 28.0855, 14, 1.90)

P = Elements('P', 'Phosphorus' , 30.973761, 15, 2.19)

S  = Elements('S', 'Sulfur' ,32.066 , 16, 2.58)

Cl = Elements('Cl', 'Chlorine' , 35.4527, 17, 3.16)

Ar = Elements('Ar', 'Argon' , 39.948, 18, 0)

K = Elements('K', 'Potassium' , 39.1983, 19, 0.82)

Ca = Elements('Ca', 'Calcium' , 40.078, 20, 1.00)

Sc = Elements('Sc', 'Scandium' , 44.955910, 21, 1.36)

Ti = Elements('Ti', 'Titanium' , 47.867, 22, 1.54)

V = Elements('V', 'Vanadium' , 50.9415, 23, 1.63)

Cr = Elements('Cr', 'Chromium' , 51.9961, 24, 1.66)

Mn = Elements('Mn', 'Manganese' , 54.938049, 25, 1.55)

Fe = Elements('Fe', 'Iron' , 55.845, 26, 1.83)

Co = Elements('Co', 'Cobalt' , 58.933200, 27, 1.88)

Ni = Elements('Ni', 'Nickel' ,58.6934 , 28, 1.91)

Cu = Elements('Cu', 'Copper' , 63.546, 29, 1.90)

Zn = Elements('Zn', 'Zinc' , 65.39, 30, 1.65)

Ga = Elements('Ga', 'Gallium' , 69.723, 31, 1.81)

Ge = Elements('Ge', 'Germanium' , 72.61, 32, 2.01)

As = Elements('As', 'Arsenic' , 74.2160, 33, 2.18)

Se = Elements('Se', 'Selenium' , 78.96, 34, 2.55)

Br = Elements('Br', 'Bromine' , 79.904, 35, 2.96)

Kr = Elements('Kr', 'Krypton' , 83.80, 36, 3.00)

Rb = Elements('Rb', 'Rubidium' , 85.4678, 37, 0.82)

Sr = Elements('Sr', 'Strontium' , 87.62, 38, 0.95)

Y = Elements('Y', 'Yittrium' , 88.90585, 39, 1.22)

Zr = Elements('Zr', 'Zirconium' , 91.224, 40, 1.33)

Nb = Elements('Nb', 'Niobium' , 92.90638, 41, 1.6)

Mo = Elements('Mo', 'Molybdenum' , 95.94, 42, 2.16)

Tc = Elements('Tc', 'Technetium' , 98, 43, 1.9)

Ru = Elements('Ru', 'Ruthenium' , 101.07, 44, 2.2)

Rh = Elements('Rh', 'Rhodium' , 102.90550, 45, 2.28)

Pd = Elements('Pd', 'Palladium' , 106.42, 46, 2.20)

Ag = Elements('Ag', 'Silver' , 107.8682, 47, 1.93)

Cd = Elements('Cd', 'Cadmium' , 112.411, 48, 1.69)

In = Elements('In', 'Indium' , 114.818, 49, 1.78)

Sn = Elements('Sn', 'Tin' , 119.710, 50, 1.96)

Sb = Elements('Sb', 'Antimony' , 121.760, 51, 2.05)

Te = Elements('Te', 'Tellurium' , 127.60, 52, 2.1)

I = Elements('Ru', 'Iodine' , 126.90447, 53, 2.66)

Xe = Elements('Xe', 'Xenon' , 131.29, 54, 2.6)

Cs = Elements('Cs', 'Cesium' , 132.90545, 55, 0.79)

Ba = Elements('Ba', 'Barium' , 137.327, 56, 0.89)

La = Elements('La', 'Lanthum' , 138.9055, 57, 1.10)

Ce = Elements('Ce', 'Cerium' , 140.116, 58, 1.12)

Pr = Elements('Pr', 'Praseodymium' , 140.90765, 59, 1.13)

Nd = Elements('Nd', 'Neodymium' , 144.24, 60, 1.14)

Pm = Elements('Pm', 'Promethium' , 145, 61, 1.13)

Sm = Elements('Sm', 'Samarium' , 150.36, 62, 1.17)

Eu = Elements('Eu', 'Europium' , 151.964, 63, 1.2)

Gd = Elements('Gd', 'Gadolinium' , 157.25, 64, 1.2)

Tb = Elements('Tb', 'Terbium' , 158.92534, 65, 1.22)

Dy = Elements('Dy', 'Dysprosium' , 162.50, 66, 1.23)

Ho = Elements('Ho', 'Holmium' , 164.93032, 67, 1.24)

Er = Elements('Er', 'Erbium' , 167.26, 68, 1.24)

Tm = Elements('Tm', 'thulium' , 168.93421, 69, 1.25)

Yb = Elements('Yb', 'Ytterbium' , 173.04, 70, 1.1)

Lu = Elements('Lu', 'Lutetium' , 174.967, 71, 1.27)

Hf = Elements('Hf', 'Hafnium' , 178.49, 72, 1.3)

Ta = Elements('Ta', 'Tantalum' , 180.9479, 73, 1.5)

W= Elements('W', 'Tungsten' , 183.84, 74, 2.36)

Re = Elements('Re', 'Rhenium' , 186.207, 75, 1.9)

Os = Elements('Os', 'Osmium' , 190.23, 76, 2.2)

Ir = Elements('Ir', 'Iridium' , 192.217, 77, 2.2)

Pt = Elements('Pt', 'Platinum' , 195.078, 78, 2.28)

Au = Elements('Au', 'Gold' , 196.96655, 79, 2.54)

Hg = Elements('Hg', 'Mercury' , 200.59, 80, 2.00)

Tl = Elements('Tl', 'Thallium' , 204.3833, 81, 1.62)

Pb = Elements('Pb', 'Lead' , 207.2, 82, 2.33)

Bi = Elements('Bi', 'Bismuth' , 208.98038, 83, 2.02)

Po = Elements('Po', 'Polonium' , 209, 84, 2.0)

At = Elements('At', 'Astatine' , 210, 85, 2.2)

Rn = Elements('Rn', 'Radon' , 222, 86, 0)

Fr = Elements('Fr', 'Francium' , 223, 87, 0.7)

Ra = Elements('Ra', 'Radium' , 226, 88, 0.89)

Ac = Elements('Ac', 'Actinium' , 227, 89, 1.1)

Th = Elements('Th', 'Thorium' , 232.0381, 90, 1.3)

Pa = Elements('Pa', 'Protactinium' , 231.03588, 91, 1.5)

U = Elements('U', 'Uranium' , 238.0289, 92, 1.38)

Np = Elements('Np', 'Neptunium' , 237, 93, 1.38)

Pu = Elements('Pu', 'Plutonium' , 244, 94, 1.28)

Am = Elements('Am', 'Americium' , 243, 95, 1.3)

Cm = Elements('Cm', 'Curium' , 247, 96, 1.3)

Bk = Elements('Bk', 'Berkelium' , 247, 97, 1.3)

Cf = Elements('Cf', 'Californium' , 251, 98, 1.3)

element_list =[H, He, Li, Be, B, C, N, O, F, Ne, Na, Mg, Al, Si, P, S, Cl, Ar, K, Ca, Sc, Ti, V, Cr, Mn, Fe, Co, Ni, Cu, Zn, Ga, Ge, As, Se, Br, Kr, Rb, Sr, Y, Zr, Nb, Mo, Tc, Ru, Rh, Pd, Ag, Cd, In, Sn, Sb, Te, I, Xe, Cs, Ba, La, Ce, Pr, Nd, Pm, Sm, Eu, Gd, Tb, Dy, Ho, Er, Tm, Yb, Lu, Hf, Ta, W, Re, Os, Ir, Pt, Au, Hg, Tl, Pb, Bi, Po, At, Rn, Fr, Ra, Th, Pa, U , Np, Pu, Am, Cm, Bk, Cf]

#for abc in element_list:
#    print(abc.name)


chosen = Elements.finding_elements_symbols_by_name('Hydrogen')

print(eval(f'{chosen}.electronegativity'))

Elements.compare_electronegativities('Na', 'Cl')

print(Elements.calling_atomic_number( element_symbol= 'Br'))