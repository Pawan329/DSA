#we will use python list to perform stack operations

class Stack:
    def __init__(self, size):
        self.top = -1
        self.size = size
        self.stack = []
        
    def isEmpty(self):
        return self.top == -1  #if top == -1, return "TRUE" else "FALSE"
        
    def isFull(self):
        return self.top == (self.size-1)  #if top element is -1 than size of stack (because indexing starts with 0 in py List),
                                          # return "TRUE" else "FALSE"
                                          
    def insertElement(self, data):
        if self.isFull():
            print("Stack is full !, can't insert: ",data)
        else:
            self.stack.append(data)  #Append function will add data as last element of List
            # print("New element inserted in Stack: ",data)
            self.top += 1  # Moving top with one level up
            return data
    
    def deleteElement(self):
        if self.isEmpty():
            print("Can't delete, Stack is Empty !")
        else:
            top_element = self.stack[self.top]
            self.top -= 1
            return top_element
    
    def peek(self):
        if self.isEmpty():
            print("Stack is Empty!")
            
        else:
            return self.stack[self.top]
        
    def statusOfStack(self):
        print("Size: ", self.size)
        print("Space occupied: ",self.top+1 )
        print("Space left: ", (self.size - self.top-1))
            
    def display(self):
        temp = self.top
        while temp != -1:
            print(self.stack[temp], end=" ")
            temp -= 1
        print()
            
    def copyStack(self, source, target):
        temp = self.top
        while temp != -1:
            target.insertElement(source.stack[temp])
            temp -= 1
            
    def moveStack(self, source, target):
        
        if (source.top+1) <= (target.size - target.top-1):
            while s1.top != -1:
                target.insertElement(source.peek())
                source.deleteElement()
                
        else:
            print("target stack doesn't have enough space!!")
        
    
s1 = Stack(5)
s2 = Stack(5)
s3 = Stack(5)
# print("is Stack Full? :",s1.isFull())
# print("is Stack Empty? :",s1.isEmpty())
s1.insertElement(10)
s1.insertElement(20)
s1.insertElement(30)
s1.insertElement(40)
s1.insertElement(50)
# s1.insertElement(60)
# print("Peek element of stack :",s1.peek())
# s1.statusOfStack()
# print("Element deleted: ",s1.deleteElement())
# print("Peek element of stack :",s1.peek())
print("*** S1 ***")
s1.display()

# s1.copyStack(s1, s2)
# print("*** Transfer: S1 to S2 ***")
# s2.display()

# s2.copyStack(s2, s3)
# print("*** Transfer: S2 to S3 ***")
# s3.display()

s2.moveStack(s1, s2)

print("*** S2 ***")
s2.display()

print("*** S1 ***")
s1.statusOfStack()






