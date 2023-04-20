import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 生成随机数据
data1 = np.random.normal(0, 1, 100)
data2 = np.random.normal(2, 1.5, 80)
data3 = np.random.normal(-2, 2, 120)
data4 = np.random.normal(1, 0.5, 150)
data5 = np.random.normal(-1, 0.8, 90)

# 小提琴图
plt.figure(figsize=(8,6))
plt.violinplot([data1, data2, data3, data4, data5])
plt.title("Violin Plot")
plt.xlabel("Group")
plt.ylabel("Value")
plt.show()

# 箱线图
plt.figure(figsize=(8,6))
plt.boxplot([data1, data2, data3, data4, data5])
plt.title("Box Plot")
plt.xlabel("Group")
plt.ylabel("Value")
plt.show()

# 三维散点图
fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection='3d')
ax.scatter(data1, data2, data3, c='r', marker='o')
ax.set_xlabel('X Label')
ax.set_ylabel('Y Label')
ax.set_zlabel('Z Label')
plt.title("3D Scatter Plot")
plt.show()

# 折线图
plt.figure(figsize=(8,6))
plt.plot(data1, label="Group 1")
plt.plot(data2, label="Group 2")
plt.plot(data3, label="Group 3")
plt.plot(data4, label="Group 4")
plt.plot(data5, label="Group 5")
plt.title("Line Plot")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.show()

