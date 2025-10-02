from typing import List

def find_the_target_in_a_rotated_sorted_array(nums: List[int], target: int) -> int:
    """
    Problem:
    Given a rotated sorted array and a target value,
    return the index of target. If not found, return -1.

    Approach:
    - Use modified binary search.
    - One half of the array is always sorted.
    - Decide which half to search based on target range.
    """

    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        # Found target
        if nums[mid] == target:
            return mid

        # Left half is sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1   # target in left half
            else:
                left = mid + 1    # target in right half

        # Right half is sorted
        else:
            if nums[mid] < target <= nums[right]:
                left = mid + 1    # target in right half
            else:
                right = mid - 1   # target in left half

    return -1  # not found


