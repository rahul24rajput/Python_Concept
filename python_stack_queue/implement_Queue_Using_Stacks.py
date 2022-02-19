class Stack:
    def __init__(self):
        self.stc_list = []
        self.stc_length = 0


    @property
    def get_length(self):
        return self.stc_length

    def sts_enq(self,item):
        self.stc_length = self.stc_length+1
        return  self.stc_list.append(item)

    def stc_deq(self,item):
        self.stc_length = self.stc_length-1
        return self.stc_list.pop(-1)
    
    def __str__(self):
        return "stack is {}".format(self.stc_list)

    def __iter__(self):
        return self

    def __next__(self):
        if self.stc_list:
            return self.stc_list.pop(-1)
        raise StopIteration

s = Stack()
s2 = Stack()

s.sts_enq(1)
s.sts_enq(2)
s.sts_enq(3)
s.sts_enq(4)
s.sts_enq(5)
s.sts_enq(6)
s.sts_enq(7)
lent = s.get_length
print(s)

for i in s:
    s2.sts_enq(i)

print(s2)
print(s)