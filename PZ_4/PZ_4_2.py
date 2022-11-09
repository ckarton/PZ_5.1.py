a = int(input('Введите a>0: ')) #Ввод a
k = int(input('Введите K>a: ')) #Ввод K
resul = 1
while k>a:
    vsp = 1/k
    resul = resul + vsp
    k = k-1
print(resul)
