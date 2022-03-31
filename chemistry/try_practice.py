from msilib.schema import Error


def try_program():
    while True:
        try:
            a = input('Please enter a number')
            b = int(a)/2
        except Exception:
            print("there was an error in the program")
        else:
            return b


def main():
    while True:
        try:
            print(try_program())
            break
        except Exception:
            print('there was an error')
            continue


main()