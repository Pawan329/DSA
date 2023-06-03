class Node:
    
    def __init__(self,value):
        self.value= value
        self.left= None
        self.right= None
        

class BTree:
    
    def __init__(self):
        self.root= None
    
    def addNode(self,current,value):
        
        if current is None:
            return Node(value)
        
        #LEFT
        if value < current.value:
            current.left= self.addNode(current.left,value)
        #RIGHT
        else:
            current.right= self.addNode(current.right,value)
        
        return current  
        
    def deleteNode(self,value):
        
        current= self.root
        prev= None
        
        while current is not None:
            
            #NODE FOUND
            if current.value == value:
                #TWO CHILD
                if current.left != None and current.right != None:
                    self.twoChild(current)
                #ONE CHILD
                elif current.left != None or current.right != None:
                    self.oneChild(prev,current)
                    
                #ZERO CHILD
                else:
                    self.zeroChild(prev,current)
                    
                
            prev= current    
            #LEFT
            if value < current.value:
                current= current.left
                
            #RIGHT
            else:
                current= current.right
    
    def zeroChild(self,parent,current):
        
        if current.value > parent.value:
            parent.right= None
        else:
            parent.left= None
    
    def oneChild(self,parent,current):
        
        #CURRENT HAS LEFT CHILD
        isLeft= False
        
        if current.left is not None:
            isLeft= True    
        #CURRENT HAS RIGHT CHILD
       
        
        if parent.left == current:
            
            if isLeft:
                parent.left= current.left
            else:
                parent.left= current.right
            
            return
        
        
        if isLeft:
            parent.right= current.left
        else:
            parent.right= current.right
            
    def twoChild(self,current):
        
        #FIND MAX IN LEFT SUBTREE
        maxVal= self.max(current.left)
        self.deleteNode(maxVal)
        current.value= maxVal
        
        
    
    def max(self,current):
        
        if current.right is None:
            return current.value
        
        return self.max(current.right)    
        
            
            
        


t1= BTree()

t1.root= t1.addNode(t1.root,50)
t1.addNode(t1.root,40)
t1.addNode(t1.root,60)
t1.addNode(t1.root,30)
t1.addNode(t1.root,25)
t1.addNode(t1.root,70)
t1.addNode(t1.root,45)
t1.addNode(t1.root,20)
t1.addNode(t1.root,65)



#ZERO CHILD
#t1.deleteNode(45)
#ONE CHILD
t1.deleteNode(70)
#TWO CHILD
t1.deleteNode(40)

print(t1.root.left.value)




