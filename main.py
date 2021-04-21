import numpy as np

list = [1, 2, 3, 4, 5]
array = np.array(list)

print(2 * list)
print(2 * array)

r = range(5)
print(r)
r2 = np.arange(5)
print(r2)
r3 = np.arange(3, 8, 2)
print(r3)

a = np.array(np.arange(6))
print(a)
a = a.reshape((2, 3))
print(a)

zeros = np.zeros((3, 2))
print(zeros)

ticks = np.linspace(4.0, 11.0, num=8)
print(ticks)

import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')

x = np.arange(6)
y = np.arange(6)
print(x)

fig = plt.figure()
plt.plot(x, y)
plt.xlabel("Time")
plt.title("A plot")
fig.savefig("plot1")

x = np.linspace(0, 2 * np.pi)
y1 = np.cos(x)
y2 = np.sin(x)
y3 = -1 * np.sin(x)
y4 = -1 * np.cos(x)

fig_sine = plt.figure()
plt.plot(x, y1)
plt.plot(x, y2)
plt.plot(x, y3)
plt.plot(x, y4)
fig_sine.savefig("sinecurves")
