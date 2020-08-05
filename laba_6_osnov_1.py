# ______________________laba_6_ocnov_1______________________

# Постройте графики кривых, заданных параметрически:
# Циклоида (кривая, описанная точкой, лежащей на окружности радиуса R, 
# если эта окружность катится без скольжения по прямой):
# x = R·(t-sin(t))
# y = R·(1-cos(t))

import numpy as np
import matplotlib.pyplot as plt

# ________________________cycloida_____________________________

def cycloida (R,n,k):
    
    t = np.linspace(0, 2*k*np.pi, n)
    
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
         
    plt.xlabel("coord - x")
    plt.ylabel("coord - y")
    plt.title("laba_6_osnov_1_A_cycloida")
    plt.legend()
    plt.axis('equal')
    plt.grid()
        
    plt.plot(x,y,color= "magenta")
    plt.show()
    
cycloida( 2,# радиус
        1000, #количество точек
        4 #количество дуг
        )

# Астроида (кривая, некоторой точки окружности радиуса R/4, 
# катящейся без скольжения по другой окружности радиуса R, 
# причем меньшая окружность все время остается внутри большей):
# x = R·cos3(t)
# y = R·sin3(t)

# ________________________astroida_____________________________

def astroida (R,n):
    
    t = np.linspace(0, 2*np.pi, n)
    
    x = R * np.cos(t)**3
    y = R * np.sin(t)**3
         
    plt.xlabel("coord - x")
    plt.ylabel("coord - y")
    plt.title("laba_6_osnov_1_B_astroida")
    plt.legend()
    plt.axis('equal')
    plt.grid()
        
    plt.plot(x,y,color= "navy")
    plt.show()
    
astroida ( 20,# радиус
        150, #количество точек
        )