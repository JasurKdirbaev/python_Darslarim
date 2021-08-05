    #Integer-3
"""bayt = int(input("Fayl hajmini baytlarda kiriting: "))
Kbayt = 1024
print("Fayl hajmi ", bayt / Kbayt, "Kbayt ga teng:")"""

    #Integer-4+5
"""A = int(input("A > B shartni qanoatlantirsin\nA kesmani kiriting: "))
B = int(input("B kesmani kiriting: "))
print("A kesmada B kesma", int(A/B), "marta joylashgan")
print("B kesmaning A kesmada joylashmagan qismi ", B - (A - (int(A/B)*B)), "ga teng")"""

    #Integer-12
"""n = int(input("Uch xonali son kiriting: "))
birlar = n % 10
onlar = int((n % 100 - birlar)/10)
yuzlar = int((n - (n % 100)) / 100)
print(str(birlar) + str(onlar) + str(yuzlar))
print(str(onlar) + str(birlar) + str(yuzlar))"""

    #Integer-17
"""n = int(input("999 dan katta son kiriting: "))
yuzliklar = (n % 1000 - n % 100) / 100
print(int(yuzliklar))"""

    #Integer-23
"""sekund = int(input("Kun boshidan boshlab qancha sekund o'tdi: "))
minut = int(sekund / 60)
saot = int(sekund / 3600)
print("kun boshidan", minut, "minut va ", saot, "saot o'tdi")"""

    #Integer-24
"""print("0-yakshanba, 1-dushanba, 2-seshanba, 3-chorshanba, 4-payshanba, 5-juma, 6-shanba\n1-yanvar dushanbaga to'g'ri keladi")
K = int(input("1 - 365 sonlari orasida yotuvchi sonni kiriting: "))
n = K % 7
print(K , "haftaning ", n, "- kuniga teng")"""

    #Integer-25
"""print("0-yakshanba, 1-dushanba, 2-seshanba, 3-chorshanba, 4-payshanba, 5-juma, 6-shanba\n1-yanvar payshanbaga to'g'ri keladi")
K = int(input("1 - 365 sonlari orasida yotuvchi sonni kiriting: "))
n = K % 7
print(K , "haftaning ", n+3, "- kuniga teng")"""

   #Integer-26
"""print("0-yakshanba, 1-dushanba, 2-seshanba, 3-chorshanba, 4-payshanba, 5-juma, 6-shanba\n1-yanvar seshanbaga to'g'ri keladi")
K = int(input("1 - 365 sonlari orasida yotuvchi sonni kiriting: "))
n = K % 7
print(K , "haftaning ", n+1, "- kuniga teng")"""

   #Integer-28
"""print("0-yakshanba, 1-dushanba, 2-seshanba, 3-chorshanba, 4-payshanba, 5-juma, 6-shanba")
N = int(input("1 - yanvar haftaning qaysi kuniga to'g'ri keladi: "))
K = int(input("1 - 365 sonlari orasida yotuvchi sonni kiriting: "))
n = K % 7
print(K , "haftaning ", n+N-1, "- kuniga teng")"""

    #Integer-29
A = int(input("To'g'ri to'rtburchakning A tomonini kiriting: "))
B = int(input("To'g'ri to'rtburchakning B tomonini kiriting: "))
C = int(input("Kvadratning C tomonini kiriting: "))
print("To'g'ri to'rtburchak ichiga", (A//C) * (B//C), "ta kvadrat joylashtirish mumkin!!!")
print("Sig'magan kvadrat yuzi", (A+C-(A%C)) * (B+C-(B%C)) - (A*B))