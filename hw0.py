# Please fill out this stencil and submit using the provided submission script.





## Problem 1
def myFilter(L, num): return [x for x in L if x % num != 0]



## Problem 2
def myLists(L): return [[i+1 for i in range(x)] for x in L]



## Problem 3
def myFunctionComposition(f, g): return {k:g[f[k]] for k in f}


## Problem 4
# Please only enter your numerical solution.

complex_addition_a = 5 + 3j 
complex_addition_b = 1j
complex_addition_c = -1 + 0.001j
complex_addition_d = 0.001 + 9j



## Problem 5
GF2_sum_1 = 1
GF2_sum_2 = 0
GF2_sum_3 = 0


## Problem 6
def mySum(L):
    '''(list of number) -> number
    Return sum of elements of L.
    '''
    sum = 0
    for x in L:
        sum = sum + x
    return sum


## Problem 7
def myProduct(L):
    '''(list of number) -> number
    Return product of elements of L.
    '''
    product = 1 if len(L) > 0 else 0
    for x in L:
        product = product * x
    return product


## Problem 8
def myMin(L):
    '''(list of number) -> number
    Return minimum of elements of L.
    
    Prerequisite: len(L) > 0
    '''
    assert len(L) > 0, "List must have at least one element"
    minimum = L[0]
    for x in L[1:]:
        if x < minimum:
            minimum = x
    return minimum



## Problem 9
def myConcat(L):
    '''(list of str) -> str
    Return concatenation of elements of L.
    '''
    concat = ""
    for x in L:
        concat = concat + x
    return concat



## Problem 10
def myUnion(L):
    '''(list of set) -> set
    Return union of elements of L.
    '''
    union = set()
    for x in L:
        union.update(x)
    return union
    

