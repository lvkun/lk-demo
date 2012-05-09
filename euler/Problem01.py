#-------------------------------------------------------------------------------
# Name:        Problem 1
# Purpose:
#       If we list all the natural numbers below 10 
#       that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
#       The sum of these multiples is 23.
#
#       Find the sum of all the multiples of 3 or 5 below 1000.
#
# Link: http://projecteuler.net/index.php?section=problems&id=1
# Author:      brlv
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    print sum([3*i for i in range(0, 334)]) + sum([5*i for i in range(0, 200)]) - sum([15*i for i in range(0, 67)])

    # more simple way
    print (3 + 999) * 333 / 2 + (5 + 995) * 199 / 2 - (15 + 990) * 66 / 2
    
if __name__ == '__main__':
    main()