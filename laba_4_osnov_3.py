# Создайте функцию, определяющую полную механическую энергию тела,
# подброшенного на определенную высоту и определенной скоростью над поверхностью Земли.
# В качестве входных аргументов функции определить: массу тела, высоту полета и скорость
# (все необходимые константы взять из модуля констант).
print("________________________laba_4_osnov_3_____________________")
m = int (input ("vvedi massu tela "))
h = int (input ("vvedi visotu poleta "))
v = int (input ("vvedi skorost tela "))
def funk (massa_tela = m, visota_poleta = h, skorost_tela = v):
    from astro_constants import acceleration_of_gravity_ears as g
    m = massa_tela
    h = visota_poleta
    v = skorost_tela
    E = m * v**2 / 2 + m * g *h
    return E
print(funk())