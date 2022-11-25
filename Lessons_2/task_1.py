# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# num = input('num = ')
# sum = 0

# for i in num:
#     if i.isdigit(): #проверка, но то, что это именно число, а не символ
#         sum += int(i)
# print(f'Summ cifr = {sum}')
    
n = input()
n = [int(i) for i in n]
summma = sum(n)
print(summma)
print(n)