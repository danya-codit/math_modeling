import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# peremennaya
x = np.arange(-0.9, 0.9, 0.01)

# opredelyaem funk
def diff_funk(z,x): # z - izmenenyarmaya vel
    y, omega = z # ukazanie izmen funk 
    
    dy_dx = omega # 1 orave sistem
    domega_dx = (n**2*y + x*omega) / (1-x**2)
    return dy_dx, domega_dx # funk return znachenie proizvodnih

# opredelyaim start znach 
    
y0 = 10
omega0 = 40
z0 = y0,omega0 # start value
n = 0.01

# rashem sistem ekuanion
sol = odeint(diff_funk, z0, x)

##ctroim colve how 
#plt.plot(sol[:,1],sol[:,0], 'g', label='y(omega)')
plt.plot(x,sol[:,0], 'b')
#plt.plot(t,sol[:,1], 'b')
plt.legend()
plt.show()

