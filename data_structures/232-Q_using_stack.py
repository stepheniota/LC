""" lc 232 - implement Q using stacks

Implement a first in first out (FIFO) queue using only two stacks. 
The implemented queue should support all the functions of a 
normal queue (push, peek, pop, and empty).
"""

class MyQueue:

    def __init__(self):
        self.q = []


    def push(self, x: int) -> None:
        tmp = []
        while self.q:
            tmp.append(self.q.pop())
        self.q.append(x)
        while tmp:
            self.q.append(tmp.pop())


    def pop(self) -> int:
        return self.q.pop() if not self.empty() else None


    def peek(self) -> int:
        return self.q[-1] if not self.empty() else None


    def empty(self) -> bool:
        return len(self.q) == 0



if __name__ == '__main__':
    pass
    # Your MyQueue object will be instantiated and called as such:
    # obj = MyQueue()
    # obj.push(x)
    # param_2 = obj.pop()
    # param_3 = obj.peek()
    # param_4 = obj.empty()

