'''
AVL (Adelson-Velsky and Landis) Tree is a self-balancing binary search tree that 
can perform certain operations in logarithmic time. It exhibits height-balancing 
property by associating each node of the tree with a balance factor and making sure 
that it stays between -1 and 1 by performing certain tree rotations.
'''

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
        
        
    def heightOfTree(self, current):
        
        if current is None:
            return -1
        return 1 + max(self.heightOfTree(current.left), self.heightOfTree(current.right))
        
        
    def balanceFactor(self, current):
        print("Balance Factor: ", (self.heightOfTree(current.left) - self.heightOfTree(current.right)))
    
    
    # preOrderTraversal - ROOT LEFT RIGHT
    def preOrderTraversal(self, current):
        
        if current is None:
            return
        
        print("Node Value: ", current.value)
        print("Height: ",self.heightOfTree(current))
        self.balanceFactor(current)
        self.preOrderTraversal(current.left)
        self.preOrderTraversal(current.right)


        
t1= BTree()

t1.root= t1.addNode(t1.root,50)
t1.addNode(t1.root,40)
t1.addNode(t1.root,30)
t1.addNode(t1.root,45)
t1.addNode(t1.root,60)
t1.addNode(t1.root,55)
t1.addNode(t1.root,65)
t1.addNode(t1.root,62)
t1.addNode(t1.root,70)
t1.addNode(t1.root,80)

t1.preOrderTraversal(t1.root)



