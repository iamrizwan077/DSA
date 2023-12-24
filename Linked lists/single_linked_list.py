class Node():
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList():
    def __init__(self) -> None:
        self.head = None

    def insertAtBegin(self, data):
        node = Node(data)

        if self.head == None:
            self.head = node
        
        else:
            node.next = self.head
            self.head = node
    
    def insertAtEnd(self, data):
        node2 = Node(data)
        node1 = self.head

        if self.head == None:
            self.head = node2
        else:
            while node1.next != None:
                node1 = node1.next
            node1.next = node2

    def insertAtIndex(self, index, data):
        node2 = Node(data)
        i = 0
        node1 = self.head

        while i < index and node1.next != None:
            i+=1
            node1 = node1.next

        node2.next = node1.next
        node1.next = node2

    def printList(self):
        node = self.head
        print(node.data, end = " ")
        
        while node.next != None:
            node = node.next
            print(node.data, end = " ")
        print("\n")

    def removeFromBegin(self):
        if self.head is None:
            print("List is already empty")
        else:
            if self.head.next is None:
                del self.head
            else:
                temp = self.head
                self.head = self.head.next
                del temp

    def removeFromEnd(self):
        if self.head is None:
            print("List is already empty")
        else:
            if self.head.next is None:
                del self.head
            else:
                node = self.head
                while node.next.next != None:
                    node = node.next
                temp = node.next
                node.next = None
                del temp

    def removeFromIndex(self, index):

        i = 0

        node = self.head
        temp = self.head
        while i < index -1 and node.next.next != None:
            i+=1
            node = node.next
        temp = node.next
        node.next = node.next.next
        del temp

    def reverseList(self):
        current = self.head
        prev = None
        while current != None:
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev


llist = LinkedList()

llist.insertAtBegin(1)
llist.insertAtIndex(1, 2)
llist.insertAtIndex(2, 3)
llist.insertAtIndex(3, 4)
llist.insertAtEnd(5)

print("After Insertion")

llist.printList()

llist.removeFromBegin()
llist.removeFromIndex(2)
llist.removeFromEnd()

print("After Deletion")

llist.printList()

llist2 = LinkedList()

llist2.insertAtBegin(1)
llist2.insertAtIndex(1, 2)
llist2.insertAtIndex(2, 3)
llist2.insertAtIndex(3, 4)
llist2.insertAtEnd(5)

llist2.reverseList()

print("After Reverse")

llist2.printList()




            

