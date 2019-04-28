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
    
    def BST(self): 
        # Base Case 
        if self.root is None: 
            return

        # Create an empty queue for level order traversal 
        queue = [] 
        list=[]
        # Enqueue Root and initialize height 
        queue.append(self.root) 

        while(len(queue) > 0): 
            # Print front of queue and remove it from queue 
            list.append(queue[0].val)
            node = queue.pop(0)

            #Enqueue left child 
            if node.left is not None: 
                queue.append(node.left) 

            # Enqueue right child 
            if node.right is not None: 
                queue.append(node.right) 
        
        print(list)





bt=BinarySearchTree()
bt.insert(9)
bt.insert(4)
bt.insert(6)
bt.insert(20)
bt.insert(170)
bt.insert(15)
bt.insert(1)
bt.lookup(10)
bt.BST()

