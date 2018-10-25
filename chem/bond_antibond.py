import scipy as np

a = 0.7  # half the distance between atoms

a0 = 0.53  # Bohr radius in Angstrom

x = np.mgrid[-5:5:100j]

sa = np.exp(-np.sqrt((x - a) ** 2 / a0))

sb = np.exp(-np.sqrt((x + a) ** 2 / a0))

import matplotlib.pyplot as plt

plt.subplot(2, 1, 1)

plt.plot(x, sa + sb, '-', label='Bond')

plt.plot(x, sa, '-', label='A')

plt.plot(x, sb, '-', label='B')

plt.legend()

plt.subplot(2, 1, 2)

plt.plot(x, np.absolute(sa - sb), '-', label='Anti-bond')

plt.plot(x, sa, '-', label='A')

plt.plot(x, sb, '-', label='B')

plt.legend()

plt.show()
