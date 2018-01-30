import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 窗口
# 背景色
# plt.subplot(facecolor='black')


# 直线样式属性
# 可以查看函数说明
# linestyle 线段样式
# linewidth 粗细
# marker 点样式
# markersize 点样式大小
# color 颜色
xx = [1,2,3,4]
yy = [2,2,5,3]

# plt.plot(xx, yy, linestyle='-.', color='y', marker='d', markersize=20)

# 点样式属性
# 颜色 c/color
# 样式marker
# 大小s
# 透明度 alpha

# 生成正态分布点
# loc 对应整个分布的中心
# scale 次概率分布的标准差   对应于分布的宽度,值越大越矮胖 越小越瘦高
# size 数量
"""
num = 200
xx = np.random.normal(loc=0, scale=1, size=num)
yy = np.random.normal(loc=0, scale=1, size=num)

colors = np.random.rand(num * 3).reshape(num, 3)
sizes = np.random.randint(3, 40, size=num)

# plt.scatter(xx, yy, marker='x', c=colors, s=sizes)
plt.scatter(xx, yy, marker='>', c=colors, s=sizes)
# plt.scatter(xx, yy, marker='d', c=colors, s=sizes)
"""

### 文字
"""
text = plt.text(x=0.5,
                y=0.5,
                s='English中文'
    
)
"""

# 给每个点加上坐标注释
"""
xx = np.random.randint(0, 100, size=30)
yy = np.random.randint(0, 100, size=30)
plt.scatter(xx, yy)

for x, y in zip(xx, yy):
    plt.text(x, y, '[%d, %d]' % (x, y))
"""


# 箭头
# 函数annotate
"""
plt.scatter(10, 10)
plt.annotate('this is a point', xy=(10,10), xytext=(30, 30),
             textcoords='offset points',
             arrowprops=dict(arrowstyle="->"))

"""

# 等高线 contour contourf
# 画圆
# 生成网格 meshgrid(x, y) 网格越密,图形越平滑
num = np.linspace(-5, 5, 20)
x, y = np.meshgrid(num, num)
# plt.scatter(x, y)
# plt.plot(x, y)
# plt.plot(y, x)

# contour 会在网格线上找到符合计算的点,即每个点至少落在一条网格线上，然后用线连起来

# plt.contour(x, y, x ** 2 + y ** 2, [4,9])

# 不规则登高线(1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x **2 - y ** 2)

# plt.contour(x, y, (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x **2 - y ** 2))
plt.contourf(x, y, (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x **2 - y ** 2))





plt.show()



