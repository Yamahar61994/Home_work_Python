# 2'. Напишите программу, которая найдёт произведение пар чисел списка. 
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 
# В скобках пример, как это работает!!!

list1 = [2, 3, 4, 6]
pro =[]
a = 0
l = len(list1)

if l % 2 != 0:
    for i in range(0, l):
      pro.append(list1[i] * list1[l-1-i])
      if i == (l - 1 - i):
          break
else:
   for i in range(0, l // 2):
      pro.append(list1[i] * list1[l-1-i])
print(pro)