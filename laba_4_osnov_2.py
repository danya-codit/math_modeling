# Создайте функцию, которая перемножает все элементы входного одномерного массива
import numpy as np
print("________________________laba_4_osnov_2_____________________")
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
    k = 0
    peremnozili = 1
    while k < len(B):
        peremnozili = peremnozili * B[k]
        k = k + 1
    return peremnozili
print(funk(B))