# Creating Binary Tree using recursion and Insert/ Delete Node function added

class Node:
    # Node creation
    def __init__(self,value):
        self.value= value
        self.left= None
        self.right= None
        
class BTree:
    
    # Initially Root node will created with "None" value
    def __init__(self):
        self.root= None
    
    # Add Node function, It take current as Root Node and traverse to 
    # the left or right location and insert new node according to their value
    def addNode(self,current,value):
        
        # In case of first Node current will be None
        if current is None:
            return Node(value)
        
        # LEFT - Move Current
        if value < current.value:
            current.left = self.addNode(current.left,value)
        
        #RIGHT - Move Current
        else:
            current.right= self.addNode(current.right,value)
        
        return current  
        
    def deleteNode(self,value):
        
        current = self.root
        prev = None
        
        if current == None:
            return print("Tree is Empty!")
        
        # Traverse till current will become None (Reach to leaf Node)
        while current != None:
            
            # NODE FOUND
            if current.value == value:
                
                # TWO CHILD
                if current.left != None and current.right != None:
                    self.twoChild(current)
                
                # ONE CHILD
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
                
    def zeroChild(self, parent, current):
        
        # If Parent node has greater value make Parent's Right Node as None 
        # Else - Make Left Node as None
        if current.value > parent.value:
            parent.right= None
        else:
            parent.left= None
    
    def oneChild(self, parent, current):
        
        #CURRENT HAS LEFT CHILD
        isLeft = False
        
        if current.left != None:
            isLeft = True    
        
        if parent.left == current:
           
            # If current has Node in left side
            if isLeft == True:
                parent.left = current.left
            
            # If current has Node in right side
            else:
                parent.left = current.right
            
            return
        
        # If Current has Node in left side
        if isLeft == True:
            parent.right= current.left
        
        # If current has Node in right side
        else:
            parent.right= current.right
            
    def twoChild(self,current):
        
        #FIND MAX IN LEFT SUBTREE
        maxVal= self.max(current.left)
        self.deleteNode(maxVal)
        current.value= maxVal
        
    def max(self,current):
        
        if current.right == None:
            return current.value
        
        return self.max(current.right)    
      
    # ROOT LEFT RIGHT
    def preOrderTraversal(self, current):
        
        if current is None:
            return
        print(current.value, end=" ")
        self.preOrderTraversal(current.left)
        self.preOrderTraversal(current.right)
         
    # LEFT RIGHT ROOT  
    def postOrderTraversal(self, current):
        if current is None:
            return
        self.postOrderTraversal(current.left)
        self.postOrderTraversal(current.right)
        print(current.value, end=" ")
        
    # LEFT ROOT RIGHT  
    def InOrderTraversal(self, current):
        if current is None:
            return
        self.InOrderTraversal(current.left)
        print(current.value, end=" ")
        self.InOrderTraversal(current.right)
        
        
        
        


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
# t1.deleteNode(70)
#TWO CHILD
# t1.deleteNode(40)

t1.preOrderTraversal(t1.root)
print()
t1.postOrderTraversal(t1.root)
print()
t1.InOrderTraversal(t1.root)

