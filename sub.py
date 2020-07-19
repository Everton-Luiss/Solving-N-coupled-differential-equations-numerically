import numpy as np
import matplotlib.pyplot as plt
import sys

x1, y1 = np.loadtxt("numerico.dat",unpack=True)
#x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
x = np.linspace(0, 30, 256, endpoint=True)

fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1, sharex=True, sharey=False)
ax1.plot(x1, y1, x, 2.*np.cos(0.2**(1/2)*x))
ax1.legend(('Numérico', 'Analítico'),
           loc='upper right')
ax1.set_title('Resultado numérico', color='orange')

#ax2.plot(x, 2.*np.cos(0.2**(1/2)*x))#, label='cubic')
#ax2.legend(('No mask', 'Masked if > 0.5'),
         #  loc='upper right')
#ax2.set_title('Resultado analítico')


plt.xlabel('t')

fig.suptitle('Regime flutuativo')

plt.show()
