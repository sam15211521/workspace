import time
import math


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
    number = input('What number do you want to test for all primes:\n\n')
    global start_time 
    start_time= time.time()
    current_number = 5
    lst_of_primes =[2,3,5]
    max_div = math.floor(math.sqrt(int(number)))

    while current_number <= int(number):
        if is_prime_easy(str(current_number)) is True and is_prime_hard(intnumber = max_div, number = str(current_number), lst_of_primes=lst_of_primes) is True:
            lst_of_primes.append(current_number)
            #print(current_number)
            current_number +=2
        else:
            current_number +=2
    i = 0
    final_time = time.time() - start_time, "seconds"
    print(lst_of_primes)
    for prime in lst_of_primes:
        i += 1
    print(f'there are {i} primes between 1 and {number}')
    print(final_time)
    with open(f'C:/Users/sam15/Documents/workspace/prime finder/lst_of_primes/list_of_primes_[{number}].txt', 'w') as file:
        file.write(f'there are {i} primes between 1 and {number}')
        for numb in lst_of_primes:
            file.writelines(f'{str(numb)}\n')
        



main()

