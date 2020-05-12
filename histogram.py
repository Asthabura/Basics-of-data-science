from matplotlib import pyplot as plt
frequency=[6,15,16,21,18]
height=[0,10,20,24,30,50]
plt.hist(height,bins=height,edgecolor='black')
plt.title('Heights of plants growing in a garden')
plt.xlabel('Height')
plt.tight_layout()
plt.show()
