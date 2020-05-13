from matplotlib import pyplot as plt
frequency=[6,15,16,21,18]
height=[0,10,20,24,30,50]
plt.hist(height,bins=height,edgecolor='black') #Bins helps us to decide the band size and edgecolor helps us to distinguish bands.
plt.title('Heights of plants growing in a garden')
plt.xlabel('Height')
plt.tight_layout()
plt.show()
