class Node:
    def __init__(self, data):
        self.data = data
        self.addressOfNextNode = 0

class LinkedList:

    def __init__(self):
        self.head = 0
        self.tail = 0

    def insertNodeAtEnd(self, data):
        
        newNode = Node(data)

        if self.head == 0:
            self.head = self.tail = newNode

        else:
            self.tail.addressOfNextNode = newNode
            self.tail = newNode 

    def display(self):
        
        temp = self.head

        while temp != 0:
            print(temp.data)
            temp = temp.addressOfNextNode
        


l1 = LinkedList()
l1.insertNodeAtEnd(150)
l1.insertNodeAtEnd(200)
l1.insertNodeAtEnd(500)
l1.insertNodeAtEnd("hello")

l1.display()