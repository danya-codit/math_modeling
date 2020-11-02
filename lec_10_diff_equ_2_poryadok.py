import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# peremennaya
x = np.arange(0, 10, 0.01)

# opredelyaem funk
def diff_funk(z,x): # z - izmenenyarmaya vel
    y, omega = z # ukazanie izmen funk 
    
    dtheta_dx = omega # 1 orave sistem
    domega_dx = np.sin(y) * omega - 3*x*y - 5   
    return dtheta_dx, domega_dx # funk return znachenie proizvodnih

# opredelyaim start znach 
    
theta0 = np.pi - 0.1
omega0 = 0
z0 = theta0,omega0 # start value
b = 0.25
c = 5.0
# rashem sistem ekuanion
sol = odeint(diff_funk, z0, x)

#ctroim colve how 
plt.plot(sol[:,1],sol[:,0], 'g', label='theta(omega)')
plt.plot(t,sol[:,0], 'b')
plt.plot(t,sol[:,1], 'b')
plt.legend()
plt.show()

