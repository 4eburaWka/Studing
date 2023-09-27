def write_array_to_file(array):
    with open("SSP\\lab2\\output.txt", 'w') as file:
        for number in array:
            file.write(str(number) + '\n')

def check(filename, sorting_mode):
    with open(filename, 'r') as file:
        num1 = int(file.readline())
        while num2 := file.readline() != '':
            if num1 > int(num2) and sorting_mode == 1:
                return "Error!"
            elif num1 < int(num2) and sorting_mode == 2:
                return "Error!"
        return "Success!"

numbers = []
with open("SSP\\lab2\\file.txt", 'r') as file:
    sorting_mode = int(file.readline()) # 1 - по взрастанию, 2 - по убыванию
    for _ in range(int(file.readline())):
        numbers.append(int(file.readline()))
numbers.sort()

if sorting_mode == 1:
    write_array_to_file(numbers)
elif sorting_mode == 2:
    numbers.reverse()
    write_array_to_file(numbers)

print(check("SSP\\lab2\\output.txt", sorting_mode))