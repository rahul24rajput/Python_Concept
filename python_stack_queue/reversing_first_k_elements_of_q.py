class Stack:
    def __init__(self):
        self.stack = []
        self.size =0
    
    
    def enq_stc(self,item):
        self.size = self.size+1
        return  self.stack.append(item)

    def deq_stc(self):
        self.size = self.size-1
        return self.stack.pop(-1)

    def __str__(self):
        return "the stack is {}".format(self.stack)


class Queue:
    def __init__(self):
        self.queue = []
        self.size =0
    
    
    def enq_q(self,item):
        self.size = self.size+1
        return self.queue.append(item)

    def deq_q(self):
        self.size = self.size-1
        return self.queue.pop(0)

    @property
    def q_size(self):
        return  self.size

    def __iter__(self):
        return self

    def __next__(self):
        if self.queue:
            return self.queue.pop(0)
        raise StopIteration

    def __str__(self):
        return "the queue is {}".format(self.queue)


q = Queue()
q2=Queue()
s = Stack()
q.enq_q(1)
q.enq_q(2)
q.enq_q(3)
q.enq_q(4)
q.enq_q(5)
q.enq_q(6)
q.enq_q(7)
q.enq_q(8)
q.enq_q(9)
q.enq_q(10)
# print(q)
# print(q.q_size)

item = 4

# Here is some mistake in the  for loop so run the lopp in the object directly as i have implemented the iteratoe in it, 
# same can be seen in the next file about implement_q_using _stack

for i in range(q.q_size):
    if i==item:
        break
    # print(q.deq_q())
    s.enq_stc(q.deq_q())

print(s)
print(q)

for i in range(item):
    # print(s.deq_stc())
    q2.enq_q(s.deq_stc())

for i in q:
    q2.enq_q(i)

print(q2)