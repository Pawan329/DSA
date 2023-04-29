class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoublyLinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        
    def insertNodeInBeg(self,data):
        newNode = Node(data) # creating new node with given data
        
        # If List is empty
        if self.head == None:
            self.head = self.tail = newNode

        else:
            temp = self.head # storing address of head node in temp variable
            newNode.next = temp
            newNode.prev = self.tail
            self.head = newNode
            temp.prev = newNode
            self.tail.next = newNode
            
    def insertNodeAtEnd(self, data):
        newNode = Node(data)
        
        if self.head == None:
            self.head = self.tail = newNode
            
        else:
            old_tail = self.tail
            newNode.prev = old_tail
            newNode.next = self.head
            self.tail = newNode
            self.tail.next = self.head
            old_tail.next = newNode
            self.head.prev = newNode
            
    def insertNodeAtRandomPos(self, data, pos):
        newNode = Node(data)
            
        if pos == 1:
            self.insertNodeInBeg(data)

        else:
            count = 1
            temp = self.head
            
            while temp.next != self.head:
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
        if self.head == None:
            print("Invalid operation: List is Empty!")
            
        else:
            new_head_node = self.head.next
            self.head = new_head_node
            new_head_node.prev = self.tail
            self.tail.next = self.head

    def delNodeFromEnd(self):
        
        if self.head == None:
            print("Invalid operation: Linked List is Empty!")
        
        else:
            self.tail = self.tail.prev
            self.tail.next = self.head
         
    def delNodeAtRandomPos(self, pos):
        
        if self.head == None:
            print("Invalid operation: : Linked List is Empty")
            
        elif pos == 1:
            self.delNodeFromBeg()
            
        else:
            count = 1
            temp = self.head
            
            while count != pos:
                if count == pos-1:
                    if temp.next == self.tail:
                        self.delNodeFromEnd()
                        break
                    else:
                        next_node = temp.next.next
                        next_node.prev = temp
                        temp.next = next_node
                        break
                    
                else:
                    temp = temp.next
                    count += 1
            
    def display(self):
        temp = self.head
        
        while temp.next != self.head :
            print(temp.data, end = " ")
            temp = temp.next
        if temp.next == self.head:
            print(temp.data, end = " ")
            
    def revDisplay(self):
        temp = self.tail
        # print("\n")
        while temp.prev != self.tail:
            
            print(temp.data, end = " ")
            temp = temp.prev
        if temp.prev == self.tail:
            print(temp.data, end = " ")

dll = DoublyLinkedList()

dll.insertNodeInBeg(30)
dll.insertNodeInBeg(20)
dll.insertNodeInBeg(10)
dll.insertNodeAtEnd("E1")
dll.insertNodeAtEnd("E2")
dll.insertNodeAtEnd("E3")
dll.insertNodeAtRandomPos("R1",2)
dll.insertNodeAtRandomPos("R2",4)
dll.insertNodeAtRandomPos("R3",8)


dll.display()
print("\n** Deleted node from End **")
dll.delNodeFromEnd()
dll.display()

print("\n** Delete 1st Position **")
dll.delNodeAtRandomPos(1)
dll.display()

print("\n** Delete 7th Position that is tail  **")
dll.delNodeAtRandomPos(7)
dll.display()

print("\n** Delete Node from Begining **")
dll.delNodeFromBeg()
dll.display()

print("\n** Reverse display **")
dll.revDisplay()