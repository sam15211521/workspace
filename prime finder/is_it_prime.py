def is_prime_easy(number):
    snum = number
    sendnum = snum[-1]
    if sendnum in ['0','2','4','5','6','8']:

        return False
    else:
        n_sum = 0
        for n in snum:
            n_sum += int(n)
        if n_sum % 3 ==0:

            return False
        else:
            return True

def is_prime_hard(intnumber, number, lst_of_primes= []):
        
    for num in lst_of_primes:
        if num <= intnumber:
            if int(number) % num == 0:

                return False

    return True

def main():
    num = input('What number do you want to find?\n\n')
    for numb in range(1,int(num)+1):
        if numb <= 

main()