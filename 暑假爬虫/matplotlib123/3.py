import matplotlib.pyplot as plt
import matplotlib

# 设置字体
font = {
    'family':"MicroSoft YaHei",
    'weight':'bold',
}
matplotlib.rc("font", **font)

fig = plt.figure(figsize = (20, 8), dpi = 80)
y1 = [1, 0, 1, 1, 2, 4, 3, 2, 3, 4, 4, 5, 6, 5, 4, 3, 3, 1, 1, 1]
y2 = [1, 0, 3, 1, 2, 2, 3, 3, 2, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
x = range(11, 31)
plt.plot(x, y1, label = '自己', color = 'red', alpha = 0.7)
plt.plot(x, y2, label = '同桌', color = 'orange', alpha = 0.7)

xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x, xtick_labels)

plt.legend(loc = 'best')
plt.grid()

plt.show()
