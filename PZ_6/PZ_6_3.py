from math import sqrt

N = 3


x = [1, 4, 3]
y = [-1, 1, 0]

def da(x,y):
    a = 0
    b = 0
    for i in x:
        if i < 0 and i < a:
            a = i
        if all(i > 0 for i in x):
            return "0 0"

    for j in y:
        if j > 0 and j > b:
            b = j
        if all(j < 0 for j in y):
            return "0 0"
    return a,b