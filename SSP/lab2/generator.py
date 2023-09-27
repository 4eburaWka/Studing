import random as r

with open("file.txt", 'w') as file:
    for _ in range(1000):
        file.write(str(r.randint(0, 1000)) + "\n")