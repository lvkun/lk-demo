#-------------------------------------------------------------------------------
# Name:        Problem 7
# Purpose:
#              By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
#              we can see that the 6th prime is 13.
#              What is the 10001st prime number?
# Link:        http://projecteuler.net/index.php?section=problems&id=7
# Author:      brlv
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def isPrime(num, primes):
    for i in primes:
        if num%i == 0:
            return False
        if i > num**0.5:
            break

    primes.append(num)
    return True

def brute():
    # solve problem in brute way.
    primes = []
    count = 0
    for num in range(3, 100000000, 2):
        if isPrime(num, primes):
            count += 1
            if count > 9999:
                print ' 10001st prime is ' + str(num)
                break

from math import log

def sieve():
    # solve problem with sieve of Eratosthenes
    num_of_primes = 120000.0/log(120000.0)
    print "below %d there should be about %f primes" % (120000, num_of_primes)
    
    numbers = [0 for x in range(0,120000)]
    count = 0
    prime_index = 2
    while prime_index < 120000:
        count += 1

        if count > 10000:
            break;

        numbers[prime_index] = 1

        mul = 0
        while (prime_index+mul)*prime_index < 120000:
            numbers[(prime_index+mul)*prime_index] = 1
            mul += 1

        while numbers[prime_index] == 1:
            prime_index += 1
            
    print ' 10001st prime is ' + str(prime_index)

def main():
    brute()
    sieve()

if __name__ == '__main__':
    main()
