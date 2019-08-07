from array import *

print("Deleting element in array\n")

array_3 = array('i', [1,2,3,4,5]) #defining array

for k in array_3:
    print(k)
print("\nResult")
# array_3.remove(1)   #removes element upto this index
array_3.pop(1)  #removes the specified index element


for k in array_3:         #Traversing array after Deletion
    print(k)
