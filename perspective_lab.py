from image_mat_util import *

from mat import Mat
from vec import Vec

from solver import solve
from matutil import rowdict2mat, mat2coldict, coldict2mat

## Task 1
def move2board(v): 
    '''
    Input:
        - v: a vector with domain {'y1','y2','y3'}, the coordinate representation of a point q.
    Output:
        - A {'y1','y2','y3'}-vector z, the coordinate representation
          in whiteboard coordinates of the point p such that the line through the 
          origin and q intersects the whiteboard plane at p.
    '''
    return Vec({'y1','y2','y3'}, {k:v[k]/v['y3'] for k in {'y1','y2','y3'}})

## Task 2
def make_equations(x1, x2, w1, w2): 
    '''
    Input:
        - x1 & x2: photo coordinates of a point on the board
        - y1 & y2: whiteboard coordinates of a point on the board
    Output:
        - List [u,v] where u*h = 0 and v*h = 0
    '''
    domain = {(a, b) for a in {'y1', 'y2', 'y3'} for b in {'x1', 'x2', 'x3'}}
    u = Vec(domain, {('y3','x1'):w1*x1, ('y3','x2'):w1*x2, ('y3','x3'):w1,
                     ('y1','x1'):-x1, ('y1','x2'):-x2, ('y1','x3'):-1})
    v = Vec(domain, {('y3','x1'):w2*x1, ('y3','x2'):w2*x2, ('y3','x3'):w2,
                     ('y2','x1'):-x1, ('y2','x2'):-x2, ('y2','x3'):-1})
    return [u, v]


## Task 3
y_dom = {'y1', 'y2', 'y3'}
x_dom = {'x1', 'x2', 'x3'}
domain = {(a, b) for a in y_dom for b in x_dom}
l8 = Vec(domain, {('y1','x1'):1})
L = rowdict2mat(make_equations(358, 36, 0, 0) + 
                make_equations(329, 597, 0, 1) + 
                make_equations(592, 157, 1, 0) + 
                make_equations(580, 483, 1, 1) + [l8])
b = Vec(set(range(9)), {8:1})
h = solve(L, b)
H = Mat((y_dom, x_dom), {(a,b):h[a,b] for a in y_dom for b in x_dom})

## Task 4
def mat_move2board(Y):
    '''
    Input:
        - Y: Mat instance, each column of which is a 'y1', 'y2', 'y3' vector 
          giving the whiteboard coordinates of a point q.
    Output:
        - Mat instance, each column of which is the corresponding point in the
          whiteboard plane (the point of intersection with the whiteboard plane 
          of the line through the origin and q).
    '''
    Y_cols = list(mat2coldict(Y).values())
    for i in range(len(Y_cols)):
        Y_cols[i] = move2board(Y_cols[i])
    return coldict2mat(Y_cols)
    
    
    
