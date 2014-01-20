from vec import Vec
from GF2 import one

from factoring_support import dumb_factor
from factoring_support import intsqrt
from factoring_support import gcd
from factoring_support import primes
from factoring_support import prod

import echelon

def root_method(N):
    '''(int) -> int
    Return first integer that is equal to sqrt(a*a - N), where a is
    another integer greater than sqrt(N).
    >>> root_method(77)
    2
    '''
    a = intsqrt(N)
    if a*a < N:
        a += 1
    while True:
        diff = a*a - N
        b = intsqrt(diff)
        if b*b == diff:
            return a-b
        a += 1
        
def is_prime(p, n=25):
    '''
    Return True if p is prime for non-Charmichael numbers 
    with false positive probability 1/2^n. 
    '''
    from random import randint
    return all([pow(randint(1, p-1), p-1, p) == 1 for i in range(n)])
   
## Task 1
def int2GF2(i):
    '''
    Returns one if i is odd, 0 otherwise.

    Input:
        - i: an int
    Output:
        - one if i is congruent to 1 mod 2
        - 0   if i is congruent to 0 mod 2
    Examples:
        >>> int2GF2(3)
        one
        >>> int2GF2(100)
        0
    '''
    return one if i % 2 == 1 else 0

## Task 2
def make_Vec(primeset, factors):
    '''
    Input:
        - primeset: a set of primes
        - factors: a list of factors [(p_1,a_1), ..., (p_n, a_n)]
                   with p_i in primeset
    Output:
        - a vector v over GF(2) with domain primeset
          such that v[p_i] = int2GF2(a_i) for all i
    Example:
        >>> make_Vec({2,3,11}, [(2,3), (3,2)]) == Vec({2,3,11},{2:one})
        True
    '''
    return Vec(primeset, {p:int2GF2(a) for (p, a) in factors})

## Task 3
def find_candidates(N, primeset):
    '''
    Input:
        - N: an int to factor
        - primeset: a set of primes

    Output:
        - a list [roots, rowlist]
        - roots: a list a_0, a_1, ..., a_n where a_i*a_i - N can be factored
                 over primeset
        - rowlist: a list such that rowlist[i] is a
                   primeset-vector over GF(2) corresponding to a_i
          such that len(roots) = len(rowlist) and len(roots) > len(primeset)
    '''
    n = len(primeset) + 1
    x = intsqrt(N) + 2
    roots = []
    rowlist = []
    
    while len(roots) < n:
        diff = x*x - N
        factors = dumb_factor(diff, primeset)
        if factors != []:
            roots.append(x)
            rowlist.append(make_Vec(primeset, factors))
        x += 1
    return (roots, rowlist)
    



## Task 4
def find_a_and_b(v, roots, N):
    '''
    Input: 
     - a {0,1,..., n-1}-vector v over GF(2) where n = len(roots)
     - a list roots of integers
     - an integer N to factor
    Output:
      a pair (a,b) of integers
      such that a*a-b*b is a multiple of N
      (if v is correctly chosen)
    '''
    a_factors = [roots[i] for i in v.f if v[i] == one] 
    a = prod(a_factors)
    c_factors = [x*x - N for x in a_factors]
    c = prod(c_factors)
    b = intsqrt(c)
    assert b*b == c, "a*a - N is not a perfect square"
    return(a, b)


## Task 5
if __name__ == "__main__":
    primelist = primes(10000)
    N = 2461799993978700679
    (roots, rowlist) = find_candidates(N, primelist)
    M = echelon.transformation_rows(rowlist, sorted(primelist, reverse=True))

    divisor = N #starting at the largest possible divisor
    for i in range(2,20):
        v = M[-i]
        (a, b) = find_a_and_b(v, roots, N)
        x = gcd(a-b, N)
        if x < divisor and x != 1: divisor = x
        if N//x < divisor and x != N: divisor = N//x
    print("The smallest found divisor is: {0}".format(divisor))
smallest_nontrivial_divisor_of_2461799993978700679 = 1230926561






