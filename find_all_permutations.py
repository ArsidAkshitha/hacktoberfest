from typing import List

def find_all_permutations(nums: List[int]) -> List[List[int]]:
    result = []
    n = len(nums)

    def backtrack(index: int):
        if index == n:
            result.append(list(nums))
            return

        for i in range(index, n):
            nums[index], nums[i] = nums[i], nums[index]
            backtrack(index + 1)
            nums[index], nums[i] = nums[i], nums[index]

    backtrack(0)
    return result
