# Given a string, continually perform the following operation: remove a pair of adjacent duplicates from the string. Continue performing this operation until the string no longer contains pairs of adjacent duplicates. Return the final string.
def repeated_removal_of_adjacent_duplicates(s: str) -> str:
    stack = []
    
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()  # remove adjacent duplicate
        else:
            stack.append(char)
    
    return "".join(stack)
