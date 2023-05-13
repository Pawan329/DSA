class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.queue = [None] * size
        
    #isEmpty
    def isEmpty(self):
        return (self.front == -1) and (self.rear == -1) # Return True when front and rear both are -1
        
    #isFull
    def isFull(self):
        return (self.rear+1) % self.size == self.front  # Return True when next index of front is rear that mean Queue is full
    
    #peek
    def peek(self):
        return self.queue[self.front]  # return current first element of queue
        
    #enqueue - adding elements to queue
    def enqueue(self, data):
        
        if self.isFull():
            raise Exception("Can't Enqueue: QUEUE is FULL!")
            
        if (self.front == -1) and (self.rear == -1):  # if front and rear both are at -1 in this case increment front with +1
            self.front += 1 # incase of fist element of queue need increment front also after insert
        
        self.queue[(self.rear+1) % self.size] = data # insert new element in next place of existing front
        self.rear = (self.rear+1) % self.size  # Move rear element with +1
     
        
    #dequeue - deleted element from front of queue
    def dequeue(self):
        
        temp_front = self.queue[self.front]  # to return deleted element
        
        if self.isEmpty():
            raise Exception("Can't Dequeue: QUEUE is Empty!")
        
        if self.front == self.rear: # when queue has only only one element, reset front and rear element with -1
            self.queue[self.front] = self.queue[self.rear] = None
            self.front = self.rear = -1
            
            
        else:
            self.queue[self.front] = None
            self.front = (self.front+1) % self.size
        
        return temp_front  # returing deleted element
        
    
    #display
    def display(self):
        
        if self.isEmpty():
            return -1, print(self.queue)
            
        else:
            print(self.queue)
        
    
cq = CircularQueue(6)
cq.display()

cq.enqueue(10)
cq.enqueue(20)
cq.enqueue(30)
cq.enqueue(40)
cq.enqueue(50)
cq.enqueue(60)

cq.display()

cq.dequeue()
cq.dequeue()
cq.dequeue()
cq.display()

cq.enqueue("A")
cq.display()

cq.enqueue("B")
cq.display()

cq.enqueue("C")
cq.display()


cq.dequeue()
cq.display()

cq.dequeue()
cq.display()

cq.dequeue()
cq.display()

cq.dequeue()
cq.display()

cq.dequeue()
cq.display()

cq.dequeue()
cq.display()

cq.enqueue("X")
cq.display()

print(cq.front)
print(cq.rear)

cq.dequeue()
cq.display()

cq.enqueue("Y")
cq.display()

print(cq.front)
print(cq.rear)

cq.enqueue("Z")
cq.display()

print(cq.front)
print(cq.rear)







    
    
    
    
    
    
    
    
    