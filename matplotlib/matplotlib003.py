import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

"""
# 柱状图
# bar(index, data, width, bottom, tick_label)
plt.bar([1, 2, 3, 4], [50, 15, 20, 35],
        width=0.5, bottom=[0, 0, 0, 0],
        tick_label=['python', 'java', 'c++', 'php'])

# 叠加柱状图
plt.bar([1, 2, 3, 4], [50, 30, 40, 10],
        width=0.5, bottom=[50, 15, 20, 35],
        tick_label=['python', 'java', 'c++', 'php'])
"""
# 并列柱状图
"""
plt.bar([0.3], [50], width=0.4)
plt.bar([0.7], [60], width=0.4)
plt.bar([0.5], [0], tick_label=['英语'])
"""

# 饼状图 pie(data, labels, autopct='%1.1f%%', explode)
# plt.pie([10, 30, 20], labels=['Python', 'C++', 'Java'], autopct='%1.2f%%', explode=[0.1, 0, 0])


# DataFrame  自带绘图函数

# 实例
table = pd.DataFrame(data=np.random.randint(0, 100, 16).reshape(4, 4),
                     columns=['Python', 'C++', 'PHP', 'Java'],
                     index=['spiderman', 'jack', 'lili', 'hulk'])
print(table)
# 图的主要类型 kind=line  bar  barh(横向)  pie
# subplots=True  分图展示
# 线形图
# table.plot(kind='line')

# 柱状图
# table.plot(kind='bar')
# table.plot(kind='bar', subplots=True)
# 横向树状图
# table.plot(kind='barh', subplots=True)
# table.plot(kind='barh')
# 饼状图
# table.plot(kind='pie', subplots=True)
table['Python'].plot(kind='pie', subplots=True)












plt.show()
