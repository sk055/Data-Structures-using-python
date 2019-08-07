from array import *

print("Insertion in array")

array_1 = array('i', [1,2,3,4,5]) #defining array

for k in array_1:
    print(k)
print("\nResult\n")
array_1.insert(1,30)

for k in array_1:         #Traversing array after insertion
    print(k)
