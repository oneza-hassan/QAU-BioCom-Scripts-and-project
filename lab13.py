import numpy as np
'''
arr=np.array([[[1,2,3],[4,5,6]],[[55,44,33],[12,34,2]]])
print(arr)
print("---------")

for x in arr:
    print("xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
    print(x)
    print()
    for y in arr:
        print("yyyyyyyyyyyyyyyyyyyyyyyyyyyyyy")
        print(y)
        print()
        for z in arr:
            print("zzzzzzzzzzzzzzzzzzzzzzzz")
            print(z)
            print()
'''

'''
arr=np.array([[[1,2,3],[4,5,6]],[[55,44,33],[12,34,2]]])
print(arr)
print("---------")

for x in arr:
    for y in arr:
        for z in arr:
            print(z)
            print()
'''

#iter 
'''
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr)
for x in np.nditer(arr[1,1,:]):
  print(x)
'''

#np.nditer three paramenters: array to iterate over, flags and op_dtypes
'''
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['float']): #flag ‘buffered’, iterator will use a buffer to store the values of the array. iterator to modify the values without affecting the original array.
                                          # op_dtypes, which is a list of data types that specify the type of the output elements
    print(x)
'''

#loop through sliced array using np.nditer function
'''
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print((arr[:, ::2]))  #the sliced array is arr[:, ::2], which means all rows and every other column starting from the first one
for x in np.nditer(arr[:, ::2]):
    print(x)
'''

#A program that prints the indices and values of the elements that are equal to 5 in a 2D numpy array, and also prints the corresponding row of the array.
'''
arr = np.array([[1, 5, 3],[4, 2, 6],[7, 8, 5]]) #2D numpy array row=3, col=3
print(arr)
for idx, x in np.ndenumerate(arr):# Loop over the elements and their indices in the array
    if(x==5):
        print(idx, x) #for example for first 5 found it will be ((0,1),5) that is ((row,column),value)
        for x in np.nditer(arr[idx[0]:idx[0]+1, ::]):  # Create a slice of the array that contains the row that has the element and all columns
            #for first iteration of outer loop; slice is arr[0:1, ::],which is arr[0], [1, 5, 3].
            #for second itr of out loop: slice is arr[2:3, ::], arr[2],  [7, 8, 5].
            print(x)
'''

#reshape and concatenate

'''
arr1 = np.array([5, 7, 3])
arr2 = np.array([4, 9, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
newarr=arr.reshape(2,3) #reshape methods should have parameter that should multiply to the original num of elements in the arr
print(newarr)
newarr = arr.reshape(3, -1) #using -1 sets the missing dimention accordingly, automatically
print(newarr)
'''