def get_array_from_string(string):
    return [int(i) if i != '?' else 2 for i in string]

class ASM:
    def __init__(self, block_size, memory_size):
        self.memory = [[ [1] for __ in range(block_size) ] for _ in range(memory_size)]
        self.block_size = block_size

    def _is_cell_empty(self, block_number, cell_number):
        return self.memory[block_number][cell_number][0] == 1

    def find(self, value):
        finding_address = get_array_from_string(value)
        addresses = [[not self._is_cell_empty(block_number, cell_number) for cell_number, _ in enumerate(block)] for block_number, block in enumerate(self.memory)]
        for i, bit in enumerate(finding_address):
            if bit == 2:
                continue

            for block_number, block in enumerate(self.memory):
                for cell_number, cell in enumerate(block):
                    if not addresses[block_number][cell_number]:
                        continue
                    if cell[i+1] != finding_address[i]:
                        addresses[block_number][cell_number] = False
            if [block.count(1) for block in addresses].count(1) == 1:
                for block_number, block in enumerate(addresses):
                    if block.count(1):
                        return (block_number, block.index(1))
        result = []
        for block_number, block in enumerate(addresses):
            for cell_number, cell in enumerate(block):
                if cell:
                    result.append((block_number, cell_number))
        return result
        """
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
        """

    def write(self, value):
        for block in self.memory:
            for cell in block:
                if cell[0] == 1:
                    cell[0] = 0
                    cell += get_array_from_string(value)
                    return
            else:
                print("Память заполнена!")

    def delete(self, value):
        cell_numbers = self.find(value)
        if isinstance(cell_numbers[0], tuple):
            print("Найдено несколько значений!")
            return
        self.memory[cell_numbers[0]][cell_numbers[1]][0] = 1

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
print(mem.find("1?"))

str = "1234"
str.find("34")