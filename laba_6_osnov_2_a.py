print('___________________________laba_6_osnov_2_A_cycloida__________________________')
print('Функция, строящая графики кривых, заданных параметрически: Циклоиды и Астроиды')

import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.animation as anim         

fig, ax = plt.subplots()                                                                              #Создание пространства и подпространства для анимации  

anim_object, = plt.plot([], [], marker='o', color='darkorange', ms=50, label='Cicloida')                  #Создание анимируемого объкта

def cicloida_move(R, angle, time):
    """Функция строит циклоиду:
       На вход подаются:
       R - радиус окружности
       angle, time параметры
    """
    t = angle * (np.pi / 180) * time
    
    x = R * (t - np.sin(t))
    y = R * (1 - np.cos(t))
    
    return x, y  

ax.set_xlim(-1, 20) #Пределы изменения переменной X
ax.set_ylim(-2, 4)  #Пределы изменения переменной Y

def animate(i):
    anim_object.set_data(cicloida_move(R = 1, angle = 1, time=i))
    ax.set_title('time csiferka{}'.format(i))

animation_6_2 = anim.FuncAnimation(fig, animate, frames=1000, interval=0.1)

sub = cicloida_move(R = 1, #radius
                    angle = 360,
                    time = np.arange(0, 2 * np.pi, 0.01))
plt.plot(sub[0],sub[1], color = 'navy')
animation_6_2.save('laba_6_osnov_1_A_cycloida.gif')
