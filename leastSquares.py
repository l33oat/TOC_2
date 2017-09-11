import numpy as np
from numpy import genfromtxt
my_data = genfromtxt('LS.csv',delimiter=',', names=True)#import data from csv file
x = np.array(my_data['X'])#keep X column data in to array
y = np.array(my_data['Y'])#keep Y column data in to array
z = np.polyfit(x, y, 1) #change data in to array
p = np.poly1d(z)#change data into equation
print (my_data['X'])
#plotting
import matplotlib.pyplot as plt
xp = np.linspace(-1, 25, 100)#build line start from -1 to 25
plt.plot(x, y, '.', xp, p(xp)) 
plt.show()#show graph
