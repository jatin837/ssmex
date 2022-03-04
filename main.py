import numpy as np
import matplotlib.pyplot as plt

m = 2  ## [kg]
c = 1  ## [Ns/m]
k = 2  ## [N/m]
x0 = 0  ## [m]
v0 = 0  ## [m/s]

A = np.array([[0, 1],
          [-k/m, -c/m]])
B = np.array([0,1/m])
C = np.array([1, 0])
D = 0

F = 1

t = np.array(range(100))
Y = []
for time in t:
    X0 = np.array([x0, v0])
    X = np.matmul(A, X0.T) + np.dot(B, F*np.ones(2).T)
    x0, v0 = X

    y = np.matmul(np.array([1, 0]), X.T) 
    Y.append(y)
    print(X, y)

plt.plot(t, Y)
plt.show()
