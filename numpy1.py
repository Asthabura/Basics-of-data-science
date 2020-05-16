import numpy as np
a=np.arange(57,69).reshape(3,4) #converted a bunch on number into a 2d array 
print("Original array")
print(a)
print("Updating the array")
a[2,3]=96  #update 
print("Reversing the given array")
a=a[ : :-1]
print(a)
print("changing the datatype of the array")
print(np.asfarray(a))
