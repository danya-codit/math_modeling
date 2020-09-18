import numpy as np
import matplotlib.pyplot as plt
import math

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
    tr1 = to *(1 - (2*G*Msun) / (r * c**2))**0.5
    print("_________________ptimer_s dannoi_massoi_i_rastoyaniem____________")
    print("time u zemlznina = ", to, "rasstoyanie do central graviti body = ", r )
    print("time u rocket =  ", tr1 )
        
   
timeobserver( 10,# time kotoroe proshlo u observera
        10, #col-vo tochek
        2*10**30 # mass sun
         )
    
timerocetg( 10,# time kotoroe proshlo u observera
        10, #col-vo tochek
         3*10**8, # ckorost light
         40*10**6, # rasstoyanie do central graviti body
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
        print("_________________ptimer_s dannoi_speed_____________")
        if v > 3*10**8:
            print("pora v durku")
            print("tak kak max speed v ouer galaktika = speed light = 3*10**8 m/c")
        else:
            tr2 = tz / (1-(v**2)/(c**2))**0.5
            print("time u zemlznina = ", tz, "speed roceti = ", v )
            print("time u rocket = ", tr2 )
        
timeobserver( 5,# time kotoroe proshlo u observera
        100 #col-vo tochek
         )
    
timerocetv( 5,# time kotoroe proshlo u observera
        100, #col-vo tochek
         3*10**8, # ckorost light
         2.5*10**8, # speed rocet
         10 # time zemlyanina
         )

def watch(R,
          time, #zemlyanina
          M, #central gravit body
          r, #do central gravit body
          v  #speed rocket
          ):
    fig = plt.figure()
    fig.suptitle('timers', fontsize=15, fontweight='bold')
    
    ax = fig.add_subplot(111)
    fig.subplots_adjust(top=0.85)
    
    
    
    #_________________________cloak_zemlyanina______________________
    
    
    
    
    """
        CLOAK FACE
       
    """
    angle = 60
    for k in range (1, 13):
        plt.axis('equal')
        ax.text( R * 1.3 * math.cos(angle * math.pi / 180) - 0.175, R * 1.3 * math.sin(angle* math.pi / 180) - 0.05, k , fontsize=15, style='italic')
        angle = angle - 30  
        
    """
      CIRCUMFERENCE OF THE CLOCK
      
    """
    x = np.arange(-2,2,0.1)
    y = np.arange(-2,2,0.1)
    X, Y = np.meshgrid(x,y)
    fxy = X**2 + Y**2
    plt.contour(X,Y,fxy, levels=[R])
    plt.axis('equal')
    
    alfa = 0
    
    
    """
        riski seconds
        
    """
    alfa = 0
    for n in range (60):
        
        x = [ (R-0.1) * math.cos(alfa * math.pi / 180) , R * math.cos(alfa * math.pi / 180)]
        y = [ (R-0.1) * math.sin(alfa * math.pi / 180) , R * math.sin(alfa * math.pi / 180)]
        
        alfa = alfa + 6
    
        plt.plot(x, y, color= "navy")
        
        
     
    """
        riski hours
        
    """
    
    alfa = 0
    for n in range (60):
        
        x = [ (R-0.2) * math.cos(alfa * math.pi / 180) , R * math.cos(alfa * math.pi / 180)]
        y = [ (R-0.2) * math.sin(alfa * math.pi / 180) , R * math.sin(alfa * math.pi / 180)]
        
        alfa = alfa + 30
    
        plt.plot(x, y, color= "navy")
        
        
    """
       comversion of secods into hours, minuts, seconds
        
    """
    
    days  =  time // (24*3600)
    hours = time / 3600
    mints = time / 60
    seconds = time 
    print("days = ", days,
          ", hours = ", hours,
          ", mints = ", mints,
          ", seconds = ", seconds
          )
    
    
    """
        seconds hand
        
    """
    
    alfa = 90 - seconds * 6
    
    x = [ 0 , (R - 0.1) * math.cos(alfa * math.pi / 180)]
    y = [ 0 , (R - 0.1) * math.sin(alfa * math.pi / 180)]
        
    
    plt.plot(x, y, color= "deeppink", marker = '.', ms = 3,label='seconds')
    
    
    """
        minuts hand
        
    """
    
    alfa = 90 - mints * 6
    
    x = [ 0 , (R - 0.2) * math.cos(alfa * math.pi / 180)]
    y = [ 0 , (R - 0.2) * math.sin(alfa * math.pi / 180)]
        
    
    plt.plot(x, y, color= "darkblue", marker = '.', ms = 10, label='mints')
    
    
    """
        hours hand
        
    """
    
    alfa = 90 - hours * 30
    
    x = [ 0 , (R - 0.3) * math.cos(alfa * math.pi / 180)]
    y = [ 0 , (R - 0.3) * math.sin(alfa * math.pi / 180)]
        
    
    plt.plot(x, y, color= "r", marker = '.', ms = 15, label='hours')
    
    """ 
        days
        
    """
    ax.text( 0.32, -0.4, days, fontsize=12, style='italic')
    ax.text( -0.5,-0.4, "days:", fontsize=12, style='italic')
    ax.text( -0.9,2, "observer", fontsize=15)
    
    
    
    
    #_________________________cloak_rocket______________________
    
    G = 6.672 * 10**-11
    c = 2.998*10**8
    
    tr1 = time *(1 - (2*G*M) / (r * c**2))**0.5
    tr2 = time / (1-(v**2)/(c**2))**0.5
    
    timer = (tr1 + tr2) / 2
    """
        CLOAK FACE
       
    """
    angle = 60
    for k in range (1, 13):
        plt.axis('equal')
        ax.text( R * 1.3 * math.cos(angle * math.pi / 180) - 0.175 + 5, R * 1.3 * math.sin(angle* math.pi / 180) - 0.05, k , fontsize=15, style='italic')
        angle = angle - 30  
        
    """
      CIRCUMFERENCE OF THE CLOCK
      
    """
    x = np.arange(3,7,0.1) 
    y = np.arange(-2,2,0.1)
    X, Y = np.meshgrid(x,y)
    fxy = (X-5)**2 + Y**2
    plt.contour(X,Y,fxy, levels=[R])
    plt.axis('equal')
    
    """
        riski seconds
        
    """
    alfa = 0
    for n in range (60):
        
        x = [ (R-0.1) * math.cos(alfa * math.pi / 180) + 5 , R * math.cos(alfa * math.pi / 180) + 5]
        y = [ (R-0.1) * math.sin(alfa * math.pi / 180) , R * math.sin(alfa * math.pi / 180)]
        
        alfa = alfa + 6
    
        plt.plot(x, y, color= "navy")
        
        
     
    """
        riski hours
        
    """
    
    alfa = 0
    for n in range (60):
        
        x = [ (R-0.2) * math.cos(alfa * math.pi / 180) + 5, R * math.cos(alfa * math.pi / 180) + 5]
        y = [ (R-0.2) * math.sin(alfa * math.pi / 180) , R * math.sin(alfa * math.pi / 180)]
        
        alfa = alfa + 30
    
        plt.plot(x, y, color= "navy")
        
        
    """
        comversion of secods into hours, minuts, seconds
        
    """
    
    days  = timer // (24*3600)
    hours = timer / 3600
    mints = timer / 60
    seconds = timer 
    print("days = ", days,
          ", hours = ", hours,
          ", mints = ", mints,
          ", seconds = ", seconds
          )
    
    
    """
        seconds hand
        
    """
    
    alfa = 90 - seconds * 6
    
    x = [ 0 + 5 , (R - 0.1) * math.cos(alfa * math.pi / 180) + 5]
    y = [ 0 , (R - 0.1) * math.sin(alfa * math.pi / 180)]
        
    
    plt.plot(x, y, color= "deeppink", marker = '.', ms = 3,label='seconds')
    
    
    """
        minuts hand
        
    """
    
    alfa = 90 - mints * 6
    
    x = [ 0 + 5, (R - 0.2) * math.cos(alfa * math.pi / 180) + 5]
    y = [ 0 , (R - 0.2) * math.sin(alfa * math.pi / 180)]
        
    
    plt.plot(x, y, color= "darkblue", marker = '.', ms = 10, label='mints')
    
    
    """
        hours hand
        
    """
    
    alfa = 90 - hours * 30
    
    x = [ 0 + 5 , (R - 0.3) * math.cos(alfa * math.pi / 180) + 5]
    y = [ 0 , (R - 0.3) * math.sin(alfa * math.pi / 180)]
        
    
    plt.plot(x, y, color= "r", marker = '.', ms = 15, label='hours')
    
    """ 
        days
        
    """
    ax.text( 0.32 + 5, -0.4, days, fontsize=12, style='italic')
    ax.text( -0.5 + 5,-0.4, "days:", fontsize=12, style='italic')
    ax.text( -0.65 + 5,2, "rocket", fontsize=15)
      
watch(1,# radius wathch
      3600,# time zemlyanina
      2*10**30,#mass central gravit body
      1.469*10**11,# rasstoyanie do central gravit body
      2.5*10**8# speed rocket
      )

plt.show()