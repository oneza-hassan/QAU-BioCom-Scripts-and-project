
import numpy as np 

#check the datatype of the elements in array, int
'''
arr=np.array([1,3,4,5])
print(type(arr))
print(arr.dtype)
'''
#check the datatype of the elements in array, char
'''
arr=np.array(["a","b","c"],dtype='c') 
print(arr)
print(arr.dtype)
'''
#to convert the datatype
'''
arr=np.array(["1.66","3.5","2.0"],dtype="f")
narr=arr.astype("i")
carr=arr.astype("c")
print(narr)
print(narr.dtype)
print(carr, carr.dtype, type(carr))
'''
#if you try to convert data types that are not possible to be interchanged it will throw error
'''
arr=np.array(["a","b","c"],dtype='c') 
narr= arr.astype("i")
print(arr)
print(arr.dtype)
'''
#bool datatype
'''
arr=np.array(["1","3","0"])
narr=arr.astype(bool)
print(narr)
print(narr.dtype)
'''
'''
name = input("Enter name: ")
total=30

num = int(input("Enter marks obtained: "))
if num<=30:
    percent = (num / total) * 100
    print(f"{name} got {num} out of total 30, and its percentage is  {percent}%.")
else:
    print(f"enter number that is less than {num}")
    
'''

#copy, view, type of obj and type of elements
'''
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy() #creates a copy of the array thats independent of arr
arr[0] = 25
print(type(x)) #prints the type of the object x
print(x.dtype) # prints the data type of the elements in the arra
print(arr)
print(x)
y = arr.view()
print(y)
'''

#unicode char array
'''
arr = np.array(["abc","alpha", "beta"])
x = arr.copy()
x[0] = 31
print(arr)
print(arr.dtype)
print(x.dtype)
print(x)
print(arr.base)
print(x.base)
'''

#base func
'''
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
y = arr.view()
print(x.base) #x is independent and own its own data
print(y.base) #y is dependent and relies on arr
'''

#shape of array
'''
arr = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]],[[1, 2, 3, 4], [5, 6, 7, 8]],[[1, 2, 3, 4], [5, 6, 7, 8]]])
print(arr)
print(arr.shape) 
print(arr.ndim)
'''

#reshape array to 2D and check dimention
'''
arr=np.array(range(0,12)) #1d array of 12 elements (0-11)
print(arr) #print num of dimentions of arr
print(arr.ndim)
newarr=arr.reshape(2,6) #row 2, col 6
print(newarr)
print(newarr.ndim)
newarr=arr.reshape(4,3) 
print(newarr)
'''

'''
arr=np.array(["biopython", "matlplotlib", "regex", True], dtype='str' )
newarr=arr.reshape(2,2)
print(arr, "  ", newarr, "  ", newarr.ndim," ", type(newarr), " ", newarr.dtype)
'''

#reshape array to 3D
'''
arr=np.array(range(0,18))
print(arr)
newarr=arr.reshape(3,-1,3) #3 blocks, 3 colums, -1 means “let the reshape method decide the size of this dimension” we can use -1 for rows.
print(newarr)
print(newarr.ndim)
'''
#reshape and base
'''
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print(arr.reshape(2, 4).base)# reshape the array into a two-dimensional array of 2 rows and 4 columns and print its base attribute
                             # the base attribute returns the original array that the new array is a view of
'''

# Write a Program to take input from user:
#1- Name
#2-Estimate Numbers Obtained
#Percentage when total is 30
#print results with name

'''
print("To calculate your %age enter the following details")
print("--------------------------------------------------")
name=input("Enter your name: ")
percentage=None
valid = False # initialize valid to False
while not valid: # repeat until valid is True
    num=int(input("Marks obtained: "))
    total=30
    try:
        if (num>=0 and num<=30): 
            percentage=(num*100)/30
            valid = True # set valid to True if marks are in range
        else:
            raise ValueError # raise an exception if marks are out of range
    except ValueError:
        print("Marks should be less than ", total) # handle the exception by printing an error message
                                                   # do not change valid, so the loop continues
    finally:
        print(name, " secured ", percentage, "%") 
        print("---------------------------------")
'''