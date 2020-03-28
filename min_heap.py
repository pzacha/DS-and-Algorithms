import heapq
from random import randint

#Creating random list
heap = [randint(1, 100) for i in range(6)]
print(heap)

#Convert list to heap
heapq.heapify(heap)
print(heap)

#Add element to heap
heapq.heappush(heap,21)
print(heap)

#Remove smallest element from heap
heapq.heappop(heap)