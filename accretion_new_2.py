# __________________tidal_forces___________________

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from matplotlib.animation import ArtistAnimation


# defining a variable value

seconds_in_year = 365*24*3600
seconds_in_day = 24*3600
years = 1

t = np.arange(0, years*seconds_in_year, seconds_in_day)

# define a function for a system of difequations

def danya_gravition_func (s,t):
    (x1, v_x1, y1, v_y1,
     x2, v_x2, y2, v_y2,
     x3, v_x3, y3, v_y3,
     x4, v_x4, y4, v_y4,
     x5, v_x5, y5, v_y5,
     x6, v_x6, y6, v_y6,
     x7, v_x7, y7, v_y7,
     x8, v_x8, y8, v_y8,
     x9, v_x9, y9, v_y9,
     x10, v_x10, y10, v_y10,
     x11, v_x11, y11, v_y11

     ) = s
    
     # dynamics of 1 body under the influence of 2 3 4 5 6 7 8 9 10
    dxdt1 = v_x1
    dv_xdt1 = (-G * m2 * (x1 -x2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
               -G * m3 * (x1 -x3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
               -G * m4 * (x1 -x4) / ((x1 - x4)**2 + (y1 - y4)**2)**1.5
               -G * m5 * (x1 -x5) / ((x1 - x5)**2 + (y1 - y5)**2)**1.5
               -G * m6 * (x1 -x6) / ((x1 - x6)**2 + (y1 - y6)**2)**1.5
               -G * m7 * (x1 -x7) / ((x1 - x7)**2 + (y1 - y7)**2)**1.5
               -G * m8 * (x1 -x8) / ((x1 - x8)**2 + (y1 - y8)**2)**1.5
               -G * m9 * (x1 -x9) / ((x1 - x9)**2 + (y1 - y9)**2)**1.5
               -G * m10 * (x1 -x10) / ((x1 - x10)**2 + (y1 - y10)**2)**1.5
               )
               
    dydt1 = v_y1
    dv_ydt1 = (-G * m2 * (y1 -y2) / ((x1 - x2)**2 + (y1 - y2)**2)**1.5
               -G * m3 * (y1 -y3) / ((x1 - x3)**2 + (y1 - y3)**2)**1.5
               -G * m4 * (y1 -y4) / ((x1 - x4)**2 + (y1 - y4)**2)**1.5
               -G * m5 * (y1 -y5) / ((x1 - x5)**2 + (y1 - y5)**2)**1.5
               -G * m6 * (y1 -y6) / ((x1 - x6)**2 + (y1 - y6)**2)**1.5
               -G * m7 * (y1 -y7) / ((x1 - x7)**2 + (y1 - y7)**2)**1.5
               -G * m8 * (y1 -y8) / ((x1 - x8)**2 + (y1 - y8)**2)**1.5
               -G * m9 * (y1 -y9) / ((x1 - x9)**2 + (y1 - y9)**2)**1.5
               -G * m10 * (x1 -x10) / ((x1 - x10)**2 + (y1 - y10)**2)**1.5
                )

    # dynamics of 2 body under the influence of 1 
    dxdt2 = v_x2
    dv_xdt2 = (-G * m1 * (x2 -x1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
               )
               
    dydt2 = v_y2
    dv_ydt2 = (-G * m1 * (y2 -y1) / ((x2 - x1)**2 + (y2 - y1)**2)**1.5
               )
               
    # dynamics of 3 body under the influence of 1 
    dxdt3 = v_x3
    dv_xdt3 = (-G * m1 * (x3 -x1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
               )
               
    dydt3 = v_y3
    dv_ydt3 = (-G * m1 * (y3 -y1) / ((x3 - x1)**2 + (y3 - y1)**2)**1.5
               )
    
    # dynamics of 4 body under the influence of 1 
    dxdt4 = v_x4
    dv_xdt4 = (-G * m1 * (x4 -x1) / ((x4 - x1)**2 + (y4 - y1)**2)**1.5
               )
               
    dydt4 = v_y4
    dv_ydt4 = (-G * m1 * (y4 -y1) / ((x4 - x1)**2 + (y4 - y1)**2)**1.5
               )           
    
    # dynamics of 5 body under the influence of 1 
    dxdt5 = v_x5
    dv_xdt5 = (-G * m1 * (x5 -x1) / ((x5 - x1)**2 + (y5 - y1)**2)**1.5
              )
               
    dydt5 = v_y5
    dv_ydt5 = (-G * m1 * (y5 -y1) / ((x5 - x1)**2 + (y5 - y1)**2)**1.5
               )   
    
    # dynamics of 6 body under the influence of 1 
    dxdt6 = v_x6
    dv_xdt6 = (-G * m1 * (x6 -x1) / ((x6 - x1)**2 + (y6 - y1)**2)**1.5
               )
               
    dydt6 = v_y6
    dv_ydt6 = (-G * m1 * (y6 -y1) / ((x6 - x1)**2 + (y6 - y1)**2)**1.5
               )
    
    # dynamics of 7 body under the influence of 1 
    dxdt7 = v_x7
    dv_xdt7 = (-G * m1 * (x7 -x1) / ((x7 - x1)**2 + (y7 - y1)**2)**1.5
               )
    
    dydt7 = v_y7
    dv_ydt7 = (-G * m1 * (y7 -y1) / ((x7 - x1)**2 + (y7 - y1)**2)**1.5
               )
     # dynamics of 8 body under the influence of 1 
    dxdt8 = v_x8
    dv_xdt8 = (-G * m1 * (x8 -x1) / ((x8 - x1)**2 + (y8 - y1)**2)**1.5
               )
               
    dydt8 = v_y8
    dv_ydt8 = (-G * m1 * (y8 -y1) / ((x8 - x1)**2 + (y8 - y1)**2)**1.5
               )
    # dynamics of 9 body under the influence of 1 
    dxdt9 = v_x9
    dv_xdt9 = (-G * m1 * (x9 -x1) / ((x9 - x1)**2 + (y9 - y1)**2)**1.5
               )
               
    dydt9 = v_y9
    dv_ydt9 = (-G * m1 * (y9 -y1) / ((x9 - x1)**2 + (y9 - y1)**2)**1.5
               )
    
    # dynamics of 10 body under the influence of 1 
    dxdt10 = v_x10
    dv_xdt10 = (-G * m1 * (x10 -x1) / ((x10 - x1)**2 + (y10 - y1)**2)**1.5
               )
               
    dydt10= v_y10
    dv_ydt10 = (-G * m1 * (y10 -y1) / ((x10 - x1)**2 + (y10 - y1)**2)**1.5
               )
    
    # dynamics of 11 body under the influence of 1 
    dxdt11 = v_x11
    dv_xdt11 = (-G * m1 * (x11 -x1) / ((x11 - x1)**2 + (y11 - y1)**2)**1.5
               )
               
    dydt11 = v_y11
    dv_ydt11 = (-G * m1 * (y11 -y1) / ((x11 - x1)**2 + (y11 - y1)**2)**1.5
               )
  

    return (
       dxdt1, dv_xdt1, dydt1, dv_ydt1,
       dxdt2, dv_xdt2, dydt2, dv_ydt2,
       dxdt3, dv_xdt3, dydt3, dv_ydt3,
       dxdt4, dv_xdt4, dydt4, dv_ydt4,
       dxdt5, dv_xdt5, dydt5, dv_ydt5,
       dxdt6, dv_xdt6, dydt6, dv_ydt6,
       dxdt7, dv_xdt7, dydt7, dv_ydt7,
       dxdt8, dv_xdt8, dydt8, dv_ydt8,
       dxdt9, dv_xdt9, dydt9, dv_ydt9,
       dxdt10, dv_xdt10, dydt10, dv_ydt10,
       dxdt11, dv_xdt11, dydt11, dv_ydt11
       )

# defining the initial values

step = 3631040000

x10 = step * 0
v_x10 = 1000
y10 = step * 0
v_y10 = 0

x20 = step * 3
v_x20 = 0
y20 = step * 1
v_y20 = 0

x30 = step * 4
v_x30 = 0
y30 = step * 2
v_y30 = 0

x40 = step * 5
v_x40 = 0
y40 = step * 3
v_y40 = 0

x50 = step * 6
v_x50 = 0
y50 = step * 2
v_y50 = 0

x60 = step * 7
v_x60 = 0
y60 = step * 1
v_y60 = 0

x70 = step * 3
v_x70 = 0
y70 = -step * 1
v_y70 = 0

x80 = step * 4
v_x80 = 0 
y80 = -step * 2
v_y80 = 0

x90 = step * 5
v_x90 = 0
y90 = -step * 3
v_y90 = 0

x100 = step * 6
v_x100 = 0
y100 = -step * 2
v_y100 = 0

x110 = step * 7
v_x110 = 0
y110 = -step * 1
v_y110 =0

s0 = (
      x10, v_x10, y10, v_y10,
      x20, v_x20, y20, v_y20,
      x30, v_x30, y30, v_y30,
      x40, v_x40, y40, v_y40,
      x50, v_x50, y50, v_y50,
      x60, v_x60, y60, v_y60,
      x70, v_x70, y70, v_y70,
      x80, v_x80, y80, v_y80,
      x90, v_x90, y90, v_y90,
      x100, v_x100, y100, v_y100,
      x110, v_x110, y110, v_y110     
      )

m1 = 5.97* 10**(24) 

m2 = 7.35 * 10**(22) 

m3 = 7.35 * 10**(22)

m4 = 7.35 * 10**(22)

m5 = 7.35 * 10**(22)
 
m6 = 7.35 * 10**(22)

m7 = 7.35 * 10**(22)

m8 = 7.35 * 10**(22)

m9 = 7.35 * 10**(22)

m10 = 7.35 * 10**(22)

m11 = 7.35 * 10**(22)

G = 6.67 * 10**(-11)

# solving a system of dif equations

sol = odeint(danya_gravition_func, s0, t)

# building a solution as a graph and animating it

fig = plt.figure()
bodys = []

for i in range(0, len(t), 1):
    # body1, = plt.plot(sol[:i, 0], sol[:i, 2], '-', color='darkorange')
    body1_line, = plt.plot(sol[i, 0], sol[i, 2], 'o', color='darkorange', ms=50)
    
    # body2, = plt.plot(sol[:i, 4], sol[:i, 6], '-', color='navy')
    body2_line, = plt.plot(sol[i, 4], sol[i, 6], 'o', color='navy', ms=5)
    
    # body3, = plt.plot(sol[:i, 8], sol[:i, 10], '-', color='navy')
    body3_line, = plt.plot(sol[i, 8], sol[i, 10], 'o', color='navy', ms=5)
    
    # body4, = plt.plot(sol[:i, 12], sol[:i, 14], '-', color='navy')
    body4_line, = plt.plot(sol[i, 12], sol[i, 14], 'o', color='navy', ms=5)
    
    # body5, = plt.plot(sol[:i, 16], sol[:i, 18], '-', color='navy')
    body5_line, = plt.plot(sol[i, 16], sol[i, 18], 'o', color='navy', ms=5)
    
    # body6, = plt.plot(sol[:i, 20], sol[:i, 22], '-', color='navy')
    body6_line, = plt.plot(sol[i, 20], sol[i, 22], 'o', color='navy', ms=5)
    
    # body7, = plt.plot(sol[:i, 24], sol[:i, 26], '-', color='navy')
    body7_line, = plt.plot(sol[i, 24], sol[i, 26], 'o', color='navy', ms=5)
   
    # body8, = plt.plot(sol[:i, 28], sol[:i, 30], '-', color='navy')
    body8_line, = plt.plot(sol[i, 28], sol[i, 30], 'o', color='navy', ms=5)
    
    # body9, = plt.plot(sol[:i, 32], sol[:i, 34], '-', color='navy')
    body9_line, = plt.plot(sol[i, 32], sol[i, 34], 'o', color='navy', ms=5)
    
    # body10, = plt.plot(sol[:i, 36], sol[:i, 38], '-', color='navy')
    body10_line, = plt.plot(sol[i, 36], sol[i, 38], 'o', color='navy', ms=5)
    
    # body11, = plt.plot(sol[:i, 40], sol[:i, 42], '-', color='navy')
    body11_line, = plt.plot(sol[i, 40], sol[i, 42], 'o', color='navy', ms=5)
    
    # bodys.append([
    #               body1, 
    #               body1_line, 
    #               body2, 
    #               body2_line, 
    #               body3, 
    #               body3_line,
    #               body4,
    #               body4_line,
    #               body5,
    #               body5_line,
    #               body6,
    #               body6_line,
    #               body7,
    #               body7_line,
    #               body8,
    #               body8_line,
    #               body9,
    #               body9_line,
    #               body10,
    #               body10_line,
    #               body11,
    #               body11_line
                  
    #               ])
    
    bodys.append([
                  body1_line, 
                  
                  body2_line, 
                 
                  body3_line,
               
                  body4_line,
                 
                  body5_line,
                  
                  body6_line,
                 
                  body7_line,
                 
                  body8_line,
                 
                  body9_line,
                
                  body10_line,
                  
                  body11_line
                  ])
ani = ArtistAnimation(fig, bodys, interval=50)
plt.axis('equal')
ani.save('accretion_new_2.gif')