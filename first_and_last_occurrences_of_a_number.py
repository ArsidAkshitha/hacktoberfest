

from typing import List

def first_and_last_occurrences_of_a_number(nums: List[int], target: int) -> List[int]:
    """
    Problem:
    Given a sorted array 'nums', return the indices of the first and last occurrence of 'target'.
    If 'target' is not found, return [-1, -1].
    
    Example:
    nums = [1, 2, 3, 4, 4, 4, 5], target = 4
    Output: [3, 5]
    """

    def find_first(nums, target):
        """Binary search to find the first occurrence of target"""
        left, right = 0, len(nums) - 1
        first = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                first = mid       # record possible first occurrence
                right = mid - 1   # move left to find earlier occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return first

    def find_last(nums, target):
        """Binary search to find the last occurrence of target"""
        left, right = 0, len(nums) - 1
        last = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                last = mid        # record possible last occurrence
                left = mid + 1    # move right to find later occurrence
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return last

    # Find both first and last occurrence
    first = find_first(nums, target)
    last = find_last(nums, target)

    return [first, last]

