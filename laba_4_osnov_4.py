# Написать функцию, которая вычисляет значения какой-либо простой функции, например,
# y = x2 на промежутке a < x < b в N точках. Функция возвращает массив значений.
import numpy as np
print("________________________laba_4_osnov_4_____________________")
a = int (input ("vvedi min znachenie po x "))
b = int (input ("vvedi max znachenie po x "))
def funk (minn = a, maxx = b):
    """ Функция y = x**3
    """
    A = np.linspace(minn, maxx, 10)
    i = 0
    while i < 10:
        d = A[i] ** 3
        A.append(d)
        i += 1
    return A
print(funk())