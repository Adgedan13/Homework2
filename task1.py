# Напишите программу, которая принимает на вход вещественное число
# и показывает сумму его цифр. Учтите, что числа могут быть отрицательными
# Пример:
# 67.82 -> 23
# (-0.56) -> 11

num = input('Введите число: ')
sum_num = 0
for i in num:
    if i.isdigit():
        sum_num += int(i)

print (f'Сумма цифр числа {num} → {sum_num}')