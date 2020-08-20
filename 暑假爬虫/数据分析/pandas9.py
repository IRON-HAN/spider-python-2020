import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# methods
# bar, hist, box, kde, area, scatter, hexbin, pie


data = pd.DataFrame(np.random.randn(1000, 4), index = np.arange(1000), columns = list("ABCD"))
data = data.cumsum()
ax = data.plot.scatter(x = 'A', y = 'B', color = 'Blue', label = 'Class 1')
data.plot.scatter(x = 'A', y = 'C', color = 'Green', label = 'Class 2', ax = ax)
data.plot()
plt.show()
