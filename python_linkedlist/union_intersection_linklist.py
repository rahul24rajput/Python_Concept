class Node:
    def __init__(self,text):
        self.text = text
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = None

    
    def pprint(self):
        temp = self.head
        while(temp):
            print(temp.text)
            temp = temp.next

    def push(self,text):
        new_node = Node(text)
        temp  = self.head 
        self.head  = new_node
        new_node.next = temp


def union(lst1,lst2):
    hash = set()
    # self.head = lst1
    print(lst2,"-----------------")
    while(lst1.next is not None):
        head = lst1
        if head.text not in hash:
            hash.add(head.text)
            head = head.next
        else:
            head = head.next
    while(lst1.next is not None):
        head2 = lst2
        if head2.text not in hash:
            hash.add(head2.text)
            head2 = head2.next
        else:
            head2 = head2.next




a = Linkedlist()
b = Linkedlist()

a.push(1)
a.push(2)
a.push(3)
a.push(4)
a.push(5)
a.push(6)

b.push(7)
b.push(8)
b.push(9)
b.push(10)
b.push(1)
b.push(2)

print(a.next)

# union(a,b)
        