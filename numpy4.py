import numpy as np
a=np.arange(12).reshape(3,4)
print("Shape of the array")
print(a.shape)
print("Size of the array")
print(a.size)
print("Slicing of elements of array")
print(a[0:2,3])
print("Log of the elements")
print(np.log(a)) #natural log with base e
print(np.log10(a)) #log with base 10
print("Exponentent of elements")
print(np.exp(a))
