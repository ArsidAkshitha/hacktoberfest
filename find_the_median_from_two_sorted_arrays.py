from typing import List

def find_the_median_from_two_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Problem:
    Find the median of two sorted arrays as if merged.

    Approach:
    - Binary search on the smaller array to find correct partition.
    - Ensure left side elements <= right side elements.
    - Return median based on total length (odd/even).
    """

    # Ensure nums1 is the smaller array
    if len(nums1) > len(nums2):
        nums1, nums2 = nums2, nums1

    m, n = len(nums1), len(nums2)
    total = m + n
    half = (total + 1) // 2

    left, right = 0, m
    while left <= right:
        i = (left + right) // 2   # partition index in nums1
        j = half - i              # partition index in nums2

        # Left and right values around partitions
        left1 = nums1[i - 1] if i > 0 else float("-inf")
        right1 = nums1[i] if i < m else float("inf")

        left2 = nums2[j - 1] if j > 0 else float("-inf")
        right2 = nums2[j] if j < n else float("inf")

        # Check if partition is valid
        if left1 <= right2 and left2 <= right1:
            if total % 2 == 1:
                return float(max(left1, left2))  # odd length
            return (max(left1, left2) + min(right1, right2)) / 2  # even length

        elif left1 > right2:
            right = i - 1  # move partition left
        else:
            left = i + 1   # move partition right

