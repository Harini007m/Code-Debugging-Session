# Problem6: Given a string containing '(', ')', '{', '}', '[' and ']', determine if the input is valid (all brackets are closed properly).

def is_balanced(s):
    stack = []
    mapping = {')':'(', '}':'{', ']':'['}
    for char in s:
        if char in mapping.values():
            stack.append(char)
        elif char in mapping.keys():
            if not stack or stack.pop() != mapping[char]:
                return False
    return not stack

print(is_balanced("()[]{}"))
print(is_balanced("(]"))
print(is_balanced("([)]"))  # nested different
print(is_balanced("((()))"))  # nested same
print(is_balanced("())"))  # extra closing
print(is_balanced("(()"))  # extra opening
print(is_balanced(""))  # empty
print(is_balanced("a(b)c"))  # with non-brackets
