# 4'. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

num =int(input('N= '))
temp =[]
while num != 0:
     temp.append(str(num % 2))
     num = num // 2
     
temp.reverse()
binar = ','.join(temp)
print(binar)