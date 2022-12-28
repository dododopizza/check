from random import randint 
a = []
for i in range(10):
    a += randint(1,100),
def insert1(A:list,S1,S2):
    B = []
    mx = max(A)
    key = 0
    for elem in A:
        if elem == mx and key == 0:
            B += S1,
            B += elem,
            B += S2,
            key = 1
        else:
            B += elem,
    return B
print("NO changes")
print(*a)
print("insert pered maximum 5 posle maximum -1")
print(*insert1(a,5,-1))
