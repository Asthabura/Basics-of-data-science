import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df = pd.DataFrame(np.random.rand(7,3), columns=['A', 'B', 'C'])
df.plot.box(grid=True)
plt.show()
