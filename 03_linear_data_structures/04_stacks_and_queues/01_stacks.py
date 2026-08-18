class Stack:
    def __init__(self):
        self.items = []

    def __str__(self):
        return f"Stack({self.items})"

    def push(self, item):
        """Add an element to the top of the stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return the top element of the stack."""
        if self.is_empty():
            return None  # or raise an exception
        return self.items.pop()

    def peek(self):
        """Return the top element without removing it."""
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        """Check if the stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return the number of elements in the stack."""
        return len(self.items)


# Example usage:
stack = Stack()
stack.push(10)
stack.push(20)
print("Top element:", stack.peek())  # Output: Top element: 20
print("Pop element:", stack.pop())  # Output: Pop element: 20
print("Is empty?", stack.is_empty())  # Output: Is empty? False
print("Stack size:", stack.size())  # Output: Stack size: 1
print(stack)
