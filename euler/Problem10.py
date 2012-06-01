#-------------------------------------------------------------------------------
# Name:        Problem 10
# Purpose:
#              The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
#              Find the sum of all the primes below two million.
# Link:        http://projecteuler.net/index.php?section=problems&id=10
# Author:      brlv
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def isPrime(num, primes):

    for i in primes:
        if i > num**0.5:
            primes.append(num)
            return True
        if num%i == 0:
            return False

def main():
    primes = [2]
    for num in range(3, 1999999):
        isPrime(num, primes)

    print sum(primes)

if __name__ == '__main__':
    main()
