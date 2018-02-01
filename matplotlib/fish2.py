import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


imdata = plt.imread('fish.png')


print(imdata.shape)

# 灰度
# imdata = imdata.mean(axis=2)
# plt.imshow(imdata, cmap='gray')















plt.imshow(imdata, cmap='gray')
plt.show()