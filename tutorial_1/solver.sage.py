

# This file was *autogenerated* from the file solver.sage
from sage.all_cmdline import *   # import sage library

_sage_const_2 = Integer(2); _sage_const_3 = Integer(3); _sage_const_4 = Integer(4); _sage_const_7 = Integer(7)
A = [
[_sage_const_2 ,_sage_const_3 ],
[_sage_const_4 ,_sage_const_7 ],
]
A = Matrix(A)

C = [ int(input()), int(input()) ]
C = vector(C)

print(A.solve_right(C))

