import math
try:
x = float(input('Введите -1<x<1: ')) #Ввод x
n = int(input('Введите N>0: ')) #Ввод N
a = (-1)**n
b = x**(2*n+1)
c = 2*n+1
vsp = a*b/c
while n>0:
    resul = vsp + vsp
    n = n-1
print(math.atan(resul), "радиан")
except :
print('вы ввели неверное число')