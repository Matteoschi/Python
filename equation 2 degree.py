from math import sqrt
import numpy as np 
import matplotlib.pyplot as plt
import time
a=float(input("inserisci coefficente a "))
b=float(input("inserisci coefficente b "))
c=float(input("inserisci termine noto "))
class assi_cartesiani():
    plt.xlim(-50,50)        #indicate the space of the plan (X)
    plt.ylim(-50,50)        #indicate the space of the plan (y)

    ascissa_x1=0        #create abscissa axis
    ascissa_y1=-50
    ascissa_x2=0
    ascissa_y2=50
    plt.plot([ascissa_x1,ascissa_x2],[ascissa_y1,ascissa_y2],color="black")     #draw the axis

    ascissa_x1=-50      #create ordinate axis
    ascissa_y1=0
    ascissa_x2=50
    ascissa_y2=0
    plt.plot([ascissa_x1,ascissa_x2],[ascissa_y1,ascissa_y2],color="black")     #draw the axis
class equazione_2_grado():
    try:
        if a !=0:
            try:
                delta=(sqrt((b*b-4*a*c)))
                risultato1=(-b+delta)/(a*2)
                risultato2=(-b-delta)/(a*2)
                print("x1=",risultato2,"x2=",risultato1)
                class grafico_funzione():
                    def f(x):       
                        return a*x*x+b*x+c   

                    x=np.arange(-50,50)     #dominio
                    plt.plot(x, f(x),color="red")       
                    plt.show()
            except:
                print("radice negativa")
                time.sleep(10)
        else:
            risultato=(-c/b)
            print(risultato)
    except:
        print("cosa stai facendo?")


