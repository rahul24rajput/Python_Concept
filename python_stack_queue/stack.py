class Stack:
    def __init__(self):
        self.stack = []
        self.stack_size=0



    def enqueue(self,item):
        # print(self.stack_size )
        self.stack.append(item)
        self.stack_size = self.stack_size+1
        # print(self.stack_size )

    def dequeue(self):
        self.stack.pop(-1)
        self.stack_size = self.stack_size-1

    def get_stack_size(self):
        return self.stack_size
        

    def __str__(self):
        return "here is the stack {}".format(self.stack)
    

s = Stack()
s.enqueue(1)
s.enqueue(2)
s.enqueue(3)
s.enqueue(4)
s.enqueue(5)
print(s)
s.dequeue()
print(s.get_stack_size())

# print(s)