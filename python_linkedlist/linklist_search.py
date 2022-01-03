class Node:
    def __init__(self,text):
        self.text = text
        self.next = None

class LinkedList:
    def __init__(self):
        selfhead = None


    def pt_lnklst(self):
        temp = self.head
        while(temp):
            print(temp.text)
            temp = temp.next

    def search_elem(self,elem):
        temp =  self.head
        while(temp):
            if temp.text== elem:
                return True
            temp = temp.next
        return False

    def del_elem_by_val(self,elem):

        if self.head.text == elem:
            self.head = self.head.next
            return self.head

        temp = self.head
        while(temp):
            if temp.text == elem:
                break
            prev = temp
            temp = temp.next
        if prev.next is not None:
            prev.next = temp.next
            temp = None
            return True
        else:
            return False

        


llist = LinkedList()
llist.head = Node(1)
snd = Node(2)
tnd = Node(3)
frnd = Node(4)
fivnd = Node(5)
llist.head.next = snd
snd.next = tnd
tnd.next = frnd
frnd.next = fivnd

# print(llist.search_elem(9))
print(llist.del_elem_by_val(6))

llist.pt_lnklst()
