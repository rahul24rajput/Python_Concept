class Node:
    def __init__(self,text):
        self.text = text
        self.next = None

    
class LinkedList:
    def __init__(self):
        self.head = None

    

    def pprint(self):
        temp = self.head
        while(temp):
            print(temp.text)
            temp = temp.next

    def find_middle_node(self):
        fst  = self.head
        snd = self.head
        while (snd and snd.next is not None):
            fst = fst.next
            snd = snd.next.next
        print(fst.text)

llsit = LinkedList()
f1 = Node(1)
f2 = Node(2)
f3 = Node(3)
f4 = Node(4)
f5 = Node(5)
f6 = Node(6)



llsit.head = f1
f1.next = f2
f2.next = f3
f3.next = f4
f4.next = f5
f5.next = f6


llsit.find_middle_node()
# llsit.pprint()