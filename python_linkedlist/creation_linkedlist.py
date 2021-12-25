

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def print_list(self):
        temp = self.head
        while (temp):
            data=temp.data
            print(data)
            temp = temp.next



llist = LinkedList()
llist.head=Node(1)
second_node = Node(2)
third_node = Node(3)


llist.head.next = second_node

second_node.next = third_node
llist.print_list()