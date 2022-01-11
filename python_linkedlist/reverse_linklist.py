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


    def reverse(self):
        prev = None
        curr = self.head

        while(curr is not None):
            next = curr.next
            curr.next = prev 
            prev = curr
            curr = next
        self.head = prev


llist = LinkedList()
fst  = Node(1)
snd = Node(2)
tnd = Node(3)
fnd  = Node(4)
fvnd = Node(5)
sxnd = Node(4)
llist.head = fst
llist.head.next = snd

snd.next = tnd
tnd.next = fnd
fnd.next = fvnd
fvnd.next = sxnd

# llist.reverse()
llist.pprint()