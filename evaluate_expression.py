# Given a string representing a mathematical expression containing integers, parentheses, addition, and subtraction operators, evaluate and return the result of the expression.
def evaluate_expression(s: str) -> int:
    stack = []
    current_number = 0
    current_result = 0
    sign = 1  # +1 for positive, -1 for negative
    
    for char in s:
        if char.isdigit():
            current_number = current_number * 10 + int(char)
        elif char in ['+', '-']:
            current_result += sign * current_number
            sign = 1 if char == '+' else -1
            current_number = 0
        elif char == '(':
            # Push current result and sign for later
            stack.append(current_result)
            stack.append(sign)
            current_result = 0
            sign = 1
        elif char == ')':
            current_result += sign * current_number
            current_number = 0
            current_result *= stack.pop()  # sign
            current_result += stack.pop()  # previous result
        # ignore spaces
    
    # add any leftover number
    current_result += sign * current_number
    return current_result
