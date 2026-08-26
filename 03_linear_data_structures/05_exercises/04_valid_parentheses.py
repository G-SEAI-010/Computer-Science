# Lösung 1 - Zeit O(n), Speicher O(n)


def is_valid(string):
    if len(string) % 2 != 0:
        return False

    stack = []
    mapping = {")": "(", "}": "{", "]": "["}

    for char in string:
        if char in mapping:
            top_element = stack.pop() if stack else "#"
            if mapping[char] != top_element:
                return False
        else:
            stack.append(char)

    return not stack


print(is_valid("()"))  # True
# '(' → pushen → stack: ['(']
# ')' → pop '(' → entspricht matching[')']='(' ✓ → stack: []
# Ende: stack ist leer → True

print(is_valid("()[]{}"))  # True
# Jedes Paar öffnet und schließt sauber, der Stack ist am Ende leer

print(is_valid("(]"))  # False
# '(' → pushen → stack: ['(']
# ']' → pop '(' → matching[']']='[' aber haben '(' bekommen ✗ → return False

print(is_valid("([])"))  # True
# '(' → pushen → stack: ['(']
# '[' → pushen → stack: ['(', '[']
# ']' → pop '[' → matching[']']='[' ✓ → stack: ['(']
# ')' → pop '(' → matching[')']='(' ✓ → stack: []
# Ende: stack ist leer → True
