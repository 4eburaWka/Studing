from os import system
num_of_colls, num_of_records, num_of_appeals = 0, 0, 0
provisional_values = {
#             11       21      15     4       12     11        13           0           17     21      2     1         5       20     10       15      22       12      11         13   
    "keys": ["hello", "good", "cat", "car", "flood", "dog", "graduate", "underground", "this", "he", "she", "word", "excel", "lion", "leon", "spike", "game", "point", "mother", "earth"],
    "vals": ["hello", "good", "cat", "car", "flood", "dog", "graduate", "underground", "this", "he", "she", "word", "excel", "lion", "leon", "spike", "game", "point", "mother", "earth"], 
    "names":["hello", "good", "cat", "car", "flood", "dog", "graduate", "underground", "this", "he", "she", "word", "excel", "lion", "leon", "spike", "game", "point", "mother", "earth"]
}

class HashItem:
    def __init__(self, key="", val="", name="") -> None:
        self.key, self.val, self.name = key, val, name
        self.link = None

    def to_set(self, key, val, name):
        self.key, self.val, self.name = key, val, name
    
    def to_clear(self, key):
        if self.key == key:
            self.key, self.val, self.name = "", "", ""
            print("Удалено:", key)
            num_of_records -= 1
        elif self.link == None:
            print("Такого ключа не существует")
        else:
            self.link.TO_CLEAR(key)

        global num_of_appeals
        num_of_appeals += 1
    
    def to_show(self, key):
        if self.key == key:
            print(f"{self.val=}\t{self.name=}")
        elif self.link == None:
            print("Такого ключа не существует")
        else:
            self.link.TO_SHOW(key)

        global num_of_appeals
        num_of_appeals += 1
    
    def to_show_all(self):
        if not self.is_empty():
            print(self.key, self.val, self.name, sep='\t')
        if self.link is not None:
            print("Коллизия: ")
            self.link.TO_SHOW_ALL()
    
    def make_link(self, link):
        if self.link is None:
            self.link = link

            global num_of_colls
            num_of_colls += 1 
        else:
            self.link.make_link(link)

    def is_empty(self):
        return self.key == self.val == self.name == ""


class Hash_tabl:
    def __init__(self, length: int) -> None:
        self.tabl = [HashItem() for x in range(length)]
    
    def add(self, key, val, name):
        index = get_index(key)
        if self.tabl[index].is_empty():
            self.tabl[index].TO_SET(key, val, name)
        else:
            self.tabl[index].make_link(HashItem(key, val, name))
            
        global num_of_records
        num_of_records += 1
        global num_of_appeals
        num_of_appeals += 1

    def edit(self, key, val, name):
        index = get_index(key)
        if self.tabl[index].key == key:
            self.tabl[index].TO_SET(key, val, name)
        else:
            self.tabl[index].link.TO_SET(key, val, name)

        global num_of_appeals
        num_of_appeals += 1
    
    def delete(self, key):
        index = get_index(key)
        self.tabl[index].TO_CLEAR(key)

        global num_of_appeals
        num_of_appeals += 1
    
    def show(self, key):
        index = get_index(key)
        self.tabl[index].TO_SHOW(key)

        global num_of_appeals
        num_of_appeals += 1
    
    def show_all(self):
        for i, el in enumerate(self.tabl):
            print(i, end='\t')
            el.TO_SHOW_ALL()
            print("\n----------------------------------------")
        

def get_index(key):
    arr = [ord(x) for x in key]
    mult = 1
    for el in arr:
        mult *= el

    mult %= 10000 # отделяет последние 4 цифры
    mult %= 23
    print(f"Индекс ключа \"{key}\" : {mult}")
    return mult


hash_tabl = Hash_tabl(23)
x, y = [], []
while True:
    menu = input("1. Добавление записи\n2. Редактирование записи\n3. Удаление записи\n4. Вывод по ключу\n5. Вывод всей таблицы\n6. Выход из программы, провести расчеты\n7. Если вы хотите занести в таблицу значения\n>> ")
    system('cls')
    match menu:
        case '1':
            key = input("Введите ключ: ")
            val = input("Введите значение: ")
            name = input("Введите имя: ")
            hash_tabl.add(key, val, name)      
        case '2':
            key = input("Введите ключ: ")
            val = input("Введите значение: ")
            name = input("Введите имя: ")
            hash_tabl.edit(key, val, name)
        case '3':
            key = input("Введите ключ: ")
            hash_tabl.delete(key)
        case '4':
            key = input("Введите ключ: ")
            hash_tabl.show(key)
        case '5':
            hash_tabl.show_all()
        case '6':
            break
        case '7':
            for i in range(20):
                hash_tabl.add(provisional_values["keys"][i]+'k', provisional_values["vals"][i]+'v', provisional_values["names"][i]+'n')
                x.append(num_of_records)
                y.append(num_of_colls)
        case '8':
            exec(input())
system('cls')
print(x)
print(y)
print(
f"""Всего коллизий: {num_of_colls}.
Всего записей в таблице: {num_of_records}.
Всего обращений к таблице: {num_of_appeals}.
Вероятность возникновения коллизий: {num_of_colls/num_of_records}.
Среднее количество обращений к таблице во время поиска записи по ключу: {num_of_appeals/num_of_records}."""
)