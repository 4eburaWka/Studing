from os import system
class Item:
    def __init__(self, key="", val="", name="") -> None:
        self.key, self.val, self.name = key, val, name
        
    def get_data(self):
        return self.key, self.val, self.name
    
class Tabl:
    def __init__(self) -> None:
        self.tabl = []
    

    def get_index(self, key):
        for i, el in enumerate(self.tabl):
            if el.key == key:
                return i
    
    def add(self, key, val, name):
        self.tabl.append(Item(key, val, name))
    
    def edit(self, key, val, name):
        self.tabl[self.get_index(key)].val, self.tabl[self.get_index(key)].name = val, name

    def delete(self, key):
        self.tabl.pop(self.get_index(key))
    
    def show(self, key):
        output = self.tabl[self.get_index(key)].get_data()
        print(output[0], output[1], output[2], sep='\t')
    
    def show_all(self):
        for i, el in enumerate(self.tabl):
            print(i, end='\t')
            output = el.get_data()
            print(output[0], output[1], output[2], sep='\t')
            print("----------------------------------------")

tabl = Tabl()
while True:
    menu = input("1. Добавление записи\n2. Редактирование записи\n3. Удаление записи\n4. Вывод по ключу\n5. Вывод всей таблицы\n6. Выход из программы\n>> ")
    system('cls')
    match menu:
        case '1':
            key = input("Введите ключ: ")
            val = input("Введите значение: ")
            name = input("Введите имя: ")
            tabl.add(key, val, name)      
        case '2':
            key = input("Введите ключ: ")
            val = input("Введите значение: ")
            name = input("Введите имя: ")
            tabl.edit(key, val, name)
        case '3':
            key = input("Введите ключ: ")
            tabl.delete(key)
        case '4':
            key = input("Введите ключ: ")
            tabl.show(key)
        case '5':
            tabl.show_all()
        case '6':
            break
        case '8':
            exec(input())
    