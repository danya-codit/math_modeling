# __________________laba_13_2___________________

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation


# defining a variable value

seconds_in_year = 365*24*3600
seconds_in_day = 24*3600
years = 10

t = np.arange(0, years*seconds_in_year, seconds_in_day)

# define a function for a system of difequations

def danya_gravition_func (s,t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3) = s
    
    # dynamics of 1 body under the influence of 2 and 3
    dxdt1 = v_x1
    dv_xdt1 = (-G * m2 * (x1 -x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
               -G * m2 * (x1 -x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
               + k * q1 * q2 / m1 * (x1 - x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
               + k * q1 * q3 / m1 * (x1 - x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5)
               
    dydt1 = v_y1
    dv_ydt1 = (-G * m2 * (y1 -y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
                -G * m2 * (y1 -y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
                + k * q1 * q2 / m1 * (y1 - y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
                + k * q1 * q3 / m1 * (y1 - y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5)

    # dynamics of 2 body under the influence of 1 and 3
    dxdt2 = v_x2
    dv_xdt2 = (-G * m1 * (x2 -x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
               -G * m3 * (x2 -x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
               + k * q2 * q1 / m2 * (x2 - x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
               + k * q2 * q3 / m2 * (x2 - x3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5)
               
    dydt2 = v_y2
    dv_ydt1 = (-G * m1 * (y2 -y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
               -G * m3 * (y2 -y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5
               + k * q2 * q1 / m2 * (y2 - y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
               + k * q2 * q3 / m2 * (y2 - y3) / ((x2 - x3)**2 + (y2 - y3)**2)**1.5)
               
    # dynamics of 3 body under the influence of 1 and 2
    dxdt3 = v_x3
    dv_xdt2 = (-G * m1 * (x3 -x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
               -G * m2 * (x3 -x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5
               + k * q3 * q1 / m3 * (x3 - x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
               + k * q3 * q2 / m3 * (x3 - x2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5)
               
    dydt3 = v_y3
    dv_ydt3 = (-G * m1 * (y3 -y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
               -G * m2 * (y3 -y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5
               + k * q3 * q1 / m3 * (y3 - y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
               + k * q3 * q2 / m3 * (y3 - y2) / ((x3 - x2)**2 + (y3 - y2)**2)**1.5)
               
    return(
       dxdt1, dv_xdt1, dydt1, dv_ydt1,
       dxdt2, dv_ydt1, dydt2, dv_ydt1,
       dxdt3, dv_xdt2, dydt3, dv_ydt3
           )

# defining the initial values

x10 = 149 * 10**9
v_x10 = 0
y10 = 0
v_y10 = 20000

x20 = -149 * 10**9
v_x20 = 1
y20 = 0
v_y20 = 15000

x30 = 0
v_x30 = 10000
y30 = 149 * 10**9 * 1.73
v_y30 = 0

s0 = (
      x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30
      )

m1 = 1.5 * 10**(30)
q1 = 1.5 * 1020

m2 = 3 * 10**(30)
q2 = 3 * 1020

m3 = 4.3 * 10**(30)
q3 = 4.3 * 1020

G = 6.67 * 10**(-11)
k = 8.98755 * 10**9

# solving a system of dif equations

sol = odeint(danya_gravition_func, s0, t)

# building a solution as a graph and animating it

fig = plt.figure()
bodys = []

for i in range(0, len(t), 1):
    body1 = plt.plot(sol[:i, 0], sol[:i, 2], '-', color='magenta')
    # body1_line, = plt.plot(sol[:i, o], sol[:i, 2], 'o', color='magenta')
    
    body2 = plt.plot(sol[:i, 4], sol[:i, 6], '-', color='darkorange')
    body2_line, = plt.plot(sol[:i, 4], sol[:i, 6], 'o', color='darkorange')
    
    body3 = plt.plot(sol[:i, 8], sol[:i, 10], '-', color='navy')
    body3_line, = plt.plot(sol[:i, 8], sol[:i, 10], 'o', color='navy')
    
    bodys.append([body1,
                  # body1_line, 
                  body2, body2_line, body3, body3_line])
    
ani = ArtistAnimation(fig, bodys, interval=50)
plt.axis('equal')
ani.save('laba_13_2.gif')