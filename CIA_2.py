import numpy as np
import matplotlib.pyplot as plt
import random

x=[]
y=[]
n=1000
for i in range (n):          
    x.append(random.randint(0,100))
    y.append(random.randint(0,100))
#%%
#2.0    
x_mean = np.mean(x)
y_mean = np.mean(y)
n = len(x)
numerator = 0
denominator = 0
for i in range(n):
    numerator += (x[i] - x_mean) * (y[i] - y_mean)
    denominator += (x[i] - x_mean) ** 2
    
b1 = numerator / denominator
b0 = y_mean - (b1 * x_mean)
print("Slope1 : ",b1 )
print("Intercept1 : " ,b0)
    

x_max = np.max(x) + 100
x_min = np.min(x) - 100
x = np.linspace(x_min, x_max, 1000)
y = b0 + b1 * x
plt.plot(x, y, color='green', label='Linear Regression')
plt.scatter(x, y, color='red', label='Data Point')
plt.xlabel('Head Size (cm^3)')
plt.ylabel('Brain Weight (grams)')
plt.legend()
plt.show()
#%%
#GRADIENT DESCENT
m = 0
c = 0

L = 0.00001 
epochs = 10000  

n = float(len(x)) 

# Performing Gradient Descent 
for i in range(epochs): 
    Y_pred = m*x + c  
    D_m = (-2/n) * sum(x * (y - Y_pred)) 
    D_c = (-2/n) * sum(y - Y_pred) 
    m = m - L * D_m  # Update m
    c = c - L * D_c  # Update c
Y_pred = m*x + c   
print ("Slope2 : ",m)
print("Intercept2 : ",c)
#%%
#SKLEARN
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
X = np.array(x).reshape(-1, 1)

y = np.array(y).reshape(-1, 1)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print("Slope3 : ", regressor.coef_)
print("Intercept3 : ",regressor.intercept_)

