# Based on FIFO (First IN First OUT)
# Technically, we can use List to implement Queue in Python, but it's not optimal because we need to remove the element from the beginning of the list everytime needed, which needs to shift all elements and cause a time complexity to increase.

# We can use dequeue class from collection module

from collections import deque

queue = deque([])
# print("Queue: ", queue) 
# deque has the methods similar to the list. 
queue.append(1)
queue.append(2)
queue.append(3)
print("Queue", queue)
# In order to remove it from the beginning of the list (queue), we use a method called popleft. 

queue.popleft()
print("pop left: ", queue)