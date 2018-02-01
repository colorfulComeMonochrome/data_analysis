import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


imdata = plt.imread('fish.png')

# 数据变换
# mydata = np.random.rand(100*100*3).reshape(100,100,3)
# mydata = np.ones(100*100*3).reshape(100,100,3)

mydata = np.zeros(100*100*3).reshape(100,100,3)
# mydata = mydata + np.array([1, 0, 0])
mydata = mydata + np.array([0.5, 0.3, 0.7])

# print(imdata)
# print(imdata.shape)

# plt.imshow(imdata[:, :, ::-1])
# plt.imshow(imdata[::50, ::50, ::])
plt.imshow(mydata)





























plt.show()










