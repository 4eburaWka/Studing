cod = input()
code = []

for x in cod:
    code.append(int(x))

Sr = 0
for x in range(1, len(code), 2):
    Sr += code[x]

S1 = Sr * 3

SH = 0
for x in range(0, len(code) - 1, 2):
    SH += code[x]

S = S1 + SH

t = S % 10
P = 10 - t

if P == code[12]:
    print("Штрих-код введен верно")
else:
    print("Штрих-код введен неверно")

    