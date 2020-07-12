import matplotlib.pyplot as plt
import numpy as np
# from scipy.interpolate import interp1d

n_observations = 10
jitter_x = 4
jitter_y = 30

r = 10
x = np.linspace(-r, r, n_observations) + np.random.rand(n_observations)*jitter_x - jitter_x/2
y = ((x)**2)+20 + np.random.rand(n_observations)*jitter_y - jitter_y/2
# y = [37.03706428, 34.88925027, 29.39072556, 24.46739443, 12.1051254,  21.42073355, 18.20683003, 20.74063966, 38.88716749, 42.14923628,]
# y = (.8*x+5) * np.random.rand(n_observations)*jitter_y - jitter_y/2
poly = np.poly1d(np.polyfit(x, y, n_observations-1))
parabola = np.poly1d(np.polyfit(x, y, 2))
poly_x = np.linspace(x[0], x[-1], n_observations*20)

plt.scatter(x, y, marker='+', s=60, zorder=3, c='#3969b1', linewidths=4)

plt.plot(poly_x, poly(poly_x), zorder = 2, c='#da7c30', linewidth=1.5, solid_capstyle='round')
plt.plot(poly_x, parabola(poly_x), c='#3e9651', zorder=2, linewidth=3.5, solid_capstyle='round')

#plt.ylim(0, 60)
#plt.xlim(x[0]-1, x[-1]+1)

# plt.gca().set_yticklabels([])
# plt.gca().set_xticklabels([])

plt.show()
# plt.savefig('overfitting.png', dpi=300, bbox_inches='tight')