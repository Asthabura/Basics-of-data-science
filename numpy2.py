import numpy as np 
a1=np.array([(1,2,3),(3,4,5)])
a2=np.array([(9,8,7),(7,6,5)])
print("Adding the two matrices")
print(a1+a2)
print("Subtracting the two matrices")
print(a2-a1)
print("Multiplying the two matrices")
print(a1*a2)
print("Dividing the two matrices")
print(a2/a1)
print("finding the square root")
print(np.sqrt(a1))
print(np.sqrt(a2))
print("finding the standard deviation")
print(np.std(a1))
print(np.std(a2))
print("Concatenating the two matrices in:")
print("vertical stacking")
print(np.vstack((a1,a2)))
print("Hortizontal stacking")
print(np.hstack((a1,a2)))
print("Median of the given arrays")
print(np.median(a1))
print(np.median(a2))
print("Variance of the given arrays")
print(np.var(a1))
print(np.var(a2))
