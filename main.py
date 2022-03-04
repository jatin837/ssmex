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

def F(t):
    if t<1:
        return 0
    return 1

t = np.arange(100)
Y = []

X0 = np.array([x0, v0])

for time in t:
    Xdot = np.matmul(A, X0.T) + np.matmul(B, F(time)*np.ones(2).T)
    X0 = X0 + Xdot

    y = np.matmul(np.array([1, 0]), X0.T) 
    Y.append(y)
    print(time, y)

plt.plot(t, Y)
plt.show()
