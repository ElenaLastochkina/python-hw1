# 1 Напишите программу, которая принимает на вход цифру, обозначающую день недели, 
# и проверяет, является ли этот день выходным.
# *Пример:*
# 6 -> да
# 7 -> да
# 1 -> нет
number = int(input("введите число дня недели от 1 до 7"))
print (number)
if number == 1 or number == 2 or number == 3 or number == 4 or number == 5:
 print("нет, это рабочий день")
elif number == 6 or number == 7:
 print("да, это выходной день")
else:
 print("введено значение не соответсвующее условию")

#2* Напишите программу для. проверки истинности утверждения 
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

#3 Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
#*Пример:*
# x=34; y=-30 -> 4
# x=2; y=4-> 1
# x=-34; y=-30 -> 3
x = int(input("введите координату х:"))
y = int(input ("введите координату у:"))
if x>0 and y>0:
 print("точка лежит во 1й четверти")
elif x<0 and y>0:
 print("точка лежит во 2-й четверти")
elif x<0 and y<0:
 print("точка лежит в 3-й четверти") 
elif x>0 and y<0:
 print("точка лежит в 4-й четверти")
else:
 print("точка лежит на координатной прямой")
 
#4 Напишите программу, которая по заданному номеру четверти, 
# показывает диапазон возможных координат точек в этой четверти (x и y).
i = int(input("введите четверть от 1 до 4:"))
if (i ==1):
 print("x>0 & y>0")
elif (i ==2):
 print("x<0 & y>0")
elif(i ==3):
 print("x<0 & y<0")
elif (i ==4):
 print("x>0 & y<0")
 
#5 Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
#*Пример:*
 # A (3,6); B (2,1) -> 5,09
 # A (7,-5); B (1,-1) -> 7,21
x1 = int(input("введите x1:"))
y1 = int(input ("введите y1:"))
x2 = int(input ("введите x2:"))
y2 = int(input ("введите y2:"))
print(((y2-y1)*(y2-y1) + (x2-x1)*(x2-x1))**0.5)