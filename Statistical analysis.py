
from scipy.stats import shapiro
import numpy as np
import matplotlib.pyplot as plt

arr_size = 1000
x = np.random.normal(loc=1, scale=2, size=arr_size)
y = np.random.uniform(low=-1, high=1, size=arr_size)
z = np.random.exponential(scale=5, size=arr_size)

print("Means: {} {} {}".format(np.mean(x), np.mean(y), np.mean(z)))
print("Stds: {} {} {}".format(np.std(x), np.std(y), np.std(z)))

_, px = shapiro(x)
_, py = shapiro(y)
_, pz = shapiro(z)

print("p-values: {} {} {}".format(px, py, pz))
# if p value is < 0.05 then it is a normal distribution

f, ax = plt.subplots(3)
ax[0].hist(x, bins=100)
ax[1].hist(y, bins=100)
ax[2].hist(z, bins=100)
plt.show()

#  ======================================== PART 2 =====================
from numpy import loadtxt

phs = loadtxt(r'C:\Users\1\PycharmProjects\Test\UFAZ/pH.txt', delimiter="\n")
print("mean of the file: {}".format(np.mean(phs)))
print("Std of the file: {}".format(np.std(phs)))
print("p-value of the file: {}".format(shapiro(phs)[1]))
plt.hist(phs)

cosmic_particle = loadtxt(r'C:\Users\1\PycharmProjects\Test\UFAZ/cosmicParticle.txt', delimiter="\n")
event_intervals = []
k = 0
for i in cosmic_particle:
    event_intervals.append(i - k)
    k = i
print("mean of the file: {}".format(np.mean(event_intervals)))
print("Std of the file: {}".format(np.std(event_intervals)))
print("p-value of the file: {}".format(shapiro(event_intervals)[1]))
plt.hist(event_intervals, bins=100)

v_wind = loadtxt(r'C:\Users\1\PycharmProjects\Test\UFAZ/wind.txt', delimiter="\n")
print("mean of the file: {}".format(np.mean(v_wind)))
print("Std of the file: {}".format(np.std(v_wind)))
print("p-value of the file: {}".format(shapiro(v_wind)[1]))
plt.hist(v_wind)

rot_angle = loadtxt(r'C:\Users\1\PycharmProjects\Test\UFAZ/spinningTop.txt', delimiter="\n")
print("mean of the file: {}".format(np.mean(rot_angle)))
print("Std of the file: {}".format(np.std(rot_angle)))
print("p-value of the file: {}".format(shapiro(rot_angle)[1]))
plt.hist(rot_angle)




