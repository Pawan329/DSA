class Queue:
    # Initialization
    def __init__(self, size):
        self.size = size
        self.front = -1
        self.rear = -1
        self.queue = []
        
    # isFull
    def isFull(self):
        if self.rear == self.size-1:
            raise Exception("Queue is full!")
    
    # isEmpty
    def isEmpty(self):
        return (self.front == -1) and (self.rear == -1)
            
    # enqueue
    def enqueue(self, data):
        
        #check if Queue is full or not
        if self.isFull():
            raise Exception("Can't Enqueue: Queue is full.")
        
        elif self.isEmpty():
            self.queue.append(data)
            self.front += 1
            self.rear += 1
    
        else:
            self.queue.append(data)
            self.rear += 1
            
    # dequeue
    def dequeue(self):
        
        #check if Queue is Empty or not
        if self.isEmpty():
            raise Exception("Can't dequeue: Queue is Empty.")
            
        elif self.front == self.rear:
            self.front = -1
            self.rear = -1
            
        else:
            self.front += 1 
            
    # peek
    def peek(self):
        if self.isEmpty():
            return -1
            
        else:
            return self.queue[self.front]
    
    #display
    def display(self):
        if self.isEmpty():
            print("queue is Empty!")
            return -1
        
        else:
            temp = self.front
            while temp <= self.rear:
                print(self.queue[temp], end = " ")
            
                temp += 1
    
q1 = Queue(5)
q1.enqueue("A")
q1.enqueue("B")
q1.enqueue("C")
q1.enqueue("D")
q1.enqueue("E")
q1.dequeue()
q1.dequeue()
q1.dequeue()
q1.dequeue()
print(q1.peek())
# q1.enqueue("new")
# q1.enqueue("F")
q1.display()  