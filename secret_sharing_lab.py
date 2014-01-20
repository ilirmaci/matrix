# version code 988
# Please fill out this stencil and submit using the provided submission script.

import random
from GF2 import one
from vecutil import list2vec, zero_vec
from matutil import listlist2mat
from independence import rank
from itertools import combinations


## Problem 1
def randGF2(): return random.randint(0,1)*one

a0 = list2vec([one, one,   0, one,   0, one])
b0 = list2vec([one, one,   0,   0,   0, one])

def choose_secret_vector(s,t):
    '''(GF2, GF2) -> Vec of GF2
    Return random vector u of length 6 such that a0*u == s, b0*u == t.
    '''
    u = list2vec([randGF2() for i in range(6)])
    
    return u if (a0*u==s) and (b0*u==t) else choose_secret_vector(s,t)



## Problem 2
# Give each vector as a Vec instance

def split_couples(L):
    '''(list) -> list of list
    Return a list of lists containing pairs of entries from L.
    '''
    return [L[i:i+2] for i in range(0, len(L), 2)]
    
def join_couples(L):
    '''(list of list) -> list
    Return a single list containing all elements in its entries in order.
    '''
    lst = []
    for l in L:
        lst.extend(l)
    return lst

secret_a0 = list2vec([one, one,   0, one,   0, one])
secret_b0 = list2vec([one, one,   0,   0,   0, one])

# make initial list of 6 independent vectors
A = [secret_a0, secret_b0]
r = 2
while r < 6:
    v = list2vec([randGF2() for i in range(6)])
    A.append(v)
    temp_rank = rank(A)
    if temp_rank == r+1: 
        r += 1
    else:
        A.remove(v)

while len(A) < 10:
    v1 = list2vec([randGF2() for i in range(6)])
    v2 = list2vec([randGF2() for i in range(6)])
    L = split_couples(A)
    L.append([v1, v2])
    C = combinations(L, 3)
    valid = all([rank(join_couples(i))==6 for i in C])
    if valid:
        A.extend([v1, v2])



secret_a0 = A[0]
secret_b0 = A[1]   
secret_a1 = A[2]
secret_b1 = A[3]
secret_a2 = A[4]
secret_b2 = A[5]
secret_a3 = A[6]
secret_b3 = A[7]
secret_a4 = A[8]
secret_b4 = A[9]
