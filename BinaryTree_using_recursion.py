
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def insert(self, current, data):
        # print("curret: ",current)
        
        if current == None:
            return Node(data)
            
        if data < current.data:
            current.left= self.insert(current.left,data)
    
        else:
           current.right= self.insert(current.right,data)
           
        return current
   
    
    def searchNode(self,current,data):
        
        if current is None:
            return False
        elif current.data == data:
            return True
    
        #LEFT  
        elif data < current.data:
            return self.searchNode(current.left,data)
        #RIGHT    
        else:
            return self.searchNode(current.right,data)
            
    
    def delZeroChild(self, current, prev, data):
        
        if current == None:
            print("Not found")
            
        elif current.left == None and current.right == None and current.data == data:
            
            if prev.data < current.data:
                prev.right = None
                # return prev.right
                
            else:
                prev.left = None
                # return prev.left
                
            
            
        elif data < current.data:
            prev = current
            return self.delZeroChild(current.left, prev, data)
            
        else:
            prev = current
            return self.delZeroChild(current.right, prev, data)
            
           
            
bt1 = BinaryTree()

bt1.root = bt1.insert(bt1.root, 100)
bt1.insert(bt1.root, 90)
bt1.insert(bt1.root, 80)
bt1.insert(bt1.root, 95)
bt1.insert(bt1.root, 85)
bt1.insert(bt1.root, 110)
bt1.insert(bt1.root, 115)
bt1.insert(bt1.root, 120)
# bt1.insert(bt1.root, 145)
# bt1.insert(bt1.root, 23)
# bt1.insert(bt1.root, 115)
# bt1.insert(bt1.root, 345)

# print(bt1.searchNode(bt1.root,15))

# print(bt1.root.left.right.right)

bt1.delZeroChild(bt1.root,None, 120)

print(bt1.root.right.right.right)






















