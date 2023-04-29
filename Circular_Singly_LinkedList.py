class Node:
    
    #Creating Node
    def __init__(self, data):
        self.data = data            # Data Node will hold
        self.next = None  # Node hold the address of next node

class LinkedList:

    def __init__(self):
        self.head = None               # Initializing head with data = None
        self.tail = None               # Initializing tail with data = None

    # Insering new node at End of LL
    def insertNodeAtEnd(self, data):
        
        newNode = Node(data)        # Creating new Node with user provided data

        if self.head == None:
            self.head = self.tail = newNode  # When there is no node Head and Tail will be the same node
            self.tail.next = self.head

        else:
            newNode.next = self.head  # connecting newNode with head node
            self.tail.next = newNode  # If LL has more one or more node tail will hold address if new inserted node
            self.tail = newNode  # New tail node assignment

    def insertNodeInBeg(self, data):
        newNode = Node(data)
        
        if self.head == None:
            self.head = self.tail = newNode
            
        else:
            newNode.next = self.head
            self.head = newNode
            self.tail.next = newNode
    
    def delNodeFromEnd(self):
        count = None
        temp = self.head
        
        if self.head == None:
            print("Invalid Operation: Linked List is empty!")
            
        else:
            
            while temp != self.tail:  
                if temp.next == self.tail:
                    self.tail = temp
                    self.tail.next = self.head
                
                    break
                else:
                    temp = temp.next
            
    def delNodeFromBeg(self):
        
        if self.head == None:
            print("Invalid Operation: Linked List is empty!")
        
        else:
            self.head = self.head.next
            self.tail.next = self.head
    
    def delNodeAtRandomPos(self, pos): # pos will take position of node that need to deleted
        
        current_node = 1  # considering first node as 1
        temp = self.head  # storing address of head node 
        
        if pos == 1:
            self.delNodeFromBeg()
        
        else:
            while temp != self.tail:  # run loop till second last node of linked list
                
                if current_node == pos-1:  # stop node before 1 node before that need to be deleted
                    temp.next = temp.next.next  # skip one node
                    break 
                    
                else:
                    current_node += 1
                    temp = temp.next  # traversing linked list using temp variable
            
    def insertNodeAtRandomPos(self, pos, data):
        
        newNode = Node(data) # creating new node
        flag = 0 # Make flag = 1 when found the valid position 
        
        # when need to insert new node before head node
        if pos == 1:   
          self.insertNodeInBeg(data)
            
        # when newNode to be insert other than 1st place    
        else:
            temp = self.head # storing head node address in temp variable
            current_node = 1
            
            while temp != self.tail:
                
                if current_node == pos-1: # if current node is one less of target node
                    newNode.next = temp.next
                    temp.next = newNode
                    flag = 1
                    break
                
                else:
                    temp = temp.next  # traversing LinkedList using temp variable
                    current_node += 1
            
            if flag == 0: # asked position is not found in list
                print("Invalid Pos!!")    
                
        
    def display(self):
        temp = self.head  # start traversing from head node

        while temp != self.tail:
            print(temp.data, end=" ")
            temp = temp.next
            
        print(self.tail.data, end=" ") 
        


l1 = LinkedList()
l1.insertNodeAtEnd(100)
l1.insertNodeAtEnd(200)
l1.insertNodeAtEnd(300)
l1.insertNodeAtEnd(400)
l1.insertNodeInBeg("B4")
l1.insertNodeInBeg("B3")
l1.insertNodeInBeg("B2")
l1.insertNodeInBeg("B1")

l1.display() # display all nodes before execution of any function

print("\n*** Insert node at 2nd position ***")
l1.insertNodeAtRandomPos(2, "NewNode")
l1.display()

print("\n*** Delete 3rd node ***")
l1.delNodeAtRandomPos(3)
l1.display()

print("\n*** Delete last node ***")
l1.delNodeFromEnd()
l1.display()

print("\n*** Delete 1st node ***")
l1.delNodeFromBeg()
l1.display() # display all nodes after execution of any function


