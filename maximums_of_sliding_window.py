# There's a sliding window of size k that slides through an integer array from left to right. Create a new array that records the largest number found in each window as it slides through.

from typing import List
from collections import deque

def maximums_of_sliding_window(nums: List[int], k: int) -> List[int]:
    n = len(nums)
    if not nums or k == 0:
        return []
    
    res = []
    dq = deque()  # will store indices
    
    for i in range(n):
        # Remove elements out of the current window
        while dq and dq[0] <= i - k:
            dq.popleft()
        
        # Maintain decreasing order in deque
        while dq and nums[dq[-1]] <= nums[i]:
            dq.pop()
        
        dq.append(i)
        
        # First window ends at index k-1
        if i >= k - 1:
            res.append(nums[dq[0]])
    
    return res
