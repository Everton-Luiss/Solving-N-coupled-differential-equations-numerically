import numpy as np
import matplotlib.pyplot as plt
import sys

x1, y1 = np.loadtxt("numerico.dat",unpack=True)
x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
#x2, y2 = np.loadtxt("pvariancia1.dat",unpack=True)

#x3, y3 = np.loadtxt("kurtosis2.dat",unpack=True)
#x4, y4 = np.loadtxt("pvariancia2.dat",unpack=True)

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=False)
ax1.plot(x1, y1)#, x3, y3)
ax1.legend(('Resultado numérico', 'Masked if > 0.5'),
           loc='upper right')
ax1.set_title('Resultado numérico', color='orange')

ax2.plot(x, x**3)#, label='cubic')
ax2.legend(('No mask', 'Masked if > 0.5'),
           loc='upper right')
ax2.set_title('variance')

#plt.plot(x, x**3, label='cubic')



plt.xlabel('t')
#t = plt.xlabel('t', fontsize=14, color='red')


#ax1.set_title('style:'.format(sty), color='C0')
fig.suptitle('Regime flutuativo')

plt.show()
