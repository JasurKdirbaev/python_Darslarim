    #for3
"""a = int(input("a = "))
b = int(input("b = "))
n = []
for i in range(a + 1, b):
    n.append(i)
n.reverse()
print(n)"""

    #For6
"""narx = int(input("Bir kilo kanfetning narxini kiriting: "))
n = 1.2
for i in range(1, 5):
    n = n + 0.2
    print(f"{n} kg kanfetning narxi {n*narx}")"""

    #For9
"""
a = int(input("a = "))
b = int(input("b = "))
print("a < b")
n = 0
for i in range(a, b):
    n = n + i**2
print(n)"""

    #For11
"""
n = int(input("n = "))
a = 0
for i in range(0, n):
    a = a + (i + n)**2
    print(a)"""

    #For18

"""
n = int(input("daraja n = "))
m = int(input("haqiqiy son m = "))
a = 0
for i in range(0, n+1):
    a = a + (-m)**i
print(a)"""

    #For20
"""
n = int(input("daraja n = "))
a = 1
s = 0
for i in range(1, n+1):
    a = a*i
    s = s + a
print(s)"""

    #For22
"""n = int(input("daraja n = "))
x = int(input("x haqiqiy son x = "))
a = 1
s = 0
q = 0
for i in range(1, n):
    a = a*i
    s = s + a
    q = q + ((x)**i)/s
print(q)"""

    #For29
"""
n = int(input("n = "))
a = int(input("a = "))
b = int(input("b = "))
m = a
s = (b - a)/n
for i in range(1, n+1):
    m = m + s
    print(m)"""

    #For32
"""
n = int(input("daraja n = "))
s = 1
for i in range(1, n+1):
    a = s
    s = (a+1)/i
    print(s)"""

    #For33
"""
n = int(input("daraja n = "))   #Fibonachi ketma-ketligi
s = 0
a = 1
for i in range(3, n+1):
    a = a + s
    s = s + a
    print(f"a = {a}\ns = {s}")"""

    #For36
"""n = int(input("n = "))
k = int(input("k = "))
s = 0
for i in range(1, n):
    s = s + i**k
    print(s)"""

    #For37
"""
n = int(input("n = "))
s = 0
k = n
for i in range(1, n+1):
    for j in range(1, k+1):
        if i == j:
            s = s + i**j
    print(f"{i}^{i} = {s}")"""

    #For38
"""
n = int(input("n = "))
s = 0
a = 0
for i in range(0, n+1):
    a = n+1 - i
    s = s + i**(a)
    print(s)"""

    #For39
"""A = int(input("A = "))
B = int(input("B = "))
n = B - A
s = 0
for i in range(A, B+1):
    A = A+1
    for j in range(1, A):
        print(A-1)"""

    #For40
A = int(input("A = "))
B = int(input("B = "))
n = B - A
s = 0
for i in range(1, n+1):
    A = A+1
    for j in range(1, i+1):
        print(A-1)
