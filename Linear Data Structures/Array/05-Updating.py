from array import *
print("\nUpdatation in array")

array_5 = array('i', [1,2,3,4,5,]) #defining array

for k in array_5:
    print(k)
print("\nResult")

array_5[0] = 100

for k in array_5:        #Traversing array after updatation
    print(k)

