from matplotlib import pyplot as plt
slices=[46,27,26,19,17]
labels=['United States','Great Britain','China','Russia','Germany']
colors=['red','green','yellow','orange','blue']
explode=[0.1,0,0,0,0] #separates the pieces of the pie from the centre based upon the specified distance.
plt.pie(slices,labels=labels,colors=colors,shadow=True,wedgeprops={'edgecolor':'black'},explode=explode,autopct='%1.1f%%') #autopct displays the % represented by each piece.
plt.title('Max gold medals won')
plt.tight_layout()
plt.show()
