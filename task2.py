# Напишите программу, которая принимает на вход число N
# и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.
# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)

num = int(input('Введите число: '))
result = 1
for i in range(1, num):
    result = i * result
    print((result), end = ", ")
print(result * (i + 1))