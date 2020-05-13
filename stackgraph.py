from matplotlib import pyplot as plt
days=[1,2,3,4,5,6,7]
student1=[3,4,2,6,7,8,4]
student2=[5,2,7,4,8,3,4]
student3=[1,1,3,1,4,1,6]
labels=('Student1','Student2','Student3')
colors=['red','yellow','green']
plt.stackplot(days,student1,student2,student3,labels=labels,colors=colors)
plt.legend(loc='upper left') #loc helps us to decide the place of legend bar consisting of labels.
plt.title('No. of hours contributed each day for school project')
plt.tight_layout()
plt.show()
