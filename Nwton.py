import decimal
import matplotlib.pyplot as plt
xg=[] #define variable for plot graph
yg=[]
def func(x):
	return x**2-13		#function for find root 13

def derivFunc(x):		#Derivative of the above function
	return 2*x

def newtonRaphson(x):	#function to find the root
	h = d(func(x) / derivFunc(x))
	count=0
	while(abs(h) > 0.00000000000001):	#While h is greater than allowed error ε
		
		h = d(func(x) / derivFunc(x))

		# x(i+1) = x(i) - f(x) / f'(x)	#Newton Raphson method, formula
		x = d(x) - d(h)
		count=count+1
		xg.append(count) #put count into array
		yg.append(x) #put x in array
		print("x =", x, ",error =", abs(h))
	return x

d = decimal.Decimal 
x0 = 1.0					#initial guess x0 = 1.0
xFound = newtonRaphson(x0)	# NewtonRaphson Method#plt.plot(xg,count)
print("\nAnswer is:", d(xFound))
plt.plot(xg,yg)	#input data in graph
plt.show()#show graph