import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((3, 4)) * 0, columns = ['a', 'b', 'c', 'd'], index = [1, 2, 3])
df2 = pd.DataFrame(np.ones((3, 4)) * 1, columns = ['b', 'c', 'd', 'e'], index = [2, 3, 4])

print(df1)
print(df2)

# 1. 默认为outer模式
# 2. 相当于内连接和全外连接的差别
res = pd.concat([df1, df2], join = 'inner', ignore_index = True)
print(res)
res = pd.concat([df1, df2], join = 'outer', ignore_index = True)
print(res)
