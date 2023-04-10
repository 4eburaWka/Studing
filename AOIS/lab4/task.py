from math import log2, ceil
from random import choice, randint


def get_tag_offset(address, block_size):
    address = bin(address)[2:] # Получить биты
    offset_len = ceil(log2(block_size))
    return int(address[:-offset_len], 2), int(address[-offset_len], 2)


class RAM:
    def __init__(self, size) -> None:
        self.size = size
        self.data = [0] * size

    def read(self, address):
        return self.data[address]
    
    def write(self, address, data):
        self.data[address] = data


class CacheLine:
    def __init__(self, block_size) -> None:
        self.is_empty = True
        self.tag = None
        self.data = [None] * block_size

    def read(self, offset):
        return self.data[offset]
    
    def write(self, tag, offset, data):
        self.is_empty = False
        self.tag = tag
        self.data[offset] = data


class Cache:
    def __init__(self, lines_count, block_size, ram) -> None:
        self.lines_count, self.block_size, self.ram = lines_count, block_size, ram
        self.cache_lines = [CacheLine(block_size) for _ in range(lines_count)]
        self.cache_lines_len = 0

    def _shift(self, index):
        for i in range(index, self.cache_lines_len - 1, 1):
            self.cache_lines[i] = self.cache_lines[i + 1]

    def _write(self, address):
        tag, offset = get_tag_offset(address, self.block_size)

        for cache_line in self.cache_lines:
            if cache_line.is_empty:
                cache_line.write(tag, offset, self.ram.read(address))
                self.cache_lines_len += 1
                break
        else:  
            self._shift(0)
            self.cache_lines[-1].write(tag, offset, self.ram.read(address))
            self.cache_lines_len -= 1
        print(f", data={self.ram.read(address)}")

    def __call__(self, address):
        tag, offset = get_tag_offset(address, self.block_size)
        print(f"{tag=}, {offset=}", end="")

        for i, cache_line in enumerate(self.cache_lines):
            if cache_line.data[offset] is not None and cache_line.tag == tag:
                data = cache_line.read(offset)
                self._shift(i)
                self.cache_lines_len -= 1
                self.cache_lines[self.cache_lines_len].write(tag, offset, data)
                print(f", data={data}")
                print("Cache hit!")
                return data
            elif cache_line.data[offset] is None and cache_line.tag == tag:
                data = self.ram.read(address)
                cache_line.data[offset] = data
                print(f", data={data}")
                print("Cache miss!")
                return data

        
        self._write(address)
        print("Cache miss!")
    
    def show(self):
        for i, cache_line in enumerate(self.cache_lines):
            print(f"{i}, tag={cache_line.tag}, {cache_line.data[0]}\t{cache_line.data[1]}")

numbers = list(range(50))
ram = RAM(2048)
cache = Cache(32, 2, ram)
for i in range(50):
    p = randint(0, 50)
    print(p)
    ram.write(i, p)

while True:
    address = input("Введите адрес: ")
    try:
        address = int(address)
    except ValueError:
        cache.show()
    else:
        cache(address)