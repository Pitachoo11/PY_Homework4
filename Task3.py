# Задайте последовательность чисел. Напишите программу, которая выведет список уникальных (неповторяющихся) элементов
# исходной последовательности.

import random

n = int(input('Введите количество чисел в последовательности: '))

list_full = []
list_selected = []

for i in range(0, n):
    list_full.append(random.randint(1,5))

for i in range(0, n):
    if list_full.count(list_full[i]) == 1:
        list_selected.append(list_full[i])

print(list_full)
print(list_selected)