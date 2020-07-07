# Написать функцию, которая вычисляет среднее арифметическое элементов одномерного массива,
#  переданного ей в качестве аргумента.
import numpy as np
print("________________________laba_4_osnov_1__________________")
A = []
col = int (input ("vvedi colichestvo elementov massiva "))
print("vvedi eleventi massiva :" )
i = 0
while i < col:
    d = int (input ())
    A.append(d)
    i = i + 1
B = np.array(A)
def funk (B):
    x = len(B)
    y = sum(B)
    srar = y / x
    return srar
print(funk(B))