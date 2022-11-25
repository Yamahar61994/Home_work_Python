# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

n = int(input('N = '))
s = []
b = 1
for i in range(1, n + 1):
    b = round(((1 + 1) / i)**i, 2)
    s.append(b)
print(s)
print(f'Summa = {round(sum(s), 2)}')