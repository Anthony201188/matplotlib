import matplotlib.pyplot as plt
import math

x = [1,2,3,4]

logN = [math.log(num) for num in x]
print(logN)

N = [num for num in x]
print(N)

NlogN = [num * math.log(num) for num in x]
print(NlogN)

N_square = [num ** 2 for num in x]
print(N_square)

N_exp = [math.exp(num) for num in x]
print(N_exp)

N_prod = [num + sum(range(num)) for num in x]       # "!" is the produc or sum of all numbers up untill x
print(N_prod)

plt.scatter(x,logN , marker='x', color='blue', label='logN')
plt.plot(x, logN, label="LogN") # cant seem to make these in the same plot
plt.plot(x, N,label="N")
plt.plot(x,NlogN, label="NlogN")
plt.plot(x,N_square, label="N_square")
plt.plot(x,N_exp,label="N_exp")
plt.plot(x,N_prod, label="N!")


plt.legend()
plt.show()




