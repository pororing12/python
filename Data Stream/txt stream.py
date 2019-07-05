import numpy
import matplotlib.pyplot as plot

data = numpy.loadtxt('good.txt')

plot.plot(data.T[0], data.T[1])
plot.plot(data.T[0], data.T[2])

plot.show()