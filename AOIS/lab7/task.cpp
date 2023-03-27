#include <iostream>
#include <cstring>
#include <cstdint>
using namespace std;

const int BLOCK_SIZE = 16; // размер блока
const int CACHE_SIZE = 32 * 2; // количество кэш-строк на количество наборов

struct CacheLine {
    bool valid; // строка содержит данные?
    uint64_t tag;
    uint8_t data[BLOCK_SIZE];
};

struct Cache {
    CacheLine lines[CACHE_SIZE];

    // Функция для чтения данных из оперативной памяти по физическому адресу
    void read_from_memory(uint64_t address, uint8_t* data) {
        // Здесь должна быть реализация чтения данных из оперативной памяти
        // В данном примере мы просто заполняем данные случайными значениями
        for (int i = 0; i < BLOCK_SIZE; i++) {
            data[i] = rand() % 256;
        }
    }

    // Функция для записи данных в оперативную память по физическому адресу
    void write_to_memory(uint64_t address, uint8_t* data) {
        // Здесь должна быть реализация записи данных в оперативную память
        // В данном примере мы не реализуем запись в оперативную память
    }

    // Функция для чтения данных из кэш-памяти по физическому адресу
    uint8_t* read_from_cache(uint64_t address) {
        uint64_t tag = address / BLOCK_SIZE; // вычисляем тег блока
        int index = -1;
        // Ищем кэш-строку с заданным тегом и флагом valid = true
        for (int i = 0; i < CACHE_SIZE; i++) {
            if (lines[i].valid && lines[i].tag == tag) {
                index = i;
                break;
            }
        }
        if (index != -1) { // кэш-попадание
            return lines[index].data + (address % BLOCK_SIZE); // возвращаем данные из кэш-строки
        } else { // кэш-промах
            uint8_t* data = new uint8_t[BLOCK_SIZE];
            read_from_memory(address, data); // читаем данные из оперативной памяти
            // Ищем свободную кэш-строку
            for (int i = 0; i < CACHE_SIZE; i++) {
                if (!lines[i].valid) {
                    index = i;
                    break;
                }
            }
            if (index == -1) { // кэш-память заполнена, выбираем кэш-строку для замещения
                index = rand() % CACHE_SIZE;
            }
            // Записываем данные в выбранную кэш-строку
            lines[index].valid = true;
            lines[index].tag = tag;
            memcpy(lines[index].data, data, BLOCK_SIZE);
            delete[] data;
            return lines[index].data + (address % BLOCK_SIZE); // возвращаем данные из кэш-строки
        }
    }
};

int main() {
    Cache cache;
    uint64_t address = 0x12345678; // заданный физический адрес
    uint8_t* data = cache.read_from_cache(address); // читаем данные из кэш-памяти
    cout << "Data at address 0x" << hex << address << ": ";
    for (int i = 0; i < BLOCK_SIZE; i++) {
        cout << hex << (int)data[i] << " ";
    }
    cout << endl;
}
