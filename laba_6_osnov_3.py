print('______laba_6_osnov_3_sin____')
print('Функция, строящая график sin')

import matplotlib.pyplot as plt 
import numpy as np
import matplotlib.animation as anim         

fig, ax = plt.subplots()                                                                              #Создание пространства и подпространства для анимации  

anim_object, = plt.plot([], [], marker='o', color='darkorange', ms=50, label='sin')                  #Создание анимируемого объкта

def sin_move(angle, time):
    """Функция строит sin:
       На вход подаются:
       angle, time параметры
    """
    t = angle * (np.pi / 180) * time
    
    x = t
    y = np.sin(x)
    
    return x, y  

ax.set_xlim(-1, 20) #Пределы изменения переменной X
ax.set_ylim(-2, 4)  #Пределы изменения переменной Y

def animate(i):
    anim_object.set_data(sin_move(angle = 1, time=i))
    ax.set_title('time csiferka{}'.format(i))

animation_6_3 = anim.FuncAnimation(fig, animate, frames=1000, interval=0.1)

sub = sin_move(angle = 360,
                    time = np.arange(0, 2 * np.pi, 0.01))
plt.plot(sub[0],sub[1], color = 'navy')
animation_6_3.save('laba_6_osnov_3_sin.gif')



