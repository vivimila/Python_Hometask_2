#Напишите программу, которая принимает на вход вещественное 
#или целое число и показывает сумму его цифр. Через строку нельзя решать.

n = int(input('Введите число: '))
 
sum = 0
 
while n > 0:
    digit = n % 10
    sum = sum + digit
    n = n // 10
 
print(f'Сумма чисел равна: {sum}')
