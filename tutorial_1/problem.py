import random
coefs = [random.randrange(2**512) for _ in range(2)]
print(2 * coefs[0] + 3 * coefs[1])
print(4 * coefs[0] + 7 * coefs[1])

with open("answer.txt", "w") as f:
    f.write(str(coefs))