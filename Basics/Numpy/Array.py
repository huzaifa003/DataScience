import numpy as np;

arr0 = np.array((1,2,3,4)) #1D Array
print(arr0)

arr1 = np.array([(1,2,3),(2,3,4),(5,6,7)]) #2D Array
print (arr1)

arr2 = np.array([(10,20,30),(20,30,40),(50,60,70)]) #2D Array 
print (arr2)

print("\nSum of above array = \n")
arr3 = arr1+arr2 #2D Array
print(arr3)

print(arr3.dtype) #Shows the type of data
print(arr3.ndim) #Checks dimension of array
print(arr3.size) #Checks size of array

arr4 = np.array([[(10,20,30),(20,30,40),(50,60,70)]]) #3Darray
print(arr4)
print(arr4.dtype) #Shows the type of data
print(arr4.ndim) #Checks dimension of array
print(arr4.size) #Checks size of array

arr5 = arr4.T #Transpose
print (arr5)
print(arr5.dtype) #Shows the type of data
print(arr5.ndim) #Checks dimension of array
print(arr5.size) #Checks size of array

arr6 = np.array([[1,2],[2,3],[3,1]])
print(arr6)
print(arr6.dtype) #Shows the type of data
print(arr6.ndim) #Checks dimension of array
print(arr6.size) #Checks size of array


#Basic Operations
print("--------------------BASIC OPERATIONS------------------")
print(arr6[0,1])
print(arr6[1,1]) #basic array accessing

print("--------------------Splicing OPERATIONS------------------")
print(arr3[0:,2]) #First arg shows the starting row and 2nd arg shows the index of row that needs to be printed
print(arr3[1:,2]) #Splicing 

print("--------------------Max & Min & Sum OPERATIONS------------------")
print(arr3.max())
print(arr3.min())
print(arr3.sum())

print("--------------------Arithmetic OPERATIONS------------------")

print(arr1/arr2)
print(arr1*arr2)

print("--------------------------------------")
print("--------------------Advanced OPERATIONS------------------")
print(arr3.ravel()) #Single Column

print("--------------------Axis OPERATIONS------------------")
print(arr3.sum(axis=1)) #Added second row of all rows
print(arr3.sum(axis=0)) #Added first row of all rows

print("--------------------SQR Root, AVG And STD Deviation OPERATIONS------------------")
print(np.sqrt(arr3))
print(np.average(arr3))
print(np.std(arr3))

print("--------------------Exponential & Log OPERATIONS------------------")
print(np.exp(arr3))
print(np.log(arr3))