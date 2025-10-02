def find_the_insertion_index(nums, target):
    """
    Problem:
    You are given a sorted array 'nums' containing unique values and an integer 'target'.
    - If 'target' is found in 'nums', return its index.
    - Otherwise, return the index where 'target' should be inserted to maintain sorted order.

    Example:
    nums = [1, 2, 4, 5, 7, 8, 9], target = 4 → Output: 2
    nums = [1, 2, 4, 5, 7, 8, 9], target = 6 → Output: 4
    """

    left, right = 0, len(nums) - 1  # define search boundaries

    # Perform binary search
    while left <= right:
        mid = (left + right) // 2   # find the middle index
        
        if nums[mid] == target:     # if target found at mid
            return mid
        elif nums[mid] < target:    # if target is bigger, move right
            left = mid + 1
        else:                       # if target is smaller, move left
            right = mid - 1

    # If not found, 'left' will be the correct insertion index
    return left

