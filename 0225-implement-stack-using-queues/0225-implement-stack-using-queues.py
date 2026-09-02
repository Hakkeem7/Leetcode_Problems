class MyStack:

    def __init__(self):
        self.q1 = []
        self.q2 = []

    def push(self, x):

        # Put new element into q2
        self.q2.append(x)

        # Move all elements from q1 to q2
        while len(self.q1) > 0:
            self.q2.append(self.q1.pop(0))

        # Swap q1 and q2
        self.q1, self.q2 = self.q2, self.q1

    def pop(self):
        return self.q1.pop(0)

    def top(self):
        return self.q1[0]

    def empty(self):
        return len(self.q1) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()




    