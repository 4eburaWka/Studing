print("ЗАДАНИЕ 1")
import random

months = ["январь", "февраль", "март", "апрель", "май", "июнь", "июль", "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]

random_values = [round(random.uniform(0.0, 100.0), 2) for _ in range(12)]

for i in range(12):
    print(f"{months[i]}: {random_values[i]}")

average_value = sum(random_values) / len(random_values)
print(f"Среднее значение: {average_value:.2f}")


print("\n\nЗАДАНИЕ 2")
dates = ["01/20/2022", "15/02/2023", "30/03/2022", "04/10/2022", "05/05/2022", "20/06/2022", "07/12/2022", "25/08/2022", "09/03/2022", "18/10/2022"]

month_names = {
    "01": "января",
    "02": "февраля",
    "03": "марта",
    "04": "апреля",
    "05": "мая",
    "06": "июня",
    "07": "июля",
    "08": "августа",
    "09": "сентября",
    "10": "октября",
    "11": "ноября",
    "12": "декабря"
}

for date in dates:
    parts = date.split("/")
    day = parts[0]
    month = parts[1]
    year = parts[2]
    
    if month in month_names:
        month_name = month_names[month]
        formatted_date = f"{day} {month_name} {year}"
        print(formatted_date)
    else:
        print("неправильный ввод")


print("\n\nЗАДАНИЕ 3")
import random

def generate_consonants_sequence(N):
    consonants = "BCDFGHJKLMNPQRSTVWXYZ"
    sequence = ''.join(random.choice(consonants) for _ in range(N))
    return sequence

N = int(input("Введите длину последовательности: "))
if N > 0:
    random_sequence = generate_consonants_sequence(N)
    print(random_sequence)


print("\n\nЗАДАНИЕ 4")
text = "Какой-то невероятно крутой текст"

vowels_count = 0
spaces_count = 0
total_letters_count = 0

for char in text:
    if char.isalpha():
        total_letters_count += 1
        
        if char.lower() in "аеёиоуыэюя":
            vowels_count += 1
    
    elif char.isspace():
        spaces_count += 1

print("Количество гласных:", vowels_count)
print("Количество пробелов:", spaces_count)
print("Общее количество букв:", total_letters_count)



print("\n\nЗАДАНИЕ 5")
string_array = ["Это строка 1", "Это строка 2", "Это строка 3"]

delimiter = input("Введите разделитель: ")

extracted_strings = []

for string in string_array:
    extracted_strings.extend(string.split(delimiter))

print("Извлеченные строки:")
for extracted_string in extracted_strings:
    print(extracted_string)
