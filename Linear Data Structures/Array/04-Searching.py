from array import *
print("Searching an element in array\n\n")

array_4 = array('i', [1,2,3,4,5]) #defining array

for k in array_4:

    if k == 5:              #condtition for cheching an element in array
        t = True
        break

    else :
        t= False

if t == True:
    print("Element found..\n")

else :
    print("Element not found..\n")