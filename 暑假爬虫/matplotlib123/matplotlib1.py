import matplotlib.pyplot as plt

fig = plt.figure(figsize = (20, 8), dpi = 80)
# 数据在x轴的位置, 可迭代对象
x = range(2, 26, 2)
# 数据在y轴的位置
y = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# 画图
plt.plot(x, y)

# 设置坐标轴的刻度
xtick_label = [i / 2 for i in range(4, 49)]
# 每隔3个显示一个
plt.xticks(xtick_label[::3])
plt.yticks(range(min(y), max(y) + 1))

# 保存图片
plt.savefig("./sig_size.png")
# 展示
plt.show()
