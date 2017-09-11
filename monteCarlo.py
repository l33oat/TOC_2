import random
import numpy as np
import matplotlib.pyplot as plt
TIMES_TO_REPEAT = 10**6
LENGTH = 2
CENTER = [0,0]
xg=[] #difine array to keep point that in circle
yg=[]
xng=[]#difine array to keep point that not in circle
yng=[]

def in_circle(point):
    x = point[0]
    y = point[1]
    center_x = CENTER[0]
    center_y = CENTER[1]
    radius = LENGTH/2
    return (x - center_x)**2 + (y - center_y)**2 < radius**2 #check point that been random are in circle
def notIn_circle(point):
    x = point[0]
    y = point[1]
    center_x = CENTER[0]
    center_y = CENTER[1]
    radius = LENGTH/2
    return (x - center_x)**2 + (y - center_y)**2 >= radius**2#check point that been random are not in circle
count = inside_count = 0
for i in range(TIMES_TO_REPEAT):
    point = random.uniform(0,1),random.uniform(1,0) #random point in Q1
    if in_circle(point):
        inside_count += 1
        xg.append(point[0]) #keep point in array to plot graph
        yg.append(point[1])
    elif notIn_circle(point):
        xng.append(point[0])#keep point in array to plot graph
        yng.append(point[1])
    count += 1

pi = (inside_count / count) * 4
print(pi)
plt.scatter(xg,yg,color="g") #orginal plot graph in dot with green (in circle)
plt.plot(xng,yng,'.',color="r")#define to plot graph in dot with red (not in circle)
plt.show()#to show graph that has been plot