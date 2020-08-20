import numpy as np
import pandas as pd

if __name__ == '__main__':
    s = pd.Series([1, 3, 6, np.nan, 44, 1])
    # print(s)

    dates = pd.date_range('20200820', periods = 6)
    # print(dates)

    df = pd.DataFrame(np.random.randn(6, 4), index = dates, columns = ['a', 'b', 'c', 'd'])
    # print(df)

    df2 = pd.DataFrame(np.arange(12).reshape(3, 4))
    print(df2)

    print(df2.describe())
