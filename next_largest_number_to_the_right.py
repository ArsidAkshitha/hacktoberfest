# Given an integer array nums, return an output array res where, for each value nums[i], res[i] is the first number to the right that's larger than nums[i]. If no larger number exists to the right of nums[i], set res[i] to ‐1.

from typing import List

def next_largest_number_to_the_right(nums: List[int]) -> List[int]:
    n = len(nums)
    res = [-1] * n
    stack = []  # will store potential "next greater" candidates
    
    for i in range(n - 1, -1, -1):  # iterate from right to left
        while stack and stack[-1] <= nums[i]:
            stack.pop()
        if stack:
            res[i] = stack[-1]
        stack.append(nums[i])
    
    return res
