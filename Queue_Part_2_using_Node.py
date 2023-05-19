
# In this program we will make a queue with help of Node.
# Isfull function won't be available.


class Node:
    def __init__(self, data):
        self.data = data # Input data to create a node
        self.next = None # Address of next node will "None" initally
        
class Queue:
    
    def __init__(self):
        self.queue = []  # python list will be used to store "Data (Node)"
        self.front = -1  # Initially value of front will be "None"
        self.rear = -1   # Initially value of rear will be "None"
        
    # isEmpty
    def isEmpty(self):
        return (self.front == -1) and (self.rear == -1)
        
    # peek
    def peek(self):
        return self.queue[self.front]
        
    # enqueue
    def enqueue(self, data):
        
        newNode = Node(data) # creating newNode
        
        if self.isEmpty(): # Checking if queue is Empty: ++ front and Rear
            self.queue.append(newNode)  # add new node from rear
            self.front += 1
            
        else:  # else queue has already some node in it, ++rear only
            old_Node = self.queue[self.rear]
            self.queue.append(newNode)
            old_Node.next = newNode
            
        self.rear += 1 
        
    # dequeue
    def dequeue(self):

        temp = self.peek().data # storing front element, to return the deleted element  
        
        if self.isEmpty(): # checking if queue is Empty: can't delete anything so raise exception
            raise Exception("Can't dequeue: Queue is Empty!")

        if self.front == self.rear: # special case: when front and rear are same, shift front and rear to -1
            self.rear = -1
            self.front = -1

            return print("deleted element: ",temp),temp
                
        else:  # In normal dequeue method element will be deleted from front so front will shift by +1
            self.front += 1

            return print("deleted element: ",temp),temp
          
    def display(self):
        
        if self.isEmpty():
            return -1
        
        while self.front <= self.rear:
            print(self.queue[self.front].data)
            self.front += 1
        
q1 = Queue()

q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)

q1.dequeue()

q1.display()



        