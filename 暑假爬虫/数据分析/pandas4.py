import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods = 6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index = dates, columns = ['A', 'B', 'C', 'D'])
df.iloc[0, 1] = np.nan
df.iloc[1, 2] = np.nan
print(df)
# print(df.dropna(axis = 0, how = 'any'))
# # how = { 'any', 'all'}
# # axis = 0 对行操作 -- 竖向的
# # axis = 1 对列操作 -- 横向的


# # 整个表格检查是否是nan
# print(df.isnull())
#
# # 填充nan
# print(df.fillna(value = 0))

# 检查整个表格中是否存在nan
print(np.any(df.isnull()) == True)
