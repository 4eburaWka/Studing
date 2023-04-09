alphabet = {"К":13, "У":10, "З":20} 

P = 6
Q = 7

N = P * Q
L = (P - 1) * (Q - 1)

for D in range(1, 14, 1):
    for c in range(min(D, L), 0, -1):
        if D % c == L % c != 0:
            break

E = 0
while (E * D) % L != 1:
    E += 1

# Encoding
c1 = alphabet["К"] ** E % N
c2 = alphabet["У"] ** E % N
c3 = alphabet["З"] ** E % N

# Decoding
M1 = c1 ** D % N
M2 = c2 ** D % N
M3 = c3 ** D % N

def M(alphabet, value):
    for i in alphabet.keys():
        if alphabet[i] == value:
            return i

print(M(alphabet, M1) + M(alphabet, M2) + M(alphabet, M3))

