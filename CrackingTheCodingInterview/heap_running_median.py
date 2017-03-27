#!/bin/python3

# FAILS TCs #1, 3, 4, 6, 8, 9

from heapq import heappush, heappop

class MidHeap:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []
    
    def __len__(self):
        return len(self.min_heap) + len(self.max_heap)

    @property
    def lower_median(self):
        return -1.0 * self.min_heap[0]
    
    @property
    def upper_median(self):
        return 1.0 * self.max_heap[0]
    
    def append(self, value):
        if len(self) > 1:
            if value <= self.lower_median:
                heappush(self.min_heap, -1 * value)
            else:
                heappush(self.max_heap, value)
        elif len(self.min_heap) == 1 and len(self.max_heap) == 0:
            self.max_heap.append(value)
        else:
            # min heap has nothing or both have nothing.
            # arbitrarily append to the min heap.
            self.min_heap.append(-1.0 * value)
            
        if len(self.min_heap) - len(self.max_heap) > 1:
            heappush(self.max_heap, -1.0 * heappop(self.min_heap))
        if len(self.max_heap) - len(self.min_heap) > 1:
            heappush(self.min_heap, -1.0 * heappop(self.max_heap))
    
    @property
    def median(self):
        if len(self.min_heap) > len(self.max_heap):
            return self.lower_median
        elif len(self.min_heap) < len(self.max_heap):
            return self.upper_median
        else:
            return (self.lower_median + self.upper_median) / 2
        
    def __repr__(self):
        return '<MidHeap Min={}, Max={}>'.format(self.min_heap, self.max_heap)

heap = MidHeap()

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
   a_t = int(input().strip())
   heap.append(a_t)
   print(heap.median)



