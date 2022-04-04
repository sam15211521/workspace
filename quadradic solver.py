
def main(A= int(input("A")), B = int(input("B")), C = int(input('C'))):
    positive = (-B +(B**2 -4*A*C)**(1/2))/(2*A)
    negative = (-B -(B**2 -4*A*C)**(1/2))/(2*A)

    value = f"{positive}     or    {negative}"
    print()
    print(value)
    print()

    print(A*positive**2 + B*positive + C)


main()