#-------------------------------------------------------------------------------
# Name:        Problem 14
# Purpose:
#              The following iterative sequence is defined for the set of
#              positive integers:
#              n -> n/2 (n is even)
#              n -> 3n + 1 (n is odd)
#              Using the rule above and starting with 13, we generate the
#              following sequence:
#              13 -> 40 -> 20 -> 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
#              It can be seen that this sequence (starting at 13 and finishing
#              at 1) contains 10 terms. Although it has not been proved yet
#              (Collatz Problem), it is thought that all starting numbers
#              finish at 1.
#              Which starting number, under one million, produces the longest
#              chain?
#              NOTE: Once the chain starts the terms are allowed to go above
#              one million.
# Link:        http://projecteuler.net/index.php?section=problems&id=14
# Author:      brlv
#-------------------------------------------------------------------------------
#!/usr/bin/env python

cache = {}

def getChain(num):
    
    ret = 0

    if num == 1:
        return 0

    if num in cache:
        return cache[num]

    if num % 2 == 0:
        ret = getChain(num/2) + 1
    else:
        ret = getChain(3*num + 1)+1

    cache[num] = ret  
    return ret

def Search(list):
    genList = []

    for i in list:
        
        numbers[i] = 1
        
        if i*2 < 1000000 and numbers[i*2] == 0:
            genList.append(i*2)

        if i*2 > 1000000 and (i*2-1)%3 == 0 and (i*2-1)/3 < 1000000 and numbers[i*2] == 0:
            genList.append(i*2)        

        if (i-1)%3 == 0 and ((i-1)/3)%2 == 1 and numbers[(i-1)/3] == 0:
            genList.append((i-1)/3)

    return genList


def main():
    list = [2]
    index = 0

    maxChains = 0
    maxIndex = 0
    for i in range(1, 1000001):
        
        print i
        chains = getChain(i)

        if maxChains < chains:
            maxChains = chains
            maxIndex = i
    
    print "max:    " + str(maxIndex)

if __name__ == '__main__':
    main()
