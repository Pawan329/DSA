class Node:
    
    #Creating Node
    def __init__(self, data):
        self.data = data            # Data Node will hold
        self.addressOfNextNode = 0  # Node hold the address of next node

class LinkedList:

    def __init__(self):
        self.head = 0               # Initializing head with data = 0
        self.tail = 0               # Initializing tail with data = 0

    # Insering new node at End of LL
    def insertNodeAtEnd(self, data):
        
        newNode = Node(data)        # Creating new Node with user provided data

        if self.head == 0:
            self.head = self.tail = newNode  # When there is no node Head and Tail will be the same node

        else:
            self.tail.addressOfNextNode = newNode  # If LL has more one or more node tail will hold address if new inserted node
            self.tail = newNode  # New tail node assignment

    def insertNodeInBeg(self, data):
        newNode = Node(data)
        
        if self.head == 0:
            self.head = self.tail = newNode
            
        else:
            temp = self.head  # Storing address of head to temp variable
            self.head = newNode  # making newNode as head node
            self.head.addressOfNextNode = temp # assigning old head address to next node of current head
    
    def delNodeFromEnd(self):
        count = 0
        temp = self.head
        
        if self.head == 0:
            print("Invalid Operation: Linked List is empty!")
            
        else:
            while temp != 0:  # run loop till last node of LinkedList
                temp = temp.addressOfNextNode  # traversing to LinkedList
                count += 1    # It will store the number of total nodes  
            
            current_node = self.head
            
            # It start with head node and traverse till second last node 
            # And make second last node as tail node
            
            for i in range(1, count):
                
                if i == count-1: # traverse till second last node of LinkedList
                    self.tail = current_node # here current node is second last node of LinkedList
                    current_node.addressOfNextNode = 0
                   
                else:
                    current_node = current_node.addressOfNextNode # traversing till second last node of LinkedList
            
    def delNodeFromBeg(self):
        
        if self.head == 0:
            print("Invalid Operation: Linked List is empty!")
        
        else:
            self.head = self.head.addressOfNextNode
    
    def delNodeAtRandomPos(self, pos): # pos will take position of node that need to deleted
        delete_node = pos
        current_node = 1  # considering first node as 1
        
        temp = self.head  # storing address of head node 
        
        if delete_node == 1:
            self.head = self.head.addressOfNextNode # to deleted head node making next node of head as head node
        
        else:
            while temp.addressOfNextNode != 0:  # run loop till second last node of linked list
                
                if current_node == delete_node-1:  # stop node before 1 node before that need to be deleted
                    temp.addressOfNextNode = temp.addressOfNextNode.addressOfNextNode  # skip one node
                    current_node += 1  
                    
                else:
                    current_node += 1
                    temp = temp.addressOfNextNode  # traversing linked list using temp variable
            
    def insertNodeAtRandomPos(self, pos, data):
        
        newNode = Node(data) # creating new node
        current_node = 1
        
        # when need to insert new node before head node
        if pos == 1:   
            temp = self.head  # storing head node address in temp variable
            self.head = newNode # making newNode as head node
            newNode.addressOfNextNode = temp # making old head node as next node of newNode
            
        # when newNode to be insert other than 1st place    
        else:
            temp = self.head # storing head node address in temp variable
            while temp.addressOfNextNode != 0:
                
                if current_node == pos-1: # if current node is one less of target node
                    temp1 = temp.addressOfNextNode  
                    temp.addressOfNextNode = newNode  # insert newNode at target position
                    newNode.addressOfNextNode = temp1 # assigning address of old node after newNode
                    break
                
                else:
                    temp = temp.addressOfNextNode  # traversing LinkedList using temp variable
                    
                current_node += 1
                
            # In case target node is last node of LinkedList    
            if temp.addressOfNextNode == 0:
                temp.addressOfNextNode = newNode # Insering newNode as last node of LinkedList
                newNode.addressOfNextNode = 0  # addressOfNextNode should be 0 after last node
        
    
    def display(self):
        temp = self.head  # start traversing from head node

        while temp != 0:
            print(temp.data)
            temp = temp.addressOfNextNode
        


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

# l1.insertNodeAtRandomPos(9, "NewNode")
# l1.delNodeAtRandomPos(8)
l1.delNodeFromEnd()
# l1.delNodeFromBeg()

l1.display() # display all nodes after execution of any function