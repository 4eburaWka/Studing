
def get_array_from_string(string):
    return [int(i) if i != '?' else 2 for i in string ]

class ASM:
    def __init__(self, block_size, memory_size):
        self.memory = [[1] for _ in range(memory_size)]
        self.block_size = block_size

    def _is_cell_empty(self, cell_number):
        return self.memory[cell_number][0] == 1


    def find(self, value):
        # memory = [cell.copy() for cell in self.memory if not cell[0]] # скопировать заполненные ячейки
        finding_address = get_array_from_string(value)
        addresses = [not self._is_cell_empty(i) for i, cell in enumerate(self.memory)] # поставить 1 напротив заполненной ячейки, 0 - напротив пустой
        for i, bit in enumerate(finding_address):
            if bit == 2:
                continue
            
            for cell_number, cell in enumerate(self.memory):
                if not addresses[cell_number]:
                    continue
                if cell[i+1] != finding_address[i]:
                    addresses[cell_number] = 0
                    
            if addresses.count(1) == 1:
                return addresses.index(1)
        return [cell_number for cell_number, cell in enumerate(addresses) if cell]
            

    def write(self, value):
        for cell in self.memory:
            if cell[0] == 1:
                cell[0] = 0
                cell += value
                return
        else:
            print("Память заполнена!")
    
    def delete(self, value):
        cell_number = self.find(value)
        if isinstance(cell_number, list):
            print("Найдено несколько значений!")
            return
        
        self.memory[cell_number] = 1

data = [
    [1, 0, 1, 0, 1, 1, 0, 0, 1, 1],
    [0, 1, 1, 1, 0, 0, 1, 0, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 1, 1, 0],
]

mem = ASM(3, 16)
mem.write(data[0])
mem.write(data[1])
mem.write(data[2])

print(mem.find("101?"))
print(mem.find("??11"))
print(mem.find("101?"))

str = "1234"
str.find("34")