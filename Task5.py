# ДОП Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

import re

# Подгрузка строки из файла1 и разбивка на кортежи
file1 = 'poly1.txt'
data = open(file1, 'r')
for line in data:
    poly1 = line.replace('= 0', '')
    poly1 = re.sub("[*|^| ]", " ", poly1).split('+')
    poly1 = [char.split(' ') for char in poly1]
    poly1 = [[x for x in list if x] for list in poly1]
    for i in poly1:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    poly1 = [tuple(int(x) for x in j if x != 'x') for j in poly1]
    print('Первый многочлен', line)
data.close()

# Подгрузка строки из файла2 и разбивка на кортежи
file2 = 'poly2.txt'
data = open(file2, 'r')
for line in data:
    poly2 = line.replace('= 0', '')
    poly2 = re.sub("[*|^| ]", " ", poly2).split('+')
    poly2 = [char.split(' ') for char in poly2]
    poly2 = [[x for x in list if x] for list in poly2]
    for i in poly2:
        if i[0] == 'x': i.insert(0, 1)
        if i[-1] == 'x': i.append(1)
        if len(i) == 1: i.append(0)
    poly2 = [tuple(int(x) for x in j if x != 'x') for j in poly2]
    print('Второй многочлен', line)
data.close()

# Суммирование кортежей в список
x = [0] * (max(poly1[0][1], poly2[0][1] + 1))
for i in poly1 + poly2:        
    x[i[1]] += i[0]
summ_poly = [(x[i]) for i in range(len(x)) if x[i] != 0]

# Составление итогового многочлена
polynomial=' + '.join([f'{(j,"")[j==1]}*x^{i}' for i, j in enumerate(summ_poly) if j][::-1])

polynomial = polynomial.replace('x^1+', 'x+')
polynomial = polynomial.replace('*x^0', ' = 0')
polynomial += ('','1')[polynomial[-1]=='+']
polynomial = (polynomial, polynomial[:-2])[polynomial[-2:] == '^1']

print('Итог.  многочлен', polynomial)

# Запись результата в файл
file3 = open("poly3.txt", "w")
file3.write(polynomial)
file3.close()