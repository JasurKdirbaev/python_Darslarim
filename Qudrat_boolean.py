    #Boolean-3
A = int(input("Son kiriting: "))
print(A % 2 == 0)

    #Boolean-5
A = int(input("A butun son A = "))
B = int(input("B butun son B = "))
print(A >= 0 and B < -2)

    #Boolean-7
A = int(input("A butun son A = "))
B = int(input("B butun son B = "))
C = int(input("C butun son C = "))
print(B > A and B < C)

    #Boolean-11
A = int(input("A butun son A = "))
B = int(input("B butun son B = "))
print((A % 2 == 0 and B % 2 == 0) or (A % 2 != 0 and B % 2 != 0))

    #Boolean-15
A = int(input("A butun son A = "))
B = int(input("B butun son B = "))
C = int(input("C butun son C = "))
print((A > 0 and B > 0 and C < 0) or (A > 0 and B < 0 and C > 0) or (A < 0 and B > 0 and C > 0))

    #Boolean-17
A = int(input("Son kiriting: "))
print(len(str(A)) == 3 and A % 2 != 0)

    #Boolean-19
A = int(input("A butun son A = "))
B = int(input("B butun son B = "))
C = int(input("C butun son C = "))
print((A == abs(B) or abs(B) == C) or (A == abs(C) or abs(C) == B) or (B == abs(A) or abs(A) == C))

    #Boolean-23
n = int(input("Uch xonali son kiriting: "))
birlar = int(n % 10)
onlar = int((n % 100) / 10)
yuzlar = int(n / 100)
print(birlar == yuzlar)

    #Boolean-28
x = int(input("x butun son x = "))
y = int(input("y butun son y = "))
print((x < 0 and y > 0) or (x < 0 and y < 0))

    #Boolean-29
x = int(input("x butun son x = "))
x1 = int(input("x1 butun son x1 = "))
x2 = int(input("x2 butun son x2 = "))
y = int(input("y butun son y = "))
y1 = int(input("y1 butun son y1 = "))
y2 = int(input("y2 butun son y2 = "))
print((x > x1 and x < x2) and (y > y2 and x < y1))

    #Boolean-37 shoh yurishi
x1 = int(input("x1 butun son x1 = "))
x2 = int(input("x2 butun son x2 = "))
y1 = int(input("y1 butun son y1 = "))
y2 = int(input("y2 butun son y2 = "))
print((abs(x2-x1) == 1 and abs(y1-y2) == 1) or (abs(x2-x1) == 0 and abs(y1-y2) == 1) or (abs(x2-x1) == 1 and abs(y1-y2) == 0))

    #Boolean-38 Fil yurishi
x1 = int(input("x1 butun son x1 = "))
x2 = int(input("x2 butun son x2 = "))
y1 = int(input("y1 butun son y1 = "))
y2 = int(input("y2 butun son y2 = "))
print((abs(x2-x1) > 0 and abs(y1-y2) == 0) or (abs(x2-x1) == 0 and abs(y1-y2) > 0))

    #Boolean-40 Ot yurishi
x1 = int(input("x1 butun son x1 = "))
x2 = int(input("x2 butun son x2 = "))
y1 = int(input("y1 butun son y1 = "))
y2 = int(input("y2 butun son y2 = "))
print((abs(x2-x1) == 2 and abs(y1-y2) == 1) or (abs(x2-x1) == 1 and abs(y1-y2) == 2))


