from random import uniform, randint

Number = 10
distribution = [0.6, 0.1, 0.1, 0.2, 0]


def high_level():
    all_work = 0
    for x in range(randint(5, 7)): # 6
        all_work += uniform(0.2, 0.5)
    return all_work # Вся работа за день

def middle_level():
    all_work = 0
    for x in range(randint(4, 6)): # 5
        all_work += uniform(0.1, 0.3)
    return all_work # Вся работа за день

def low_level():
    all_work = 0
    for x in range(randint(3, 5)): # 4
        all_work += uniform(0.05, 0.2)
    return all_work # Вся работа за день

def trainee():
    all_work = 0
    for x in range(randint(1, 3)): # 2
        all_work += uniform(0.01, 0.02)
    return all_work # Вся работа за день

def smart_but_lazy():
    all_work = 0
    for x in range(randint(1,2)): # 1
        all_work += uniform(0.3, 0.75)
    return all_work # Вся работа за день


number_of_days = []

for x in range(100):
    all_days = 0
    all_all_work = 0

    while all_all_work < 100:
        for x in range(int(Number * distribution[0])):
            all_all_work += high_level()
        for x in range(int(Number * distribution[1])):
            all_all_work += middle_level()
        for x in range(int(Number * distribution[2])):
            all_all_work += low_level()
        for x in range(int(Number * distribution[3])):
            all_all_work += trainee()
        for x in range(int(Number * distribution[4])):
            all_all_work += smart_but_lazy()
        
        all_days += 1
    
    number_of_days.append(all_days)

print(f"Среднее кол-во дней: {sum(number_of_days)/100}, минимальное кол-во дней: {min(number_of_days)}, максимальное кол-во дней: {max(number_of_days)}")