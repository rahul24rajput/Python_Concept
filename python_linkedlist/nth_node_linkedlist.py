class Node:
    def __init__(self,text):
        self.text = text
        self.next = None


class LinkedList:
    def __init__(self):
        self.head =  None


    def pprint(self):
        temp = self.head
        while(temp):
            print(temp.text)
            temp = temp.next


    def nth_num(self,index):
        self.index = index
        self.count = 0 
        temp = self.head
        while(self.count!=self.index):
            self.count = self.count+1
            # print(self.count,'------------')
            temp = temp.next
        print(temp.text)



llist = LinkedList()

f1 = Node(1)
f2 = Node(2)
f3 = Node(3)
f4 = Node(4)
f5 = Node(5)
f6 = Node(6)

llist.head = f1
llist.head.next = f2
f2.next = f3
f3.next = f4
f4.next = f5
f5.next = f6
 
llist.nth_num(3)
# llist.pprint()