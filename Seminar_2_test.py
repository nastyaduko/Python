# Задача № 9. По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
# Решить задачу используя цикл while
# Input:       5
# Output:    120

# x = int(input("Введите число "))
# n = 1
# factorial = 1
# while n <= x:
#     factorial *= n 
#     n += 1
# print("Факториал числа", x, "равен", factorial)



# Задача № 11. Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является, то есть выведите такое число n, 
# что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.

# Input:     5

# Output:  6

# Ряд чисел Фибоначчи:
# # 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, …


# n = int(input("Введите целое число "))

# fib1 = 1
# fib2 = 1
# count = 2
# while fib2 < n:
#     fib1, fib2 = fib2, fib1 + fib2 # паралелльное присваивание в одной строке
#     count += 1

# if n == fib2:
#     print(count)
# else:
#     print(-1)


# Задача № 13. Пользователь вводит число N (1 ≤ N ≤ 10). Далее построчно N чисел от -50 до 50. 
# Нужно вывести наибольшее количество идущих подряд положительных чисел.
# Input:    6 -> -20 30 -40 50 10 -10 23 45 12
# Output: 2

# n = int(input("Введите число от 0 до 10 "))
# count = 0
# count_max = 0

# for _ in range (n):
#     c = int(input()) # если нужно рандомно генерировать числа c = randint(-50, 50)
#     if c > 0:
#         count += 1
#         if count > count_max:
#             count_max = count
#     else: 
#         count = 0

# print("Наибольшее число идущих подряд положительных чисел", count_max)
        

# Задача № 15. Пользователь вводит одно число N.  Далее идут N чисел, записанных на новой строчке каждое. Вывести максимальное и минимальное (циклы)
# Input:	5 -> 5 1 6 5 9
# Output:	1 9

# n = int(input("Введите число от 0 до 10 "))
# c = int(input())
# min = c
# max = c

# for _ in range (n-1):
#     c = int(input())
#     if min > c:
#         min = c
#     if max < c:
#         max = c
    
# print(min, max)
        



# word = 'Python'
# len_word = range(len(word))
# print(len_word)
# print(list(len_word))

# for i in len_word:
#     print(i, end=' - ')
#     print(word[i])

# for i in range(len(word)):
#     print(i, end=' - ')
#     print(word[i])
    
# for i in [0,1,2,3,4,5]:
#     print(i, end=' - ')
#     print(word[i])
#     print(word[:i], word[i:])
    
# for i in '012345':
#     i = int(i)
#     print(i, end=' - ')
#     print(word[i])
#     print(word[:i], word[i:])
    
# for letter in word:
#     print(letter, end='-')

# print(enumerate(word))

# for num, elem in enumerate(word, 10):
#     print(num, end=' - ')
#     print(elem)

