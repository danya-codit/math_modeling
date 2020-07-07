# Создать функцию, определяющую параметры изображения (уменьшенное / увеличенное,
# действительное / мнимое, прямое / обратное), по заданным параметрам линзы
# (собирающая / рассеивающая, расстояние от предмета до линзы / фокусное расстояние линзы).
print("________________________laba_4_dop_3_____________________")
FF = float(input("vvedi фокусное расстояние линзы F "))
dd = float(input("введи  расстояние от предмета до линзы d "))
def funk (F = FF, d = dd):
    print()
    A = []
    w = 0
    if F < 0:
        return("rasstoyanie ne otritsatelno, pora v durku")
    if d < 0:
        print("vi uvereni chto predmet mnimi")
        h =input("yes or no : ")
        if h == "yes":
            print("ok")
            w = 1
        else:
            if h == "no":
                return"pora v durku"
            else:
                return "pora v durku"
    print("esli sobirayoushaya linza vvedi 1")
    print("esli rasseivayoushya linza vvedi 2")
    l = int(input())
    if l == 1 and w == 0:
        A.append("izobrazenie : perevernutoe, ")
        f = 1 / (1 / F  -  1 / d)
        if d < f:
            A.append("uvelichenoe, ")
        if d == f:
            A.append("pryamoe, ")
        if d > f:
            A.append("umenshenoe, ")
        if f < 0:
            A.append("mnimoe, ")
        if f > 0:
            A.append("deistvitelnoe, ")
    else:
        if l == 1 and w == 1:
            A.append("do svyazy ...")
            A.append("................na praktike takoe ne vozmozno!!!!!!!!!")
        else:
            return "pora v durku"
    if l == 2 and w == 0:
        A.append("izobrazenie : pryamoe, ")
        f = 1 / (1 / -F  -  1 / d)
        if d < f:
            A.append("uvelichenoe, ")
        if d == f:
            A.append("pryamoe, ")
        if d > f:
            A.append("umenshenoe, ")
        if f < 0:
            A.append("mnimoe, ")
        if f > 0:
            A.append("deistvitelnoe, ")
    else:
        if l == 1 and w == 1:
            A.append("do svyazy ...")
            A.append("................na praktike takoe ne vozmozno!!!!!!!!!")
        else:
            return "pora v durku"
print(funk())