A = [
[2,3],
[4,7],
]
A = Matrix(A)

C = [ int(input()), int(input()) ]
C = vector(C)

print(A.solve_right(C))
