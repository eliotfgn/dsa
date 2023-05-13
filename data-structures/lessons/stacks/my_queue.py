class MyQueue:

    def __init__(self):
        self.queue = []
        # self.push_queue = []
        # self.pop_queue = []

    def push(self, x: int) -> None:
        self.queue.append(x)

    def pop(self) -> int:
        pop_queue = []
        for i in range(len(self.queue)):
            pop_queue.append(self.queue.pop())
        first = pop_queue.pop()
        self.queue = []
        for i in range(len(pop_queue)):
            self.queue.append(pop_queue.pop())
            
        return first

    def peek(self) -> int:
        if not self.empty():
            return self.queue[0]

    def empty(self) -> bool:
        return len(self.queue) == 0


# Your MyQueue object will be instantiated and called as such:


obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
param_2 = obj.pop()
param_3 = obj.peek()
param_4 = obj.empty()

print(param_2, param_3, param_4)
