import numpy as np

#allows for printing random number arays arrays
b = np.empty(2,dtype=int)
print ("Matrix b: \n", b)

a = np.empty([2,2],dtype=int)
print ("Matrix a: \n", a)

c = np.empty([3,3],dtype=int)
print ("Matrix c: \n", c)


a = np.zeros(2, dtype = int)
b = np.zeros([2,2], dtype = int)
c = np.zeros([3,3])

statment = f'\n###\nMatrix a : \n {a} \n \nMatrix b : \n {b} \n\nMatrix c : \n {c} \n###'

print(statment)