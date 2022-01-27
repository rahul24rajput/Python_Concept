class Node :
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

    def remove_duplicate(self):

        temp = self.head
        hash = set()
        hash.add(temp.text)

        while(temp.next is not None):
            if temp.next.text in hash:
                temp.next = temp.next.next
            else:
                hash.add(temp.text)
                temp = temp.next
        
        return temp




llsit = LinkedList()

fst = Node(1)
snd = Node(2)
tnd = Node(3)
fnd = Node(4)
fvnd = Node(5)
sxnd = Node(2)
s7 = Node(3)
s8 = Node(8)

llsit.head = fst
llsit.head.next = snd
snd.next = tnd
tnd.next = fnd
fnd.next = fvnd
fvnd.next = sxnd
sxnd.next = s7
s7.next = s8
llsit.remove_duplicate()

llsit.pprint()