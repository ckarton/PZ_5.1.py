a = input("Введите предложение ")
s = a.split()
print(max(s, key=len))