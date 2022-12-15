# Задайте последовательность чисел.
#Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

import random
n = int(input('Кол-вo элементов последовательности n= '))
list1 = []
list2 = []
while n != 0:
    list1.append(random.randint(1, 5))
    n -=1
print(f'Исходная поседовательность {list1} ')
print()
for x in list1:
    i= 0
    for y in list1:
        if x == y:
            i +=1
    if i == 1:
        list2.append(x)

print(list2)

