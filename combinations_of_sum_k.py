from typing import List

def combinations_of_sum_k(nums: List[int], target: int) -> List[List[int]]:
    result = []
    
    nums.sort() 

    def backtrack(remaining: int, start_index: int, current_combination: List[int]):
        if remaining == 0:
            result.append(list(current_combination))
            return

        if remaining < 0:
            return

        for i in range(start_index, len(nums)):
            candidate = nums[i]
            current_combination.append(candidate)
            
            backtrack(remaining - candidate, i, current_combination)
            
            current_combination.pop()

    backtrack(target, 0, [])
    return result
