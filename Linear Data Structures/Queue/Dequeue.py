import collections

dequeue = collections.deque([1,2,3])
print(dequeue)

dequeue.append(4)       #append the element at the right side
print(dequeue)

dequeue.appendleft(0)   #append the element at the left side
print(dequeue)

dequeue.remove(0) #removing a specific element
print(dequeue)

dequeue.pop()       #deleting the element at the right side
print(dequeue)

dequeue.popleft()       #deleting the element at the left side
print(dequeue)