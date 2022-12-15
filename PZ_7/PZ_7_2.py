a = input("Введите предложение ")
s = a.split()
print (len(max(s, key=len)))
