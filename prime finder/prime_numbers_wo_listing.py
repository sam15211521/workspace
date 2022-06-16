import time



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

def is_prime_hard(number,lst_of_primes= []):

    for num in lst_of_primes:
        if int(number) % num == 0:

            return False

    return True
    

def main():
    number = input('What number do you want to test for all primes:\n\n')
    global start_time 
    start_time= time.time()
    current_number = 5
    lst_of_primes =[2,3,5]
    prime_count = 0

    while current_number <= int(number):
        if is_prime_easy(str(current_number)) is True and is_prime_hard(str(current_number), lst_of_primes=lst_of_primes) is True:
            lst_of_primes.append(current_number)
            prime_count += 1
            current_number +=1
        else:
            current_number +=1

    
    print(prime_count)
    print(time.time() - start_time, "seconds")

        
    # while i <= inum/2:
    #     print(i)
    #     i += 2


main()

