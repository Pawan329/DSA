class Node:
    def __init__(self, data):
        self.data = data
        self.next = 0
        self.prev = 0
        
class DoublyLinkedList:
    
    def __init__(self):
        self.head = 0
        self.tail = 0
        
    def insertNodeInBeg(self,data):
        newNode = Node(data) # creating new node with given data
        
        # If List is empty
        if self.head == 0:
            self.head = self.tail = newNode

        else:
            temp = self.head # storing address of head node in temp variable
            newNode.next = temp
            self.head = newNode
            temp.prev = newNode
            
    def insertNodeAtEnd(self, data):
        newNode = Node(data)
        
        if self.head == 0:
            self.head = self.tail = newNode
            
        else:
            old_tail_next = self.tail.next
            old_tail = self.tail
            self.tail.next = newNode
            newNode.prev = old_tail
            self.tail = newNode
       
    def insertNodeAtRandomPos(self, data, pos):
        newNode = Node(data)
            
        if pos == 1:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
            
        else:
            count = 1
            temp = self.head
            
            while temp != 0:
                temp_next = temp.next
                current_temp = temp
                
                if count == pos-1:
                    temp_next.prev = newNode
                    temp.next = newNode
                    newNode.next = temp_next
                    newNode.prev = current_temp
                    
                    break
                
                else:
                    temp = temp.next
                    count += 1
    
    def delNodeFromBeg(self):
        if self.head == 0:
            print("Invalid operation: List is Empty!")
            
        else:
            self.head = self.head.next
            self.head.prev = 0
     
    def delNodeFromEnd(self):
        
        if self.head == 0:
            print("Invalid operation: Linked List is Empty!")
        
        else:
            self.tail = self.tail.prev
            self.tail.next = 0
         
    def delNodeAtRandomPos(self, pos):
        
        if self.head == 0:
            print("Invalid operation: : Linked List is Empty")
            
        elif pos == 1:
            self.head = self.head.next
            self.head.prev = 0
            
        else:
            count = 1
            temp = self.head
            
            while count != pos:
                if count == pos-1:
                    next_node = temp.next.next
                    next_node.prev = temp
                    temp.next = next_node
                    break
                    
                else:
                    temp = temp.next
                    count += 1
            
    def display(self):
        temp = self.head
        
        while temp != 0:
            print(temp.data)
            temp = temp.next
            
    def revDisplay(self):
        temp = self.tail
        
        while temp != 0:
            print(temp.data)
            temp = temp.prev
        

dll = DoublyLinkedList()

dll.insertNodeInBeg(30)
dll.insertNodeInBeg(20)
dll.insertNodeInBeg(10)
dll.insertNodeAtEnd("E1")
dll.insertNodeAtEnd("E2")
dll.insertNodeAtEnd("E3")
dll.insertNodeAtRandomPos("R1",1)
dll.insertNodeAtRandomPos("R2",2)
dll.insertNodeAtRandomPos("R3",3)


dll.display()
print("** Deleted node from End **")
dll.delNodeFromEnd()
dll.display()

print("** Delete 1st Position **")
dll.delNodeAtRandomPos(1)
dll.display()

print("** Delete 3rd Position **")
dll.delNodeAtRandomPos(3)
dll.display()

print("** Delete Node from Begining **")
dll.delNodeFromBeg()
dll.display()

print("** Reverse display **")
dll.revDisplay()





