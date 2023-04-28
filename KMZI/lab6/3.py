ar = [
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    [0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1],
    [0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
]


def get_sum(bitset: list):
    bitset = [0, 0] + [bitset[0]] + [0] + bitset[1:4] + [0] + bitset[4:]
    r = [0, 0, 0, 0]
    for i in range(4):
        for j in range(15):
            if ar[i][j] & bitset[j]:
                r[i] += 1

    return [i % 2 for i in r]


def check_sum(bitset, sum):
    bitset = [sum[0], sum[1]] + [bitset[0]] + [sum[2]] + bitset[1:4] + [sum[3]] + bitset[4:]
    r = [0, 0, 0, 0]
    pb = 0
    for el in bitset:
        pb += el
    pb %= 2
    for i in range(4):
        for j in range(15):
            if ar[i][j] & bitset[j]:
                r[i] += 1
    r = [i % 2 == pb for i in r]
    if all(r):
        return "Сумма верная!"
    return int("".join([str(int(s)) for s in r]), 2)


bitset = [1, 1, 0, 0, 1, 0, 1, 1, 1, 1, 0]  # input("Введите последовательность: "`)
sum = get_sum(bitset)
print(sum)
bitset[5] = not bitset[5]
bitset[3] = not bitset[3]

print(check_sum(bitset, sum))