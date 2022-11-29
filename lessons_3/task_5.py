# 5'. Задайте число. Составьте список чисел Фибоначчи, в том числе 
# для отрицательных индексов.(Дополнительно)

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи]
#  F−n = ((−1)^(n+1)) * Fn.


num = int(input('N= '))
fib1 = 1
fib2 = 1
i = 0
temp =[0, fib1,]
while i < num - 1:
    temp.append(int(fib2))
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
c = 0 
while c < num -1:
      c = c + 2
      temp[c] = temp[c] * (-1)    
temp.reverse()

fib1 = 1
fib2 = 1
i = 0
temp1 =[fib1,]
while i < num - 1:
    temp1.append(int(fib2))
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
print(temp + temp1)