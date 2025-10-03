# Implement a Queue using Stacks Medium Implement a queue using the stack data structure. Include the following functions: enqueue(x: int) -> None: adds x to the end of the queue. dequeue() -> int: removes and returns the element from the front of the queue. peek() -> int: returns the front element of the queue. You may not use any other data structures to implement the queue.
class Queue:
    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def enqueue(self, x: int) -> None:
        self.stack_in.append(x)

    def dequeue(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out.pop() if self.stack_out else None

    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1] if self.stack_out else None
