import random
with open("C:\\Studing\\MOIS\\Lab. 8\\example_"+input("name: "),'w') as file:
    n = int(input("n: "))
    for i in range(n):
        file.write(f"{random.randint(5,100)} {random.randint(5,100)}\n")