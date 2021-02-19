import numpy as np
import matplotlib.pyplot as plt

def poissonpmf(mu,x):
    return (np.exp(-mu) * (mu**x) / np.math.factorial(x))

param=4
size=500
data=np.random.poisson(param, size)
mu=data.mean()
X = np.unique(data)
pi=np.array([poissonpmf(mu,xi) for xi in X])
plt.hist(data)
plt.plot(X,size*pi)