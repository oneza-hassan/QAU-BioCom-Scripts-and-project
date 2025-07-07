import numpy as np

#stack function for 1d array: take 2 arguments: tuple of array and axis
'''
arr1 = np.array(["proteases", "the", "backbone"])
arr2 = np.array(["digest", "polypeptide", "of protein"])
arr = np.stack((arr1, arr2), axis = 1) #stacks the two arrays along the second axis (axis = 1), which means it combines them column-wise.
print(arr)
'''
#stack/ concatenate/ vstack function for 2d array
'''
arr1 = np.array([[1, 2, 3],[7,8,9]])
arr2 = np.array([[4, 5, 6],[10,11,12]])
arr = np.stack((arr1, arr2), axis = 1)
print("stacked 2d array column wise", "-----------")
print(arr)
arr_conc = np.concatenate((arr1, arr2), axis = 1)
print("concatenated 2 d array column wise: ------------")
print(arr_conc)
arr_vstack = np.vstack((arr1, arr2)) #vstack=verticalstack
print("vstack array combine array row wise: -----------")
print(arr_vstack)
'''
#array_split array in to subarray
'''
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
new = np.array_split(arr, 4)
print(new)
'''
#array splitter in 2d row and column wise
'''
arr = np.array([[1, 2, 13], [3, 4, 14], [5, 6, 15], [7, 8, 16], [9, 10, 17], [11, 12, 18]])
print(arr)
newarr = np.array_split(arr, 3, 0) #split to 3 subarrays along the 1st axis; rows
print(newarr)
newarr = np.array_split(arr, 3, 1) #split to 3 subarrays along the 2nd axis; column
print(newarr)
'''
#split along 2nd axis column
'''
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
print(arr)
print(arr.size)
newarr = np.hsplit(arr, 3) #The function requires that the number of splits is a divisor of the array size along the specified axis. 
print(newarr)
'''
#finds the indices of the elements in the array that are even
'''
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
x = np.where(arr%2 == 0)
print(x)
'''
#other examples
'''
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
ind = np.where(arr > 5)
print(ind)
'''
'''
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
newarr = np.where(arr > 5, arr**2, arr)
print(newarr)
'''
'''
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
condlist = [arr < 3, (arr >= 3) & (arr <=6), arr >6]
choicelist = [-1, arr**3 , np.sqrt(arr)]
newarr = np.select(condlist , choicelist)
print(newarr)
'''