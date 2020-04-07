

import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt

def calculate_concentrations(initial_concentrations, t0, k1, k_1, k2):
    ce0, cs0, ces0, cp0 = initial_concentrations
    r1 = k1*ce0*cs0
    r_1 = k_1*ces0
    r2 = k2*ces0
    cet = r2 + r_1 - r1
    cst = r_1 - r1
    cest = r1 - r2
    cpt = r2
    return cet, cst, cest, cpt

k1 = 0.01
k_1 = 0.001
k2 = 5

ce0 = 10
cs0 = 1000
ces0 = 0
cp0 = 0

t = np.arange(60)
c_t = integrate.odeint(calculate_concentrations, [ce0, cs0, ces0, cp0], t, args=(k1, k_1, k2))

substances = ["E", "S", "ES", "P"]
f, ax = plt.subplots()
for i in range(4):
    ax.plot(t, c_t[:, i], label=substances[i])
ax.legend()





