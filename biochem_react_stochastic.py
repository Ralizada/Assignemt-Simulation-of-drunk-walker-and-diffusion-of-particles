import numpy as np
import matplotlib.pyplot as plt
from numpy.random import choice


# 1) E + S => ES
# 2) ES => E + S
# 3) ES => E + P

# reaction rates
k1 = 0.01
k2 = 0.001
k3 = 5

# number of timestamps
N = 60

# array to collect all 100 runs
values_total = np.zeros([N+1, 4, 100])

for i in range(100):
    # initial populations of molecules
    E = 5
    S = 50
    ES = 0
    P = 0

    # lists to collect all the values over time interval
    E_values = [E]
    S_values = [S]
    ES_values = [ES]
    P_values = [P]

    for t in range(N):

        # probabilities of the reactions
        p1 = k1*E*S
        p2 = k2*ES
        p3 = k3*ES

        # get two random numbers
        random_choice = choice([1, 2, 3], 1, p=[p1/sum([p1, p2, p3]), p2/sum([p1, p2, p3]), p3/sum([p1, p2, p3])])

        if random_choice == 1:
            E -= 1
            S -= 1
            ES += 1
        elif random_choice == 2:
            ES -= 1
            E += 1
            S += 1
        elif random_choice == 3:
            ES -= 1
            E += 1
            P += 1
        E_values.append(E)
        S_values.append(S)
        ES_values.append(ES)
        P_values.append(P)
    values_total[:, 0, i] = E_values
    values_total[:, 1, i] = S_values
    values_total[:, 2, i] = ES_values
    values_total[:, 3, i] = P_values

substances = ["E", "S", "ES", "P"]
ts = np.arange(N+1)
c_t = [values_total[:, 0, :].mean(axis=1), values_total[:, 1, :].mean(axis=1),
       values_total[:, 2, :].mean(axis=1), values_total[:, 3, :].mean(axis=1)]


f, ax = plt.subplots()
for i in range(4):
    ax.plot(ts, c_t[i], label=substances[i])
ax.legend()

# a = np.interp(ts, ts, values_total[:, 0, :])

