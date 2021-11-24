""" lc 225 - implement stack using queue

Implement a last-in-first-out (LIFO) stack using only two queues. 
The implemented stack should support all the 
functions of a normal stack (push, top, pop, and empty).
"""

class MyStack:

    def __init__(self):
        self.stack = []
        

    def push(self, x: int) -> None:
        self.stack.insert(0, x)
        for i, _ in enumerate(self.stack[:-1]):
            self.stack.insert(0, self.pop())


    def pop(self) -> int:
        return self.stack.pop() if self.stack else None
        

    def top(self) -> int:
        return self.stack[-1] if self.stack else None
        

    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
