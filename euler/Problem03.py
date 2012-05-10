#-------------------------------------------------------------------------------
# Name:        Problem 3
# Purpose:
#       The prime factors of 13195 are 5, 7, 13 and 29.
#
#       What is the largest prime factor of the number 600851475143 ?
#
# Link: http://projecteuler.net/index.php?section=problems&id=3
# Author:      brlv
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def main():
    remain = 600851475143
    prime = 3
    
    while prime < remain:
        prime += 2

        while remain % prime == 0:
            remain = remain / prime

    print remain, prime

if __name__ == '__main__':
    main()