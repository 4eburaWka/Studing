import bisect

class HashTable:
    def __init__(self):
        self.table = []
    
    def insert(self, identifier):
        identifier = identifier.upper()
        table = self.table[::-1]
        bisect.insort(table, identifier)
        self.table = table[::-1]
        
    def search(self, identifier):
        identifier = identifier.upper()
        comparisons = 0
        low, high = 0, len(self.table) - 1
        
        while low <= high:
            comparisons += 1
            mid = (low + high) // 2
            if self.table[mid] == identifier:
                return True, comparisons
            elif self.table[mid] < identifier:
                high = mid - 1
            else:
                low = mid + 1
                
        return False, comparisons
    
    def show(self):
        print(*self.table, "\n", sep="\n")

def read_identifiers_from_file(file_path):
    with open(file_path, 'r') as file:
        return [line.strip() for line in file]

def main():
    file_path = "APIS/lab1/ident.txt" 
    identifiers = read_identifiers_from_file(file_path)
    
    hash_table = HashTable()
    
    for identifier in identifiers:
        hash_table.insert(identifier)
    
    while True:
        print("\nМеню:")
        print("1. Найти запись по ключу")
        print("2. Показать все записи")
        print("3. Выйти")

        choice = input("Выберите действие (1-3): ")
        
        if choice == '1':
            key = input("Введите ключ для поиска: ").strip()
            value, comparisons = hash_table.search(key)
            if value:
                print(f"Найдена запись: {key}: {value}. Выполнено сравнений: {comparisons}")
            else:
                print(f"Запись с ключом '{key}' не найдена. Выполнено сравнений: {comparisons}")

        elif choice == '2':
            print("Текущие записи в хеш-таблице (в обратном алфавитном порядке):")
            hash_table.show()

        elif choice == '3':
            print("Завершение программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, выберите действие от 1 до 4.")

    search_id = input("Введите идентификатор для поиска: ").strip()
    found, comparisons = hash_table.search(search_id)
    
    if found:
        print(f"Идентификатор '{search_id}' найден за {comparisons} сравнений.")
    else:
        print(f"Идентификатор '{search_id}' не найден. Выполнено {comparisons} сравнений.")

if __name__ == "__main__":
    main()