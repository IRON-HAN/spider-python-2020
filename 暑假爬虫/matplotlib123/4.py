import matplotlib.pyplot as plt
import matplotlib

# 设置字体
font = {
    'family':"MicroSoft YaHei",
    'weight':'bold',
}

matplotlib.rc("font", **font)
a = [11, 17, 16, 11, 12, 11, 12, 6, 6, 7, 8, 9, 12, 15, 14, 17, 18, 21, 16, 17, 20, 14, 15, 15, 15, 19, 21, 22, 22, 22,
     23]
b = [26, 26, 28, 19, 21, 17, 16, 19, 18, 20, 20, 19, 22, 23, 17, 20, 21, 20, 22, 15, 11, 15, 5, 13, 17, 10, 11, 13, 12,
     13, 6]

plt.figure(figsize = (20, 8), dpi = 80)

x1 = range(1, 32)
x2 = range(51, 82)
plt.scatter(x1, a)
plt.scatter(x2, b)

_x = list(x1) + list(x2)
xtick_labels = ['3月{}日'.format(i) for i in x1]
xtick_labels += ['10月{}日'.format(i - 50) for i in x2]
plt.xticks(_x[::3], xtick_labels[::3], rotation = 45)

plt.show()
