#Задание 1:

diapazonn = int(input("Введите начало диапазона для поиска простых чисел: "))
diapazonk = int(input("Введите конец диапазона для поиска простых чисел: "))
for num in range(diapazonn, diapazonk):
    count = 0
    delitel = 2
    while delitel < num:
        if num % delitel == 0:
            count += 1
        delitel += 1
    if count == 0:
        print(f'{num} простое число')

#Задание 2:

for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")




# Задание 3:

range_start = int(input("Введите начало диапазона: "))
range_end = int(input("Введите конец диапазона: "))

for i in range(range_start, range_end + 1):
    for j in range(1, 11):
        print(f"{i} * {j} = {i * j}")
print("................................................")