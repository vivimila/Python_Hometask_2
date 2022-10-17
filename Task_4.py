# 5. Напишите программу, которая принимает на вход координаты двух точек и 
# находит расстояние между ними в 2D пространстве.

import math
try:
coordA = []
for i in range(2):
coordA.append(int(input("введите координату точки А: ")))
coordB = []
for i in range(2):
coordB.append(int(input('введите координату точки В: ')))
print(coordA, coordB)

distan = math.sqrt((coordB[0]- coordA[0])**2 + (coordB[1]- coordA[1])**2)
print(round(distan, 3))
except:
print('Введите числа')