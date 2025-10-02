
from typing import List

def matrix_search(matrix: List[List[int]], target: int) -> bool:
    """
    Problem:
    Given a matrix where:
    - Each row is sorted in non-decreasing order
    - First value of each row >= last value of previous row
    Determine if 'target' exists in the matrix.

    Approach:
    - Treat matrix as a flattened sorted array.
    - Use binary search on indices from 0 to m*n - 1.
    - Map mid index back to row and column: 
        row = mid // n, col = mid % n
    """

    if not matrix or not matrix[0]:
        return False

    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1

    while left <= right:
        mid = (left + right) // 2
        row, col = divmod(mid, n)  # same as row=mid//n, col=mid%n
        value = matrix[row][col]

        if value == target:
            return True
        elif value < target:
            left = mid + 1
        else:
            right = mid - 1

    return False


