from numpy import random
import numpy as np
#random
'''
x = random.randint(100)
print(x)
'''
'''
x = random.rand(5)
print(x)
x = random.randint(100,size=(5))
print(x)
x = random.choice([3, 5, 7, 9])
print(x)
x = random.choice([3, 5, 7, 9], size=(2, 3, 5)) #make a matrix of blocks=2, rows=3, col=5, with random values from the given 1x4 matrix
print(x)
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(20)) # probability of choosing each element The sum of p must be 1
print(x)
x = random.choice([3, 5, 7, 9], p=[0.1, 0.3, 0.6, 0.0], size=(3, 5))
print(x)
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print(arr)
arr = np.array([1, 2, 3, 4, 5])
print(random.permutation(arr))
print(arr)
'''