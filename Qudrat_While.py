    #While1 While2
"""A = int(input("A = "))
B = int(input("B = "))
s = 0
a = 0
while True:
    s = s + B
    a = a + 1
    if s>A:
        print("A kesmaning bo'sh qismi",-(s-B-A), "va", a-1, "marta joylashtirirsh mumkin")
        break"""

    #While-4
"""a = 0
s = 0
q = 3
c = 0
n = int(input("Uchning darajasi bo'lgan sonlarni kiriting: "))
while True:
    a = a + 1
    s = s + c + q
    c = s
    q = s
    if n==s:
        print(f"{n} 3 ning {a} darajasi")
        break"""


        #While-5
"""
s = 1
a = 2
n = int(input("Ikkining darajasi bo'lgan sonlarni kiriting: "))
while True:
    s = s + 1
    q = a
    a = a + q
    if a==n:
        print(f"2 ning {s} darajasi")
        break"""

    #While-6
"""n = int(input("n = "))
a = 1
while n>=2:
    a *=n
    n -=2
    print(a)"""

    #While-7
"""n = int(input("n = "))
k = 0
a = 0
while n>a:
    k = k + 1
    a = k**2
print(k)"""

    #While-15
"""summa = int(input("Summa = "))
foiz = int(input("foiz = "))
oy = 0
summa2 = summa
while summa2<2*summa:
    oy += 1
    summa2 += (summa2*foiz)/100
    print(f"{oy} - oyda {summa2} so'm bo'ladi")"""