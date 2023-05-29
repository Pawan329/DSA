class Stack:
    
    def __init__(self, size):
        self.size = size
        self.stack = []
        self.top = -1
        
    def isEmpty(self):
        return self.top == -1
        
    def isFull(self):
        return (self.top == self.size-1)
        
    def peek(self):
        if self.isEmpty():
            raise Exception("Queue is Empty")
        
        return self.stack[self.top]  
        
        
    def push(self, data):
        
        if self.isFull():
            raise Exception("Can't Push: Queue is full")
        else:
            self.stack.append(data)
            self.top += 1
        
    def pop(self):
        
        if self.isEmpty():
            raise Exception("Can't Pop: Queue is empty")
        
        temp= self.peek()
        self.top -= 1
        return temp
        
class Queue:
    
    def __init__(self, size):
        self.stackOne = Stack(size)
        self.stackTwo = Stack(size)
        
        
    def isFull(self):
        return self.stackOne.isFull()
        
    def isEmpty(self):
        return self.stackOne.isEmpty()
        
    def enqueue(self, data):
        self.stackOne.push(data)
        
        
    def dequeue(self):
    
        while not self.stackOne.isEmpty():
            self.stackTwo.push(self.stackOne.pop())
          
        self.stackOne.stack.clear()   # Clearing actual stack, else it will append after existing elements
        temp = self.stackTwo.peek()
        
        self.stackTwo.pop()

        while not self.stackTwo.isEmpty():
            self.stackOne.push(self.stackTwo.pop())
        self.stackTwo.stack.clear()  
            
        return temp
 
    def display(self):
                
        temp_top = self.stackOne.top
        
        if self.isEmpty():
            return -1, print("Stack is Empty")
            
        while temp_top != -1:
            print(self.stackOne.stack[temp_top], end=" ")
            temp_top -= 1
        print()
        
    
    
q1 = Queue(3)

q1.enqueue(10)
q1.enqueue(20)
q1.enqueue(30)

print("==Original Queue==")
q1.display()

print("==Dequeue==")
q1.dequeue()
q1.display()

print("==Enqueue==")
q1.enqueue("new")
q1.display()

print("==Dequeue==")
q1.dequeue()
q1.display()

print("==Dequeue==")
q1.dequeue()
q1.display()


print("==Enqueue==")
q1.enqueue("new1")
q1.display()    