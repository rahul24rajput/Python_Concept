class Node:
    def __init__(self,text):
        self.text = text
        self.next = None



class LinkedList:
    def __init__(self):
        self.head = None


    def pprint(self):
        temp =self.head
        while(temp):
            print(temp.text)
            temp=temp.next

    def detectLoop(self):
        hst= self.head
        fst = self.head

        while(fst and hst and fst.next):
            hst = hst.next
            fst = fst.next.next
            if hst == fst:
                return True

llist = LinkedList()
# llist.head = Node(1)
# llist.head.next = Node(2)
# llist.head.next.next = Node(3)
# llist.head.next.next.next = Node(4)
# llist.head.next.next.next.next = Node(5)
 
# Create a loop for testing(5 is pointing to 3)
# llist.head.next.next.next.next.next = llist.head.next.next
fst = Node(1)
snd = Node(2)
tnd = Node(3)
frt = Node(4)
fvt = Node(5)
sxnd = Node(6)

llist.head = fst
llist.head.next = snd
snd.next = tnd
tnd.next = frt
frt.next = fvt
fvt.next = snd

if(llist.detectLoop()):
    print ("Found Loop")
else:
    print ("No Loop")
# llist.pprint()