import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

### 3D
fig = plt.figure()

# 用matplotlib.pyplot 自带的3d功能， projection='3d'
ax = fig.add_subplot(111, projection='3d')

# 画点
# ax.scatter([1, 2], [2, 3], [3, 4], marker='x')

# 画直线
# ax.plot([1,2,3], [2,3,4], [3,4,6])

# 画曲线
"""
r = 2
thera = np.linspace(0, 6 * np.pi, num=100)
zz = np.linspace(0, 3, num=100)
xx = r * np.cos(thera)
yy = r * np.sin(thera)
# zz = thera * 0

# ax.scatter(xx, yy, zz)
ax.plot(xx, yy, zz)
"""

# 画等高线
"""
num_list = np.linspace(-10, 10, num=50)
xx, yy = np.meshgrid(num_list, num_list)
zz = xx ** 2 + yy ** 2

ax.contour(xx, yy, zz)
"""

"""
# 画曲面
# plot_wireframe
# plot_surface
# 属性： rstride和cstride 表示网格大小
# 属性 cmap表示曲面染色方法 如：plt.cm.hot/plt.cm.cool
num_list = np.linspace(-5, 5, num=50)
xx, yy = np.meshgrid(num_list, num_list)
# zz = xx ** 2 + yy ** 2
zz = (1-xx /2+xx ** 5 + yy ** 3) * np.exp(-xx ** 2 - yy **2)
# ax.plot_wireframe(xx, yy, zz)
ax.plot_surface(xx, yy, zz, cmap='cool')
"""






plt.show()
