'''
What is NumPy?
NumPy is a Python library used for working with arrays.
It also has functions for working in domain of linear algebra, fourier transform, and matrices.
NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.
NumPy stands for Numerical Python.
 
Why Use NumPy?
In Python we have lists that serve the purpose of arrays, but they are slow to process.
NumPy aims to provide an array object that is up to 50x faster than traditional Python lists.
The array object in NumPy is called ndarray, it provides a lot of supporting functions that make working with ndarray very easy.
Arrays are very frequently used in data science, where speed and resources are very important.
 
Why is NumPy Faster Than Lists?
NumPy arrays are stored at one continuous place in memory unlike lists, so processes can access and manipulate them very efficiently.
This behavior is called locality of reference in computer science.
This is the main reason why NumPy is faster than lists. Also it is optimized to work with latest CPU architectures.
 
Which Language is NumPy written in?
NumPy is a Python library and is written partially in Python, but most of the parts that require fast computation are written in C or C++.

'''


import numpy as np 

'''
print(np.__version__)
'''
'''
arr = np.array((1,2,3,4,5)) #used to make array (here we passes the tuple)
print(arr)
print(arr[2]+arr[0])
'''


#0-Dimension: have single value 
'''
arr = np.array((40))
print(type(arr))
'''

#1-Dimension: single tuple/list
'''
arr = np.array([1,2,3,4,5])
print(type(arr))
print(arr[2])
'''
#2-Dimension: matrix form
'''
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(type(arr))
print(arr)
print(arr[1,2])
print(arr[0,2]) 
print(arr.ndim) #to check the dimentions

'''
'''
arr = np.array([[1,2,3,4,5],[6,7,8,9,10],[6,7,8,9,10]])
print(type(arr))
print(arr)
print(arr.ndim)
print(arr[2,-2])
'''

#3-Dimension: have multiple 2d matrix
'''
arr=np.array([[[1,2,3],[4,2,3]],[[0,2,4],[3,3,4]],[[34,2,4],[3,5,'a']]])
print(arr)
print(arr.ndim)
print(arr[1,1,1])
'''

#slicing

# 1D 
'''
arr = np.array((1,2,8,4,5,3,2))
print(type(arr))
print(arr[0:3])
print(arr[:3])
print(arr[2:8:2])
'''

#2D
'''
arr = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr[1,1:6:1])
'''
'''
arr=np.array([[1,1,1],[2,2,2],[3,3,3]])
print(arr[2:6:1])
'''
#3D

'''
arr=np.array([[[1,2,3],[4,2,3]],[[0,2,4],[3,3,4]],[[34,2,4],[3,5,44]]])
print(arr[1,0,0:2])
'''

#to slide out a whole row
'''
arr=np.array([[[1,2,3],[4,5,6]],[[2,2,2],[3,3,3]],[[5,5,5],[6,6,6]]])
print(arr[1,1])
'''

'''
arr = np.array([[[1,1,1],[2,2,2],[3,3,3]],[[4,4,4],[5,5,5],[6,6,6]],[[7,7,7],[8,8,8],[9,9,9]]])
print(arr[1,2,:])
'''