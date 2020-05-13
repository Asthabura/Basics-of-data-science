from matplotlib import pyplot as plt
math_marks=[88,92,80,89,100,80,60,100,80,34]
science_marks=[35,79,79,48,100,88,32,45,20,30]
marks_range=[10,20,30,40,50,60,70,80,90,100]
plt.scatter(marks_range,math_marks,color='red',label='Math marks',edgecolor='black',linewidth=1,alpha=0.75) #alpha defines the intensity of the color.
plt.scatter(marks_range,science_marks,color='green',label='Science marks',edgecolor='black',linewidth=1,alpha=0.75)
plt.legend(loc='upper left') #loc hepls us to place the legend bar consisting of labels wherever we wish.
plt.xlabel('Marks scored')
plt.ylabel('Marks range')
plt.title('Test score')
plt.tight_layout()
plt.show()
