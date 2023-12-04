import matplotlib.pyplot as plt
import math


import matplotlib

# Get the list of attributes in the module
attributes = dir(matplotlib)

# Print each attribute
for attribute in attributes:
    print(attribute)





X = [1,2,3,4,5]

euler = math.exp(1)
print(euler)

Y_euler = [math.exp(num) for num in X]        # y = exp( x )      y=f(x)=e^x

plt.plot(X, Y_euler)
plt.show()