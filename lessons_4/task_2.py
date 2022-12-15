#  Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# * 6 -> [1,2,3]
# * 144 -> [2,3]

num = int(input('N = '))
list = [1,]
print()
while num != 1:
    print(f'n = {num}')
    if num % 2 == 0:
        a = 2
        num = num // a
        list.append(a)
    else:
        if num % 3 == 0:
            a = 3
            num = num // 3
            list.append(a)
        else:
            list.append(num)
            num = num // num
print()
print(f'Список прростых множителей {list}')
    