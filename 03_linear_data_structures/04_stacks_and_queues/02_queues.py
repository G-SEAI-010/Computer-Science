class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        """Insert an element at the rear of the queue."""
        self.queue.append(element)

    def dequeue(self):
        """Remove and return the element at the front of the queue."""
        if self.isEmpty():
            return "Queue is empty"
        return self.queue.pop(0)

    def peek(self):
        """Return the front element without removing it."""
        if self.isEmpty():
            return "Queue is empty"
        return self.queue[0]

    def isEmpty(self):
        """Check if the queue is empty."""
        return len(self.queue) == 0

    def size(self):
        """Return the number of elements in the queue."""
        return len(self.queue)


# Example usage
myQueue = Queue()

myQueue.enqueue("A")
myQueue.enqueue("B")
myQueue.enqueue("C")
print("Queue:", myQueue.queue)  # ['A', 'B', 'C']
print("Dequeue:", myQueue.dequeue())  # 'A' (removes 'A')
print("Peek:", myQueue.peek())  # 'B' (front element, not removed)
print("isEmpty:", myQueue.isEmpty())  # False
print("Size:", myQueue.size())  # 2

print()

from collections import deque

my_queue = deque()
my_queue.append("A")
my_queue.append("B")
my_queue.append("C")
print("queue:", my_queue)
print("peek:", my_queue[0])  # front without removing
print("dequeue:", my_queue.popleft())  # remove from front — O(1)
print("size:", len(my_queue))
print("is empty:", len(my_queue) == 0)
print("queue after dequeue:", my_queue)
