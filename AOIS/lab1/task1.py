class HashItem:
    def __init__(self, key, value, name) -> None:
        self.key = key
        self.value = value
        self.name = name

def get_index(key):
    arr = [ord(x) for x in key]
    mult = 1
    for el in arr:
        mult *= el

    mult %= 10000 # отделяет последние 4 цифры
    mult %= 23
    print(f"Индекс ключа \"{key}\" : {mult}")
    return mult

hash_tabl = [None for _ in range(20)]

while True:
    menu = input("1. Добавление записи\n2. Удаление записи\n3. Вывод таблицы\n4. Выход из программы\n> ")
    match menu:
        case '1':
            key = input("Введите ключ: ")
            val = input("Введите значение: ")
            name = input("Введите имя: ")
            hash_tabl[get_index(key)] = HashItem(key, val, name)
        case '2':
            key = input("Введите ключ: ")
            hash_tabl[get_index(key)] = None
        case '3':
            key = input("Введите ключ: ")
            el = hash_tabl[get_index(key)]
            if el is not None:
                print(el.value, el.name, sep="\t")
            else:
                print("Ничего не найдено")
        case '4':
            break