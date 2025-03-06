import numpy as np
import matplotlib.pyplot as plt

# t can be: a number, a numpy array, f is a function
def get_coords(t, f):
    return t, f(t)
def euler(t, f_0, df): # df is a function so that df(1) = grad at t=1
    # f_1 = f_0 + dt*df(t_(k-1))
    # keep on finding f_2, f_3... until f_n.
    dt = t[1]-t[0]
    f = t*0
    f[0] = f_0
    for k in range(len(t)-1):
        f[k+1] = f[k] + dt * df(f[k], t[k])
    return t, f
def midpoint(t, f_0, df):
    dt = abs(t[1]-t[0])
    f = t*0
    f[0] = f_0
    #f[k] + dt * df(f_0, t_0 + 0.5*dt)
    for k in range(len(t)-1):
        # f[k+1] = f[k] + dt * df(f[k], t[k])
        f[k+1] = f[k] + dt * df(f[k], t[k] + 0.5*dt)
    return t, f
def Runge_Kunta():
    pass

# Population for ONE species
t = np.linspace(0, 4000, 4001)
P0 = 1
dP = lambda P, t : 0.1 * P * (1-P/100) * np.sin(t/100)
plt.plot(*euler(t, P0, dP), '-')
plt.plot(*midpoint(t, P0, dP), '--')
plt.plot(t, np.sin(t/100)*10++10)
plt.show()

# Population for TWO species
t = np.linspace(0, 100, 1001)
A_0 = 100 # Prey
B_0 = 100 # Predator
dX = lambda X, t : 0.05 * np.array((2*X[0]-4*X[1], -1*X[1]+2*X[0]))
# X = np.zeros((len(t), 2))
X_0 = [A_0, B_0]
_, X = euler(np.repeat(t, 2).reshape(len(t), 2), X_0, dX)
print(X)
plt.plot(t, X[:, 0])
plt.plot(t, X[:, 1])
plt.show()