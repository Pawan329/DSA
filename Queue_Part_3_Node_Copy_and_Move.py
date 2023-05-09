''' 
In this program we will make a queue with help of Node.
Isfull function won't be available.
'''

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
        if self.isEmpty():
            return -1
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
        
        if self.isEmpty(): # checking if queue is Empty: can't delete anything so raise exception
            raise Exception("Can't dequeue: Queue is Empty!")
            
        elif self.front == self.rear: # special case: when front and rear are same, shift front and rear to -1
            self.rear = -1
            self.front = -1
                
        else:  # In normal dequeue method element will be deleted from front so front will shift by +1
            self.front += 1
          
    def display(self):
        
        if self.isEmpty():
            return (print("Empty!")),-1
            
        front = self.front  # storing in local variable because it was changing actual value of front and rear, becoming hurdle in next function
        rear = self.rear
        
        while front <= rear:
            print(self.queue[front].data)
            front += 1
        
    def copyTo(self,q2):

        front = self.front
        rear = self.rear
        
        while front <= rear:
            q2.enqueue((self.queue[front]).data)
            front += 1
        
        
    def moveTo(self,target):

        front = self.front
        rear = self.rear
        
        while front <= rear:
            target.enqueue((self.queue[front]).data)
            front += 1
            self.dequeue()
        
q1 = Queue()

q1.enqueue(1)
q1.enqueue(2)
q1.enqueue(3)
q1.enqueue(4)
q1.enqueue(5)

q2 = Queue()
# q1.copyTo(q2)

print("*Display q1*")
q1.display()
print("*Display q2*")
q2.display()

print("*Move q1 to q2*")
q1.moveTo(q2)
print("*Display q1*")
q1.display()
print("*Display q2*")
q2.display()

print("*Move q2 to q1*")
q2.moveTo(q1)
print("*Display q1*")
q1.display()
print("*Display q2*")
q2.display()

print("*Copy q1 to q2*")
q1.copyTo(q2)
print("*Display q1*")
q1.display()
print("*Display q2*")
q2.display()


        

