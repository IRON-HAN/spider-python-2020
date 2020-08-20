import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.ones((1, 2)) * 0, columns = ['a', 'b'])
df2 = pd.DataFrame(np.ones((1, 2)) * 1, columns = ['a', 'b'])
df3 = pd.DataFrame(np.ones((1, 2)) * 2, columns = ['a', 'b'])

print(df1)
print(df2)
print(df3)

# = 0 行数增加, 拼接的行向下增长
res = pd.concat([df1, df2, df3], axis = 0)
print(res)

# = 1 列数增加, 拼接的列向右增长
res = pd.concat([df1, df2, df3], axis = 1)
print(res)

# ignore_index, 让index自动增长, 不会重复
res = pd.concat([df1, df2, df3], axis = 0, ignore_index = True)
print(res)


