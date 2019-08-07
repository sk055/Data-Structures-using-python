from array import *

array_1 = array('i', [1,2,3,4,5,6,7,8,9,0]) #defining array

for x in array_1:         #Traversing array
    print(x)


print(type(array_1))  #type checking
#
print(array_1[0]) #accessing array using index

array_1.append(100)

print("\nAppended..")

for x in array_1:         #Traversing array after appending an element
    print(x)




