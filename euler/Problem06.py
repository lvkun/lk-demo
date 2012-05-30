#-------------------------------------------------------------------------------
# Name:        Problem 6
# Purpose:
#              The sum of the squares of the first ten natural numbers is,
#              1^2 + 2^2 + ... + 10^2 = 385
#              The square of the sum of the first ten natural numbers is,
#              (1 + 2 + ... + 10)^2 = 55^2 = 3025
#              Hence the difference between the sum of the squares of the
#              first ten natural numbers and the square of the sum is
#              3025 - 385 = 2640.
#              Find the difference between the sum of the squares of the first
#              one hundred natural numbers and the square of the sum.
# Link:        http://projecteuler.net/index.php?section=problems&id=6
# Author:      brlv
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    r = 100
    print sum([x for x in range(1, r+1)])**2 - sum([x**2 for x in range(1, r+1)])

    # n(n+1)(2n+1)/6
    print (r*(r+1)/2) ** 2 - r*(r+1)*(2*r+1)/6 

if __name__ == '__main__':
    main()
