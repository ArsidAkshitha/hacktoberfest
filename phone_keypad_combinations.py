from typing import List

def phone_keypad_combinations(digits: str) -> List[str]:
    if not digits:
        return []

    mapping = {
        '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', 
        '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
    }

    result = []
    
    def backtrack(index, path):
        if index == len(digits):
            result.append("".join(path))
            return

        digit = digits[index]
        letters = mapping[digit]

        for letter in letters:
            path.append(letter)
            backtrack(index + 1, path)
            path.pop()

    backtrack(0, [])
    return result
