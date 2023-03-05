

# This file was *autogenerated* from the file solver.sage
from sage.all_cmdline import *   # import sage library

_sage_const_128 = Integer(128); _sage_const_0 = Integer(0); _sage_const_1 = Integer(1); _sage_const_2 = Integer(2); _sage_const_0x20 = Integer(0x20); _sage_const_256 = Integer(256)# ref: https://qiita.com/kusano_k/items/5509bff6e426e5043591
M = int(input("M = "))
S = int(input("S = "))

n = _sage_const_128 
S -= int.from_bytes(b"O"*n, "big")

X = [[_sage_const_0 ]*(n+_sage_const_1 ) for _ in range(n+_sage_const_2 )]
for i in range(n):
  X[i][i] = _sage_const_2 
  X[i][n] = _sage_const_0x20 *_sage_const_256 **i*n
for i in range(n):
  X[n][i] = _sage_const_1 
X[n][n] = S*n
X[n+_sage_const_1 ][n] = M*n

X = Matrix(X).LLL()

print(X)
ans = X[_sage_const_1 ]
assert ans[-_sage_const_1 ]==_sage_const_0 
ans = ans[:-_sage_const_1 ]
assert all(a in (-_sage_const_1 , _sage_const_1 ) for a in ans)

ans = "".join("O" if a==_sage_const_1  else "o" for a in ans)[::-_sage_const_1 ]
print(ans)

