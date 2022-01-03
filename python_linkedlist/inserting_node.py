class Node:
    def __init__(self,text):
        self.text = text
        self.next=None



class LinkedList:
    def __init__(self):
        self.head = None


    def print_lst(self):
        temp=self.head
        while(temp):
            print(temp.text)
            temp=temp.next


    def insert_at_start(self,data):
        new_node= Node(data)
        temp = self.head
        self.head = new_node
        new_node.next = temp


    def insert_at_middle(self,prv_nd,data):
        if prv_nd.next is None:
            return "Node is not in  linklist"
        md_node = Node(data)  
        md_node.next = prv_nd.next
        prv_nd.next = md_node
    
    def insert_At_last(self,data):
        nw_node = Node(data)
        temp = self.head
        while(temp.next):
            temp = temp.next

        temp.next = nw_node 



llist = LinkedList()
llist.head = Node(1)
snd = Node(2)
tnd=Node(3)
f4nd=Node(4)

llist.head.next = snd
snd.next=tnd
tnd.next=f4nd
llist.insert_at_start(5)
llist.insert_at_middle(tnd,6)
llist.insert_At_last(7)
llist.insert_At_last(8)

llist.print_lst()
