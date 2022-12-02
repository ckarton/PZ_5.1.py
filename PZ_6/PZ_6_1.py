try:
    a = []

    N = int(input("Введите размер списка N: "))

    for i in range(N):
        a.append(int(input("Введите элемент массива: ")))

    K = int(input("Введите K>1: "))
    L = int(input("Введите N>L>=k: "))

    sum = 0
    for i in range(0, K - 1):
        sum += a[i]
    for i in range(L, N):
        sum += a[i]

    c = sum / len(sum)
    print(c)
except:
    print("Перезагрузите или попробуте позже")