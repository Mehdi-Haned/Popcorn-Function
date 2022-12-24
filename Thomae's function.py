
import matplotlib.pyplot as plt
import numpy as np
from fractions import Fraction

x = np.linspace(0 + 0.01, 1 - 0.01, 1000)
y = np.zeros(len(x))

for i in range(len(x)):
    if x[i] != 0:
        y[i] = 1 / (Fraction(abs(x[i])).limit_denominator(50).denominator)

plt.plot(x, y, ".", color = "black", ms = 1)


tick = []

for n in range(2, 13, 2):

    tick.append(1/n)
tick.append(1/3)
tick.append(1/5)

plt.yticks(tick)

plt.show()






