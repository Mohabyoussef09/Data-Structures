class Node:
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None
        
class BinarySearchTree:
    def __init__(self):
        self.root=None
        
    def insert(self,value):
        newNode=Node(value)
        if self.root==None:
            self.root=newNode
            print(self.root.val)
            return
        currentNode=self.root
        while(True):
            if value<currentNode.val:
                if currentNode.left==None:
                    currentNode.left=newNode
                    break
                else:
                    currentNode=currentNode.left
            if value>=currentNode.val:
                if currentNode.right==None:
                    currentNode.right=newNode
                    break
                else:
                    currentNode=currentNode.right
                    
    def lookup(self,value):
        if self.root==None:
            return ''
        currentNode=self.root
        while(currentNode!=None):
            if value < currentNode.val:
                currentNode = currentNode.left
            elif value > currentNode.val:
                currentNode = currentNode.right
            elif currentNode.val == value:
                return currentNode
      
        return False
                      


bt=BinarySearchTree()
bt.insert(10)
bt.insert(20)
bt.insert(3)
bt.lookup(10)

