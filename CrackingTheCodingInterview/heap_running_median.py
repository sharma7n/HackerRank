#!/bin/python3

# now passes all testcases

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
        """
            If the heap is empty, push to the lower.
            For each new value,
                if the value < the lower max, push it to the lower.
                if the value is > the upper max, push it to the upper.
                then rebalance
        """
        
        if len(self) == 0:
            heappush(self.min_heap, -1 * value)
        else:
            if value <= self.lower_median:
                heappush(self.min_heap, -1 * value)
            else:
                heappush(self.max_heap, value)
                
        self._rebalance()
        
    def _rebalance(self):
        while abs(len(self.min_heap) - len(self.max_heap)) > 1:
            if len(self.min_heap) > len(self.max_heap):
                heappush(self.max_heap, -1 * heappop(self.min_heap))
            else:
                heappush(self.min_heap, -1 * heappop(self.max_heap))
                
    
    @property
    def median(self):
        if len(self.min_heap) > len(self.max_heap):
            return self.lower_median
        elif len(self.min_heap) < len(self.max_heap):
            return self.upper_median
        else:
            return (self.lower_median + self.upper_median) / 2
        
    def __repr__(self):
        return '<MidHeap Lower={}, Upper={}>'.format(self.min_heap, self.max_heap)

heap = MidHeap()

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
   a_t = int(input().strip())
   heap.append(a_t)
   print(heap.median)



