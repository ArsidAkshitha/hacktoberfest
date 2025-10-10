from typing import List

def find_all_subsets(nums: List[int]) -> List[List[int]]:
    result = []
    
    def backtrack(index: int, current_subset: List[int]):
        result.append(list(current_subset))
        
        for i in range(index, len(nums)):
            current_subset.append(nums[i])
            backtrack(i + 1, current_subset)
            current_subset.pop()

    backtrack(0, [])
    return result
