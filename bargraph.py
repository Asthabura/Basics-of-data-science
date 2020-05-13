import numpy as np
from matplotlib import pyplot as plt
group_x=['G1','G2','G3','G4','G5']
x_indexes=np.arange(len(group_x)) #x_indexes helps us to display our desired values on the x-axis instaed of sixe of bar.
width=0.25 #Helps to avoid overlapping of bars if we plot more than one data on the same graph.
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
plt.xticks(x_indexes+width, ('G1', 'G2', 'G3', 'G4', 'G5')) #Sets the location on the x-axis.
plt.legend()

plt.tight_layout() #Provides extra padding to our graph.
plt.show()
