class Queue:
    def __init__(self):
        self.list = []


    def enqueue(self,item):
        self.list.append(item)

    def dequeue(self):
        self.list.pop(0)

    def __str__(self):
        return "here is the queue {}".format(self.list)
    

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)
q.enqueue(5)
print(q)
q.dequeue()


print(q)