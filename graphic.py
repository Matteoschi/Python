from turtle import color
import numpy as np 
import matplotlib.pyplot as plt

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


def f(x):       
    return x**2      #choose a function to graph

x=np.arange(-50,50)     #indicate that the x can vary from -50 to 150 (domain)
plt.plot(x, f(x),color="red")       #draw the graph
plt.show()      #Finally I visualize the graphical representation with the function plt.show ()