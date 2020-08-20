import numpy as np
import pandas as pd

# if __name__ == '__main__':
dates = pd.date_range('20130101', periods = 6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index = dates, columns = ['A', 'B', 'C', 'D'])
print(df)

# # 按照列取
# print(df['A'])
# print(df.A)

# # 按照行取
# print(df[0:3])
# print(df['20130102':'20130104'])

# # 按照label(名字)
# print(df.loc['20130102'])
# print(df.loc['20130102', ['A', 'B']])

# # 按照位置(坐标)
# print(df.iloc[3:5, 1:3])
# print(df.iloc[[1, 3, 5], 1:3])

# 混合
# print(df.ix[:3, ['A', 'C']])
# 会抛异常

# 增加条件
print(df[df.A < 8])
