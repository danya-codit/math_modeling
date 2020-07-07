# Создать функцию, определяющую площади круга, прямоугольника и треугольника по соответствующим параметрам,
# в зависимости от того, какую фигуру выберет пользователь.
from math import pi
print("________________________laba_4_osnov_5_____________________")
rr = int(input("vvedi radius "))

aa= int(input("vvedi storonu pramougolnik a "))
bb = int(input("vvedi smegnuyou s a storonu pramougolnika b "))

cc = int(input("vvedi storonu treugolnika c "))
hh = int(input("vvedi visotu treugolnika h "))
def funk (r = rr, a = aa, b = bb, c = cc, h = hh):
    print("esli nuzhen crug vvedi 1")
    print("esli nuzhen pramougolnik vvedi 2")
    print("esli nuzhen treugolnik vvedi 3")
    k = int(input())
    if k == 1:
        s = pi * r**2
    else:
        if k == 2:
            s = a * b
        else:
            if k == 3:
                s = c * h / 2
            else:
                s = ("pora v durku")
    return s
print(funk())