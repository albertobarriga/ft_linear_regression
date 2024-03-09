import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (12.0, 9.0)

# Preprocessing Input data
data = pd.read_csv('data.csv')
X = data.iloc[:, 0]
Y = data.iloc[:, 1]
plt.scatter(X, Y)


x_mean = X.mean()
# Normalizing the data
old_X = X
X = X / X.mean()

# Building the model
m = 0
c = 0

L = 0.1  # The learning Rate
epochs = 200  # The number of iterations to perform gradient descent

n = float(len(X)) # Number of elements in X

# Performing Gradient Descent 
for i in range(epochs): 
    Y_pred = m*X + c  # The current predicted value of Y
    D_m = (-2/n) * sum(X * (Y - Y_pred))  # Derivative wrt m
    D_c = (-2/n) * sum(Y - Y_pred)  # Derivative wrt c
    m = m - L * D_m  # Update m
    c = c - L * D_c  # Update c
    
print (m, c)
new_m = m / x_mean

print (new_m, c)
# Plotting the regression line in original scale
plt.plot(old_X, new_m*old_X+c, color='red')
plt.show()
plt.scatter(X, Y)
plt.plot(X, m*X+c, color='green')
plt.show()