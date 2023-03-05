# ref: https://qiita.com/kusano_k/items/5509bff6e426e5043591
M = int(input("M = "))
S = int(input("S = "))

n = 128
S -= int.from_bytes(b"O"*n, "big")

X = [[0]*(n+1) for _ in range(n+2)]
for i in range(n):
  X[i][i] = 2
  X[i][n] = 0x20*256**i*n
for i in range(n):
  X[n][i] = 1
X[n][n] = S*n
X[n+1][n] = M*n

X = Matrix(X).LLL()

print(X)
ans = X[1]
assert ans[-1]==0
ans = ans[:-1]
assert all(a in (-1, 1) for a in ans)

ans = "".join("o" if a==1 else "O" for a in ans)[::-1]
print(ans)
