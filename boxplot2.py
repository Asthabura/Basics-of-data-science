import pandas as pd
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
df=pd.DataFrame(np.random.rand(20,3),columns=['C1','C2','C3'])
#since we used two different libraries you will see the difference in the figures
sns.boxplot(data=df,color='yellow')#Here on giving color we get our figure filled with the mentioned color
df.plot.box(grid='True',color='blue')#here on giving color thr lines of boxplot takes that color
plt.show()

