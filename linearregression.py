import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 
data=pd.read_csv("mycsv.csv") #importing my csv file
data.head()
#collecting values of x and y from csv file
x=data["Speed"].values
y=data["Distance"].values
#calculating mean
mean_x=np.mean(x)
mean_y=np.mean(y)
#total no. of values
n=len(x)
#calculating the value of m and c for equation
a=0
b=0
for i in range(n):
	a+=(x[i]-mean_x)*(y[i]-mean_y)
	b+=(x[i]-mean_x)**2
	m=a/b
	c=(mean_y)-(m*mean_x)
    #plotting values
	max_x=np.max(x)+4
	min_x=np.min(x)-4
    #collecting line values of x and y
	x=np.linspace(min_x,max_x,10)
	y=c+(m*x)
    #plotting line
	plt.plot(x,y,color='red',label='Regression line')
    #plotting scatter plot
	plt.scatter(x,y,color='green',label='Scatter plot')
	plt.xlabel('Speed')
	plt.ylabel('Distance')
	plt.legend()
	plt.show()
