A = []
B = []
simv = int(input("Введите колличество символов в массивах: "))
N=0
while N<simv:
  A.append(int(input("Введите элемент массива a: ")))
  B.append(int(input("Введите элемент массива b: ")))
  N += 1
A,B = B,A
print("Массив а")
print(A)
print("Массив b")
print(B)
