#-------------------------------------------------------------------------------
# Name:        Problem 16
# Purpose:
#              2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
#              What is the sum of the digits of the number 2^1000?
# Link:        http://projecteuler.net/index.php?section=problems&id=16
# Author:      brlv
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    #for i in range(1, 100):
    #    print (2**i/10)%10

    print sum( [int(i) for i in str(2**1000)] )

if __name__ == '__main__':
    main()
