from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.view_init(30,120)
e = np.e

r = 1
step = .025
stept = .5
X = np.arange(-r, r, step)
Y = np.arange(-r, r, step)
X, Y = np.meshgrid(X, Y)

# Z = (X**2 - Y**2)/5 #\frac{X^2 - Y^2}{5} (pringle)
# Z = -(2*X*e**(-(X**2+Y**2)/5))/5 # Ableitung von: np.e**(-1*(X**2+Y**2)/5) (gauss)
# Z = (20 - Y)**(5/4) + 10*(X - Y**2)**2
Z = X**2 + Y**2

# Plot the surface.
surf = ax.plot_surface(X, Y, Z, cmap=cm.coolwarm,
                       linewidth=0.2, antialiased=True)

# plt.xticks(np.arange(-r/2, r*1.5, stept))
# plt.yticks(np.arange(-r, r, stept))
plt.xlabel('m')
plt.ylabel('t')
ax.tick_params(labelbottom=False, labelleft=False)
# plt.show()
plt.savefig('3d.png', bbox_inches='tight', dpi=300)