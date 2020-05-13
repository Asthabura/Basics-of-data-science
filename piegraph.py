from matplotlib import pyplot as plt
slices=[46,27,26,19,17]
labels=['United States','Great Britain','China','Russia','Germany']
colors=['red','green','yellow','orange','blue']
explode=[0.1,0,0,0,0] # separates the piece of the pie from the centre by specified distance.
plt.pie(slices,labels=labels,colors=colors,shadow=True,wedgeprops={'edgecolor':'black'},explode=explode,autopct='%1.1f%%')
# shadow makes the pie graph look a bit like 3-d and autopct helps to display the percentage each piece represents.
plt.title('Max gold medals won')
plt.tight_layout()
plt.show()
