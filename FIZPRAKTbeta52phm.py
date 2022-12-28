from math import *
from decimal import Decimal as D
print("Для количества измерений n <= 10, P = 95%")
t = [0,0,0,12.7,4.3,3.18,2.78,2.45,2.36,2.31,2.26]
bt = [0,0,0,1.41,1.64,1.87,2,2.09,2.17,2.24,2.29,2.62]
n = int(input("Введите количество измерений: "))
*ls, = map(D,input("Введите измерения через пробел: ").split())
w = 1
while True:
    mid = sum(ls) / n
    d = []
    d2 = []
    mx = 0
    f = 0
    for i in range(n):
        d += ls[i] - mid,
        if(mx < sqrt(d[-1] ** 2)):
            mx = sqrt(d[-1] ** 2)
            f = i
        d2 += d[-1] ** 2,
    sx = sqrt(sum(d2) / (n - 1))
    be = mx / (sqrt((n - 1) / n) * sx)
    print(w,"Таблица")
    w+=1
    print("n    d   di-d    (di-d)^2")
    for i in range(n):
        print(f'{i + 1}    {ls[i]}    {d[i]}    {d2[i]}')
    print(f"dср = {mid}    Sx = {sx}   Bэксп = {be}    Bтабл = {bt[n]}")
    if be <= bt[n]:
        break
    else:
        print(f"Есть промах: {ls[f]}")
        ls.pop(f)
        n -= 1
dd = t[n] * sx / sqrt(D(str(n)))
eps = D(str(dd)) / mid * 100        
print(f"t = {t[n]}")
print(f"Ответ: dср + дельтаd = {mid} + {dd:.9f}     e = {eps}")
print("Округление делайте сами")