import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# 点

"""
xx = [1, 2, 3]
yy = [1, 3, 2]
plt.scatter(xx, yy)

"""

### 线
# 直线


# 多段线


# 曲线
xx = np.linspace(0, 2 * np.pi, num=30)
yy = np.sin(xx)
# plt.scatter(xx, yy)
# plt.plot(xx, yy)


### 添加网格： grid
### 网格属性：color, linestyle linewidth
# plt.grid(color='red', linestyle='--', linewidth=3)


### 画圆
# 利用公式 y = (r ** 2 - x ** 2) ** 0.5
"""
r = 2
xx = np.linspace(-2, 2, num=30)
yy = (r ** 2 - xx ** 2) ** 0.5
plt.plot(xx, yy)
plt.plot(xx, -yy)
"""

# 利用公式 x = r * np.cos(theta) , y = r * np.sin(theta)
r = 2
theta = np.linspace(0, 2 * np.pi, num=50)
xx = r * np.cos(theta)
yy = r * np.sin(theta)
# plt.plot(xx, yy)


### 子图
# subplot(x, y, z)意思是将整个figure分成x行, y列
# 然后将这个图放在第z个格子里
# 也可以直接subplot(xyz)
# plt.subplot()

# 直接使用
"""
plt.subplot(221)
plt.plot(xx, yy)

plt.subplot(224)
plt.plot(xx, yy)
"""

# 指定使用
"""
sub1 = plt.subplot(221)
sub1 = plt.plot(xx, yy)

sub2 = plt.subplot(224)
sub2 = plt.plot(xx, yy)
"""

### 多窗口
"""
fig1 = plt.figure()
sub1 = fig1.add_subplot(111)
sub1.plot(xx, yy)

fig2 = plt.figure()
sub2 = fig2.add_subplot(111)
sub2.plot(xx, yy)
"""

# 添加坐标轴 add_axes()

fig1 = plt.figure()
ax1 = fig1.add_axes([0.1, 0.1, 0.7, 0.7])
ax1.plot(xx, yy)


# 设置坐标轴名称: set_xlabel()  set_ylabel()

ax1.set_xlabel('xxxx', rotation=45, size=20)
ax1.set_ylabel('yyyy')

# 关闭显示坐标轴
ax1.set_axis_off()


# 一个窗口画多组图
"""
plt.scatter(xx, yy)
plt.scatter(xx + 2, yy)
plt.scatter(xx + 4, yy)
plt.scatter(xx + 1, yy - 1)
plt.scatter(xx + 3, yy - 1)
"""
# 显示标签1  使用legend方法显示label标签
"""
plt.scatter(xx, yy, label='xxxx')
plt.scatter(xx + 1, yy, label='yy')
plt.legend()
"""
# 显示标签2
plt.scatter(xx, yy)
plt.scatter(xx + 1, yy)
# plt.legend(['xxx', 'yy'])

# 显示标签位置
# 默认选择位置 loc属性 0 - 10
# 自定义位置bbox_to_anchor = (0.5, 0.5)
plt.legend(['xxx', 'yyy'], ncol=2, bbox_to_anchor=(0.5, 0.5))


plt.show()








