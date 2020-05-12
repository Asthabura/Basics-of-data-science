import numpy as np
from matplotlib import pyplot as plt
group_x=['G1','G2','G3','G4','G5']
x_indexes=np.arange(len(group_x))
width=0.25
men_y = (22, 30, 33, 30, 26)
plt.bar(x_indexes-width, men_y,width=width,
color='g',
label='Men')
women_means = (25, 32, 30, 35, 29)
plt.bar(x_indexes, women_means,width=width,
color='r',
label='Women')
plt.xlabel('Person')
plt.ylabel('Scores')
plt.title('Scores by person')
plt.xticks(x_indexes+width, ('G1', 'G2', 'G3', 'G4', 'G5'))
plt.legend()

plt.tight_layout()
plt.show()
