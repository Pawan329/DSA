
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Stack:
    
    counter = 0
    
    def __init__(self, size):
        
        self.size = size
        self.head = None
        self.tail = None
        
        if size <= 0:
            print("Size of stack should be more than 0 !")
        else:
            pass
        
        
    def isEmpty(self):
        if self.head is None:
            print("Stack is Empty !")
            return True
        else:
            return False
        
            
    def isFull(self):
        if self.counter == self.size:
            print("Stack is Full !")
            return True
        else:
            return False
            
    def insertElement(self, data):
        
        if self.isFull():
            print("Can't insert: Stack is Full !")
            return
        
        else:
            newNode = Node(data)
            
            if self.head == None:
                self.head = self.tail = newNode 
                
                self.counter += 1
                
            else:
                self.tail.next = newNode
                self.tail = newNode
               
                self.counter += 1
                
    def removeElement(self):
        count = 0
        temp = self.head
        
        if self.isEmpty():
            print("*** Stack is Empty ***")
            
        else:
            while temp != None:  # run loop till last node of LinkedList
                temp = temp.next  # traversing to LinkedList
                count += 1    # It will store the number of total nodes  
            current_node = self.head
            
            # It start with head node and traverse till second last node 
            # And make second last node as tail node
            
            for i in range(1, count):
                
                if i == count-1: # traverse till second last node of LinkedList
                    self.tail = current_node # here current node is second last node of LinkedList
                    current_node.next = None
                    
                    self.counter -= 1
                   
                else:
                    current_node = current_node.next # traversing till second last node of LinkedList
                
    def display(self):
            
        temp = self.head  # start traversing from head node

        while temp != None:
            print(temp.data)
            temp = temp.next
            
    
            
            
s1 = Stack(3)

s1.insertElement(10)
s1.insertElement(20)
s1.insertElement(30)
s1.display()
s1.insertElement(40)
s1.removeElement()
s1.display()
s1.insertElement(40)
s1.display()





        
    