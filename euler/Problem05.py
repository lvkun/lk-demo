#-------------------------------------------------------------------------------
# Name:        Problem 5
# Purpose:
#              2520 is the smallest number that can be divided by each of the
#              numbers from 1 to 10 without any remainder.
#              What is the smallest positive number that is evenly divisible by
#              all of the numbers from 1 to 20?
# Link:        http://projecteuler.net/index.php?section=problems&id=5
# Author:      brlv
#-------------------------------------------------------------------------------
#!/usr/bin/env python

def divide(num, i):
    ret = 0

    while(num%i == 0):
        num = num/i;
        ret += 1
    return ret

def handle(num, num_list):
    is_prime = True

    # find whether num can be divide by primes
    for i in range(2, num):
        if num_list[i] != 0:
            r = divide(num, i)
            if r > 0:
                is_prime = False
                num_list[i] = max(r,num_list[i])

    if is_prime:
        num_list[num] = 1 

def main():
    num_list = [0 for x in range(0,21)]

    for num in range(2,21):
        handle(num, num_list)

    print num_list

    i = 0
    ret = 1
    for o in num_list:
        ret *= i**o
        i += 1

    print ret


if __name__ == '__main__':
    main()
