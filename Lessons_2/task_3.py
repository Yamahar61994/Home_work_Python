# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# n = int(input('N = '))
# s = []
# for i in range(1, n + 1):
#     b = round(((1 + 1) / i)**i, 3)
#     s.append(b)
# print(s)
# print(f'Summa = {round(sum(s), 3)}')

n = int(input('N = '))
spi = [(1+1/i)**i for i in range(1, n+1)]
print(f'Последовательность: {spi}')
print(f'Сумма: {round(sum(spi), 3)}') 