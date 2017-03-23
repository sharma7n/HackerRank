#!/bin/python3

from heapq import *
import sys

def get_median(h):
    if len(h) < 1:
        return 0

    if len(h) % 2 == 0:
        mid_indices = ((len(h) / 2) - 1, len(h) / 2)
    else:
        mid_indices = (len(h) / 2)
    
    return sum(h[idx] for idx in mid_indices) / len(mid_indices)

heap = heapify([])

n = int(input().strip())
a = []
a_i = 0
for a_i in range(n):
   a_t = int(input().strip())
   heappush(heap, a_t)
   print(get_median(heap))



