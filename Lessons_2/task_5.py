# Реализуйте алгоритм перемешивания списка.

lst = [1, 2, 3, 4, 8, 9, 5]
print(lst)
print('-------------------')
l = len(lst)
for i in range(l - 2):
    if i != l:
        a = lst[i]
        lst[i] = lst[(l - 1) - i]
        lst[(l - 1) - i] = a
        a = 0
print(lst)

