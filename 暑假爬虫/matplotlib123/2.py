import matplotlib.pyplot as plt
import matplotlib
import random

# 设置字体
font = {
    'family':"MicroSoft YaHei",
    'weight':'bold',
}
matplotlib.rc("font", **font)

fig = plt.figure(figsize = (20, 8), dpi = 80)
x = range(0, 120)
y = [random.randint(20, 35) for i in range(120)]
plt.plot(x, y)

_xtick_labels = ["10点{}".format(i) for i in range(60)]
_xtick_labels += ["11点{}".format(i) for i in range(60)]
plt.xticks(list(x)[::3], _xtick_labels[::3], rotation = 45)

plt.show()
