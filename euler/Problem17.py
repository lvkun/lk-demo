#-------------------------------------------------------------------------------
# Name:        Problem 17
# Purpose:
#              If the numbers 1 to 5 are written out in words: one, two, three,
#              four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used
#              in total.
#              If all the numbers from 1 to 1000 (one thousand) inclusive were
#              written out in words, how many letters would be used?

#              NOTE: Do not count spaces or hyphens. For example, 342 (three
#              hundred and forty-two) contains 23 letters and 115 (one hundred
#              and fifteen) contains 20 letters. The use of "and" when writing
#              out numbers is in compliance with British usage.
# Link:        http://projecteuler.net/index.php?section=problems&id=17
# Author:      brlv
#-------------------------------------------------------------------------------
#!/usr/bin/env python

numWords = {
    0  : '',
    1  : 'one',
    2  : 'two',
    3  : 'three',
    4  : 'four',
    5  : 'five',
    6  : 'six',
    7  : 'seven',
    8  : 'eight',
    9  : 'nine',
    10 : 'ten',
    11 : 'eleven',
    12 : "twelve",
    13 : "thirteen",
    14 : "fourteen", 
    15 : "fifteen",
    16 : "sixteen", 
    17 : "seventeen", 
    18 : "eighteen",
    19 : "nineteen", 
    20 : "twenty",
    30 : "thirty",
    40 : "forty", 
    50 : "fifty", 
    60 : "sixty",
    70 : "seventy", 
    80 : "eighty", 
    90 : "ninety",
    100 : "hundred", 
    1000 : "thousand"
}

def numToWord(num):
    if num < 20:
        return numWords[num]

    if num < 100:
        ten = num / 10
        rem = num % 10

        return numWords[ten*10] + numWords[rem]

    if num < 1000:
        hun = num / 100
        rem = num % 100

        if rem == 0:
            return numWords[hun] + "hundred"

        return numWords[hun] + "hundredand" + numToWord(rem)

    return "one"+numWords[num]

def main():
    print sum([len(numToWord(i)) for i in range(1, 1001)])

if __name__ == '__main__':
    main()
