
import numpy
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plot
fig = plot.figure()

alpha = numpy.linspace(1, 8, 4)#alpha의 시작값1, 끝값 8 그래프 4개
t = numpy.linspace(0, 2, 7)# T의 시작값 0, 끝값 2, 그래프 7
T, A = numpy.meshgrid(t, alpha)
data = numpy.exp(-T * (1.6 / A))#exp 자연상수의 제곱 값

fig = plot.figure()
ax = fig.gca(projection  = '3d')#플로팅 할려는 좌표를 3D로 지정

Xi = T.flatten()
Yi = A.flatten()
Zi = numpy.zeros(data.size)#numpy.zeros() 해당 배열에 모두 0을 집어넣음

dx =.25 * numpy.ones(data.size)#numpy.ones()해당 배열에 모두 1을 집어넣음
dy =.25 * numpy.ones(data.size)
dz = data.flatten()

ax.set_xlabel('T')
ax.set_ylabel('Alpha')
ax.bar3d(Xi, Yi, Zi, dx, dy, dz, color = 'w')
plot.show()
