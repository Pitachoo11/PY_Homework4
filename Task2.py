# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число n:'))
numbers = []

for i in range(1, n+1):
    if(n % i == 0):
        numbers.append(i)

print(numbers)