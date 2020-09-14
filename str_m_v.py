import numpy as np
import matplotlib.pyplot as plt

G = 6.672 * 10**-11

# _________________________str_m____________________________

def timeobserver (to,n,Msun):
    
    """
        grafik vremeni cotoroe proslo u observera v dali ot central graviti body
        
    """
    
    x = np.linspace(0, 2*Msun, n)

    
    y = np.ones(n) * to
    
    plt.xlabel("coord - m")
    plt.ylabel("coord - t")
    plt.grid()
        
    plt.plot(x, y, color= "navy")

def timerocetg (to,n,c,r,Msun):
    
    """
        grafik vremeni  u rocet v blizi central graviti body
        
    """
    
    x = np.linspace(0, 4*Msun, n)
    
    y = np.ones(n) * to *(1 - (2*G*x) / (r * c**2))**0.5
         
    plt.xlabel("coord - t")
    plt.ylabel("coord - m")
    plt.title("time(mass)")
    plt.grid()
        
    plt.plot(x,y,color= "magenta")
    plt.show()
    
    print("_________________ptimer_s dannoi_massoi_i_rastoyaniem____________")
    print("time u zemlznina = ", to, "rasstoyanie do central graviti body = ", r )
    print("time u rocket =  ", to *(1 - (2*G*Msun) / (r * c**2))**0.5 )
        
   
timeobserver( 100,# time kotoroe proshlo u observera
        100, #col-vo tochek
        2*10**30 # mass sun
         )
    
timerocetg( 100,# time kotoroe proshlo u observera
        100, #col-vo tochek
         3*10**8, # ckorost light
         400*10**6, # rasstoyanie do central graviti body
         2*10**30 # mass sun
         )

plt.show()
# _________________________str_v____________________________

def timeobserver (to,n):
    
    """
        grafik vremeni cotoroe proslo u observera so sokorostu v=0
        
    """
    
    x = np.linspace(0, 3*10**8, n)

    
    y = np.ones(n) * to
    
    plt.xlabel("coord - v")
    plt.ylabel("coord - t")
    plt.grid()
        
    plt.plot(x, y, color= "navy")

def timerocetv (to,n,c,v,tz):
    
    """
        grafik vremeni cotoroe proslo u rocet so sokorostu v
        
    """
    
    x = np.linspace(0, 3*10**8, n)
    
    y = np.ones(n) * to / (1-(x**2)/(c**2))**0.5
         
    plt.xlabel("coord - t")
    plt.ylabel("coord - v")
    plt.title("time(speed)")
    plt.grid()
        
    plt.plot(x,y,color= "magenta")
    plt.show()
    
    if v == c:
        print("_________________ptimer_s dannoi_speed_____________")
        print("time u zemlznina = ", tz, "speed roceti = ", v )
        print("time u rocket = infinity " )
    else:
        tr = tz / (1-(v**2)/(c**2))**0.5
        print("_________________ptimer_s dannoi_speed_____________")
        if v > 3*10**8:
            print("pora v durku")
            print("tak kak max speed v ouer galaktika = speed light = 3*10**8 m/c")
        else:
            print("time u zemlznina = ", tz, "speed roceti = ", v )
            print("time u rocket = ", tr )
        
timeobserver( 5,# time kotoroe proshlo u observera
        100 #col-vo tochek
         )
    
timerocetv( 5,# time kotoroe proshlo u observera
        100, #col-vo tochek
         3*10**8, # ckorost light
         3*10**8, # speed rocet
         10 # time zemlyanina
         )

plt.show()