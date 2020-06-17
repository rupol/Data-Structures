import math
from math import sqrt

# constant time O(1) or O(c)
def mult_2(n):
    print(n) # O(1)
    return n*2 # O(1)
    # O(1) + O(1) = O(2)
    # constant, so can simplify to O(2)

# linear time O(n)
def foo(n):
    for i in range(0, n): # O(n)
        # the total runtime of code in the loop is O(1)
        print(i) # O(1)

# quadratic (polynomial) time
def bar(n): # O(1) + O(n^2) + O(1)
    s = 0 # O(1)

    # this loop has a runtime of O(n) * O(n) = O(n^2)
    for i in range(0, n): # O(n)
        # this loop has a run time of O(n) * O(1) = O(n)
        for j in range(0, n): # O(n)
            s += i * j # O(1)
    return s #O(1)

# also a variant of O(n) * log(n)
def baz(n): # O(n) + O(sqrt(n)) == O(n * sqrt(n)) == O(n^1.5)
    s = 0

    for i in range(n): # O(n)
        for j in range(int(sqrt(n))): # O(sqrt(n)) or O(n ^ 0.5)
            s += i * j # O(1)
    
    return s

# O(log(n))
def divider(n):
    while n >= 1:
        print(n) # O(1)
        n = n/2 # O(1)

# if n = 8, will run 3 times; 16 -> 4 steps; 32 -> 5
# doubling n results in linear increase in run time
# this is sublinear, or logarithmic