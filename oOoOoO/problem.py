import signal
from Crypto.Util.number import long_to_bytes, bytes_to_long, getPrime
import random

message = b""
for _ in range(128):
    message += b"o" if random.getrandbits(1) == 1 else b"O"

M = getPrime(len(message) * 5)
S = bytes_to_long(message) % M

print("M =", M)
print('S =', S)
print('MESSAGE =', message.upper().decode("utf-8"))

with open("answer.txt", "w") as f:
    f.write(message.decode('utf-8'))
