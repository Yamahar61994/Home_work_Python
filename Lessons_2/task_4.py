# Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной
# строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2

n = int(input('N = '))
lst_1 = [i for i in range(-n, n + 1)]
print(lst_1)

file = open('1.txt')
lst_2 = [int(i) for i in file]
file.close
print(lst_2)

prozv = lst_1[lst_2[0]] * lst_1[lst_2[1]]
print(f'Proizvedenie = {prozv}')
