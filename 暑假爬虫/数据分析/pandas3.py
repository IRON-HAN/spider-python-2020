import numpy as np
import pandas as pd

dates = pd.date_range('20130101', periods = 6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index = dates, columns = ['A', 'B', 'C', 'D'])
print(df)

# # 单个值的修改
# df.iloc[2, 2] = 111
# print(df)
#
# df.loc['20130101', 'B'] = 222
# print(df)

# # 一整列的修改
# df.A[df.A > 4] = 0
# print(df)

# # 所有列的修改
# df[df.A > 4] = 0
# print(df)

# 添加一个列
df['F'] = np.nan
df['E'] = pd.Series([1, 2, 3, 4, 5, 6], index = dates)
print(df)
