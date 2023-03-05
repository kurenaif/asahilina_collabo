import random
coefs = [random.randrange(2**8) for _ in range(3)]
public = [random.randrange(2**128) for _ in range(3)]

S = 0
for l,r in zip(coefs, public):
    S += l*r
print("S=", S)
print("public=", public)

with open("answer.txt", "w") as f:
    f.write(str(coefs))