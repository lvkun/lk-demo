{

# Python Simple Tutorial 

Bruce Lv 

(bruce.lv@nokia.com)

}

{x=1000; rotate-y=-10;

## First Impression

* productivity
  * much shorter than C
* readability
  * indent

}

{x=800; y=250; scale=0.5; rotate-y=-10;

## About language

* Dynamic Typing/Interpreted language
* Object Oriented
* Extensible/Embeddable
* Extensive Libraries

}

{x=1300; y=250; scale=0.5; rotate-y=-10;

## Usage

* Web
* Scientific Computing
* Scripting Language
* GUI
* ...

A great language for daily work.

}

{x=2000; rotate-y=-20;

## Hello world

    print "hello world!" 

Or in python 3.x:

    print("hello world!")

}

{x=2000; Y=500; rotate-y=-20;

## Control

    times = raw_input("How many times you exercise every week?")
    if times == 0:
        print "Common on! You need more exercise!"
    elif times < 3:
        print "Good! But you can still take more!"
    elif times < 6:
        print "Excellent! Keep it!"
    elif:
        print "Maybe you need rest!"

}

{x=2000; Y=1000; rotate-y=-20;

## Loop

### for

    fruit_list = ["apple", "banana", "orange"]
    for fruit in fruit_list:
        if fruit == "banana":
            print "Found banana"
            break;

### while

    minutes = 0
    while(minutes < 60):
        print "continue run"
        minutes += 1

}

{x=3000; rotate-y=-30;
## Data Struture

* List 
* Dictionary
* Others...

}

{x=3000; y=500; rotate-y=-30;

### List (1)

* Not need the same type

        li = ['spam', 'eggs', 100, 1234]

* Index start from 0

        li[0] # 'spam'

* Slice

        li[1:3] # ['eggs', 100]

* Concatenate

        li[:2] + ['bacon', 2*2] # ['spam', 'eggs', 100, 1234]

}

{x=3000; y=1000; rotate-y=-30;

### List (2)

    li = [0, 1]

* append

        li.append(2) # [0, 1, 2]

* extend

        li.extend([3, 4]) # [0, 1, 2, 3, 4]

* insert

        li.insert(2, 5) # [0, 1, 5, 2, 3, 4]

* sort
        
        li.sort() # [0, 1, 2, 3, 4, 5]

* remove

        li.remove(3) # [0, 1, 2, 4, 5]

}

{x=3000; y=1500; rotate-y=-30;

### Dictionary

unordered set of key: value pairs

* create 
        
        seats = {'Chao':5307, 'Bruce':5306} # {'Bruce': 5306, 'Chao': 5307}

* add

        seats['Kevin'] = 5305 # {'Bruce': 5306, 'Chao': 5307, 'Kevin': 5305}

* get value

        seats['Bruce'] # 5306

* delete

        del seats['Chao'] # {'Bruce': 5306, 'Kevin': 5305}

* check

        'Bruce' in seats # True

}

{x=3000; y=2000; rotate-y=-30;

### Others

* String
* Set
* Tuple

}

{x=4000; rotate-y=-40;

### Function

* define

        def fib(n): 
            a, b = 0, 1
            while a < n:
                print a,
                a, b = b, a+b

* use

        fib(1000)

}

{x=5000; rotate-y=-50;

### Class

* define

        class Employee:
            def __init__(self, name):
                self.name = name

            def work(self):
                print self.name + " is working"

* use

        bruce = Employee("Bruce")
        bruce.work()

}

{x=5000; y=700; rotate-y=-50;

### Class - Inheritance

* define

        class Programmer(Employee):
            def work(self):
                print self.name + " is writing code"

        class Tester(Employee):
            def work(self):
                print self.name + " is looking for bugs"

* use

        bruce = Programmer("Bruce")
        bruce.work()

        shiwei = Tester("shiwei")
        shiwei.work()

}

{x=6000; rotate-y=-60;

### Unittest

        import random
        import unittest

        class TestSequenceFunctions(unittest.TestCase):
            
            def setUp(self):
                self.seq = range(10)

            def testshuffle(self):
                # make sure the shuffled sequence does not lose any elements
                random.shuffle(self.seq)
                self.seq.sort()
                self.assertEqual(self.seq, range(10))

            def testchoice(self):
                element = random.choice(self.seq)
                self.assert_(element in self.seq)

            def testsample(self):
                self.assertRaises(ValueError, random.sample, self.seq, 20)
                for element in random.sample(self.seq, 5):
                    self.assert_(element in self.seq)

        if __name__ == '__main__':
            unittest.main()

}

{x=7000; rotate-y=-70;

### Reference

* [The Python Tutorial]
* [A Byte of Python]

[The Python Tutorial]: http://docs.python.org/tutorial/index.html
[A Byte of Python]: http://www.swaroopch.org/notes/Python

}