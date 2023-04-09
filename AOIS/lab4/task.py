from math import log2
from random import choice


def get_tag_offset(address, block_size):
    address = bin(address)[2:] # Получить биты
    offset_len = log2(block_size)
    return int(address[:-offset_len], 10), int(address[-offset_len], 10)


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
        self.tag = 0
        self.data = [0] * block_size

    def read(self, offset):
        return self.data[offset]
    
    def write(self, tag, offset, data):
        self.is_empty = False
        self.tag = tag
        self.data[offset] = data


class Cache:
    def __init__(self, lines_count, block_size, ram) -> None:
        self.lines_count, self.blocks_count, self.ram = lines_count, block_size, ram
        self.cache_lines = [CacheLine(block_size) for _ in range(lines_count)]
        self.cache_lines_len = 0

    def shift(self, index):
        for i in range(index, self.cache_lines_len - 1, 1):
            self.cache_lines[i] = self.cache_lines[i + 1]

    def write(self, address):
        tag, offset = get_tag_offset(address, self.block_size)

        for cache_line in self.cache_lines:
            if cache_line.is_empty:
                cache_line.write(tag, offset, self.ram.read(address))
                self.cache_lines_len += 1
                break
        else:  
            self.shift(0)
            self.cache_lines[-1].write(tag, offset, self.ram.read(address))
            self.cache_lines_len -= 1

    def read(self, address):
        tag, offset = get_tag_offset(address, self.block_size)

        for i, cache_line in enumerate(self.cache_lines):
            if not cache_line.is_empty and cache_line.tag == tag:
                print("Cache hit!")
                data = cache_line.read(offset)
                self.shift(i)
                self.cache_lines[self.cache_lines_len] = data
                return data
        
        print("Cache miss!")
        self.write(address)

numbers = list(range(1024))
ram = RAM(2048)

for i in range(1024):
    ram.write(i, choice(numbers))