import math
def Mean(X, Y, Result):
    Result['AMean'] = (X + Y) / 2
    Result['GMean'] = math.sqrt(X * Y)
    return
R = {'AMean' : None, 'GMean' : None}

A = int(input("Введите A"))
B = int(input("Введите B"))
C = int(input("Введите C"))
D = int(input("Введите D"))

print("A, B")
Mean(A,B,R)
print('AMean = ', R['AMean'])
print('GMean = ', R['GMean'])

print("A, C")
Mean(A,C,R)
print('AMean = ', R['AMean'])
print('GMean = ', R['GMean'])

print("A, D")
Mean(A,D,R)
print('AMean = ', R['AMean'])
print('GMean = ', R['GMean'])