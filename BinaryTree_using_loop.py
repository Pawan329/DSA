class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
         
class BinaryTree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        
        newNode = Node(data) # creating new Node
        
        if self.root == None: # incase of root node
            self.root = newNode
        
        else:
            current_node = self.root # holding address of root node for traversing the tree
            
            while current_node != None: # run till the last node
                prev_node = current_node # will use this address to store newnode datta because current will become None
                
                if current_node.data > data: # if new data is less than current node'data got to left node
                    current_node = current_node.left
                else:
                    current_node = current_node.right # if new data is greater than current node'data got to right node
            
            if prev_node.data > data: 
                prev_node.left = newNode # storing new node to left of current node
                
            else:
                prev_node.right = newNode # storing new node to right of current node
    
            
bt = BinaryTree()

bt.insert(100)
bt.insert(90)
bt.insert(95)
bt.insert(80)
bt.insert(85)
bt.insert(70)
bt.insert(60)
bt.insert(110)
bt.insert(105)
bt.insert(140)
bt.insert(150)

print("root Node: ", bt.root.data)
print("1st left: ", bt.root.left.data)
print("1st right: ", bt.root.right.data)
print("2nd left: ", bt.root.left.left.data)
print("2nd right: ", bt.root.right.right.data)
print("1st left's right: ", bt.root.left.right.data)
print("1st right's left: ", bt.root.right.left.data)


        
    