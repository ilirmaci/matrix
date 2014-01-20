from mat import *
from vec import *
from cancer_data import *

features, diagnosis = read_training_data("train.data")

## Task 1 ##
def signum(u):
    '''
    Input:
        - u: Vec
    Output:
        - v: Vec such that:
            if u[d] >= 0, then v[d] =  1
            if u[d] <  0, then v[d] = -1
    Example:
        >>> signum(Vec({1,2,3},{1:2, 2:-1})) == Vec({1,2,3},{1:1,2:-1,3:1})
        True
    '''
    return Vec(u.D, {k:1 if u[k]>=0 else -1 for k in u.D})

## Task 2 ##
def fraction_wrong(A, b, w):
    '''
    Input:
        - A: a Mat with rows as feature vectors
        - b: a Vec of actual diagnoses
        - w: hypothesis Vec
    Output:
        - Fraction (as a decimal in [0,1]) of vectors incorrectly
          classified by w 
    '''
    b_hat = signum(A*w)
    e = b - b_hat # e=0 if diagnoses match, 2 or -2 otherwise
    return (e*e)/(4*len(b.D))


## Task 3 ##
def loss(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of loss function at w for training data
    '''
    e = A*w - b 
    return e*e

## Task 4 ##
def find_grad(A, b, w):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
    Output:
        - Value of the gradient function at w
    '''
    return 2*(A*w - b)*A

## Task 5 ##
def gradient_descent_step(A, b, w, sigma):
    '''
    Input:
        - A: feature Mat
        - b: diagnoses Vec
        - w: hypothesis Vec
        - sigma: step size
    Output:
        - The vector w' resulting from 1 iteration of gradient descent
          starting from w and moving sigma.
    '''
    return w - sigma*find_grad(A, b, w)


def gradient_descent(A, b, w, sigma, T):
    '''
    Return hypothesis vector w after running 
    gradient_descent_step(A,b,w,sigma) T times
    '''
    for i in range(T):
        w = gradient_descent_step(A, b, w, sigma)
    return w
    
    
    
