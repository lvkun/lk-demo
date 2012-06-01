#-------------------------------------------------------------------------------
# Name:        Problem 9
# Purpose:
#              A Pythagorean triplet is a set of three natural numbers,
#              a < b < c, for which, a^2 + b^2 = c^2
#              For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
#              There exists exactly one Pythagorean triplet for
#              which a + b + c = 1000.
#              Find the product abc.
# Link:        http://projecteuler.net/index.php?section=problems&id=9
# Author:      brlv
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def brute():
    for a in range(1, 501):
        for b in range(a, 501):
            c = 1000 - a - b

            if (c**2 == b**2 + a**2):
                print a,b,c
                print a*b*c

def main():
    brute()

if __name__ == '__main__':
    main()
