import numpy.random as r


SC = 4 # Социальные контакты
R = 4 # Ответственность
HA = 3 # Здоровье
A = 1 # Возраст
AP = 4 # Средний возраст населения
M = 1 # Эффективность лечения
T = 2 # Проведение тестов
I = 1 # Заразность
RT = 1 # Срок выздоровления
DR = 1 # Смертность


def N(m, scale):
    returned = r.normal(m, scale, size=None)
    return returned if returned > 0 else 0

def U(c, d):
    returned = r.uniform(c-d, c+d, size=None)
    return returned if returned > 0 else 0

def E(scale):
    returned = r.exponential(scale, size=None)
    return returned if returned > 0 else 0

def probability(probability): # Принимает вероятность какого-то события, и возвращает True если так надо
    return True if r.uniform(0,100) < probability else False



class Environment:
    def __init__(self) -> None:
        self.AP = N(25, 5.5)
        self.M = N(10, 1.5)
        self.T = N(3, 1.5)
Belarus = Environment()



class Agent:
    def __init__(self) -> None:
        self.condition = 2 # 1 - здоров, 2 - болен и не знает, 3 - болен и знает, 4 - лечится, 5 - мертв
        
        self.m = r.uniform(0, 50)
        self.SC = U(self.m, 6)
        self.R = 10-E(0.5)
        self.HA = N(6, 0.5)
        if self.HA < 2:
            self.PT = 0.1
        else:
            self.PT = 0.01
        self.A = N(Belarus.AP, 5.5)
        self.RT = int(1 + U( 2.-1.5*self.HA-0.5*Belarus.M, 5-0.25*self.HA-0.1*Belarus.M ))
        self.DR = A*0.05+U( 15-1.5*self.HA, 3-0.25*self.HA )
        self.check_recovery = 0 # Когда будет 100, агент вылечится
    def ch_SC(self):
        self.SC = int(self.SC / self.R)

    def ch_DR(self):
        if self.condition == 4:
            self.DR = A*0.05+U( 15-1.5*self.HA-0.5*Belarus.M, 3-0.25*self.HA-0.1*Belarus.M )



class Virus:
    def __init__(self) -> None:
        self.I = U(20, 20)
Virus = Virus()


infected = r.randint(5, 11)
infected_people = [Agent() for x in range(infected)]
for i in range(infected):
    infected_people[i].condition = 2 # болен и не знает

day = 1
dead, cured = 0, 0
information = []

print("День", "Заразившиеся","Умерло","Вылеченные", sep='\t')

needed_remove = []
while day < 51:
    needed_remove = []
    for i in infected_people:
        i.ch_DR()
        if probability(Belarus.T) and i.condition == 2: # Чтобы узнать о болезни
            i.condition = 3
            i.ch_SC()
        if probability(i.DR/10) and (i.condition == 2 or i.condition == 3): # Чтобы умереть
            needed_remove.append(infected_people.index(i))
            dead += 1

        if i.condition == 2 or i.condition == 3: 
            for x in range(int(i.SC/7)): # Заражение
                if probability(Virus.I):
                    infected_people += [Agent()]
                    infected += 1

        if True and i.condition == 3: # Принятие лечения
                i.condition = 4

        if i.condition == 4:
            i.check_recovery += Belarus.M
            if i.check_recovery >= 100:
                cured += 1
                needed_remove.append(infected_people.index(i))
    
    needed_remove.reverse()
    for x in needed_remove: # Удаление людей из списка инфицированных
        infected_people.pop(x)

        

    print(day, infected, dead, cured, sep='\t')
    day += 1
    infected = 0
    dead = 0
    cured = 0