import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
df = pd.DataFrame(np.random.randn(15, 2),
                  columns=['C1', 'C2'])
df['Sections'] = pd.Series(['P', 'Q','P','Q',]) #Series helps us to name each column of the boxplot
boxplot = df.boxplot(by='Sections',rot=55,fontsize=10,color='green') #by gives a heading to our boxplot
plt.show()
