'''
import math
import matplotlib.pyplot as plot

T = range(100)
X = [(6 * math.pi * t) / len(T) for t in T]
Y = [math.sin(value) for value in X]

plot.plot(X, Y)
plot.show()
'''
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

'''
import numpy
import matplotlib.pyplot as plot

X = numpy.linspace(-3, 2, 200)
Y = X **2 - 2 * X + 1

plot.plot(X, Y)
plot.show()
'''

import matplotlib.pyplot as plt
import numpy

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasAgg

fig = plt.figure()
'''
data = np.loadtxt('good.txt')

plt.plot(data[: , 0], data[:, 0])
plt.plot(data[:, 0], data[:, 1])
plt.plot(data[:, 0], data[:, 2])

for column in data.T :
    plt.plot(data[:, 0], column)
plt.show()
'''

label_list = (
    b'Iris-setosa',
    b'Iris-versicolor',
    b'Iris-virginica',
)

def read_label(label) :
    return label_list.index(label)

data = numpy.loadtxt('good.txt', delimiter = ',', converters = { 4 : read_label})

color_set = ('.00', '.50','.25')
color_list = [color_set[int(label)] for label in data[:, 4]]

plt.scatter(data[:, 0], data[:, 1], color = color_list)
plt.xlabel('X')
plt.ylabelI('Y')
plt.show()


window = tk.Tk()
canvas = FigureCanvasTkAgg(fig, master = window)
canvas._tkcanvas.pack(side = tk.TOP, fill = tk.BOTH, expand = 1)
window.mainloop()