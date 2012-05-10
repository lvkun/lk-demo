#-------------------------------------------------------------------------------
# Name:        Problem 4
# Purpose:
#          A palindromic number reads the same both ways. The largest
#          palindrome made from the product of two 2-digit numbers
#          is 9009 = 91*99.

#          Find the largest palindrome made from the product
#          of two 3-digit numbers.
#
# Link: http://projecteuler.net/index.php?section=problems&id=4
# Author:      brlv
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def is_palindromic(num):
    for i in range(0,3):
        if (num/(10**i)%10 != num/(10**(5-i))%10):
            return False
    return True

def main():
    for a1 in range(999,900,-1):
        for a2 in range(999,900,-1):
            if is_palindromic(a1*a2):
                print a1*a2
                return

if __name__ == '__main__':
    main()
