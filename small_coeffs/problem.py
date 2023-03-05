import random
coefs = [random.randrange(2**512) for _ in range(5)]
Sums = []
public = []

for i in range(2):
    public_values = [random.randrange(2**1024) for _ in range(5)]
    S = 0
    for l,r in zip(coefs, public_values):
        S += l*r
    Sums.append(S)
    public.append(public_values)

print("public = ", public)
print("Sums = ", Sums)
with open("answer.txt", "w") as f:
    f.write(str(coefs))