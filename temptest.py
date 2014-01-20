from vec import Vec
from mat import Mat
from hw7 import orthogonalize, orthogonal_vec2rep
from solver import solve
from math import sqrt

A = Mat(({0, 1, 2}, {0, 1, 2}), {(0, 1): 1/sqrt(2), (1, 2): 1/sqrt(3), (0, 0): 1/sqrt(2), (1, 1): -1/sqrt(3), (2, 1): 1/sqrt(6), (0, 2): 0, (2, 0): -1/sqrt(6), (2, 2): 2/sqrt(6), (1, 0): 1/sqrt(3)})
b = Vec({0, 1, 2},{0: 10, 1: 20, 2: 30})
x = solve(A, b)
y = orthogonal_vec2rep(A, b)
print(x)
print(y)
