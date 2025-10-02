
from typing import List

def cutting_wood(heights: List[int], k: int) -> int:
    """
    Problem:
    Given tree heights and a required wood length k,
    find the maximum height H at which the woodcutter can be set
    so that at least k meters of wood is cut.

    Approach:
    - Binary search for H between 0 and max(heights).
    - For each mid, calculate wood obtained if we cut at 'mid'.
    - If wood >= k, move search upwards (we can try a bigger H).
    - Else, move downwards.
    """

    left, right = 0, max(heights)  # search space
    result = 0

    while left <= right:
        mid = (left + right) // 2  # candidate cutting height

        # calculate total wood collected at height mid
        wood_collected = sum((h - mid) for h in heights if h > mid)

        if wood_collected >= k:
            result = mid        # mid is feasible
            left = mid + 1      # try higher
        else:
            right = mid - 1     # too high, try lower

    return result



