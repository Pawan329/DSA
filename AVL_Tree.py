# CREATING NODE WITH GIVEN DATA

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class Btree:
    
    def __init__(self):
        self.root = None
        
    def addNode(self, current, data):
        
        if current is None:
            return Node(data)
            
        if data < current.data:
            current.left = self.addNode(current.left, data)
        else:
            current.right = self.addNode(current.right, data)
         
        #========= Balacing Tree =============== 
        
        bf = self.balanceFactor(current)
        
        if bf < -1:
            if data > current.right.data:
                return self.leftRotate(current)
                
            else:
                current.right = self.rightRotate(current.right)
                return self.leftRotate(current)
            
        elif bf > 1:
            
            if data < current.left.data:
                return self.rightRotate(current)
               
            else:
                current.left = self.leftRotate(current.left)
                return self.rightRotate(current)
            
        return current
        
    def leftRotate(self, current):
        x = current
        y = current.right
        alpha = y.left
        
        y.left = x
        x.right = alpha
        return y
        
    def rightRotate(self, current):
        x = current
        y = current.left
        alpha = y.right
        
        y.right = x
        x.left = alpha
        
        return y
        
    def heightOfNode(self, node):
        
        if node == None:
            return -1
            
        return 1+ max(self.heightOfNode(node.left), self.heightOfNode(node.right))
        
    def balanceFactor(self, current):
        
        return self.heightOfNode(current.left) - self.heightOfNode(current.right)
        
    def preorder(self,current):
        
        if current is None:
            return
        
        print(f"D: {current.data} Ht:{self.heightOfNode(current)} bf:{self.balanceFactor(current)}")
        self.preorder(current.left)
        self.preorder(current.right)

t1 = Btree()
t1.root = t1.addNode(t1.root, 5)
t1.root = t1.addNode(t1.root, 3)
t1.root = t1.addNode(t1.root, 4)


t1.preorder(t1.root)


