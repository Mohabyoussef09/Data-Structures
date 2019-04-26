class Node:
     def __init__(self,data):
        self.data=data
        self.next=None
        
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
        
    def insert(self,newNode):
        if self.head==None:
            self.head=self.tail=newNode
        else:
            currentNode=self.head
            while currentNode.next!=None:
                currentNode=currentNode.next
            currentNode.next=newNode
            self.tail=currentNode.next

    def printLinkedList(self):
        currentNode=self.head
        while currentNode.next!=None:
            print(currentNode.data,"-> ",end="")
            currentNode=currentNode.next
        print(currentNode.data)
    def printHead(self):
        print(self.head.data)
    def printTail(self):
        print(self.tail.data)
        
        
    def deleteFromHead(self):
        temp=self.head
        self.head=self.head.next
        del temp
    def deleteFromTail(self):
        if self.tail==None:
            return
        currentNode=self.head
        while currentNode.next!=None:
            PreviousCurrentNode=currentNode
            currentNode=currentNode.next
            
        self.tail=PreviousCurrentNode
        PreviousCurrentNode.next=None
        
    def deleteAt(self,position):
        currentPosition=0
        currentNode=self.head
        if position<0 or position>=self.linkedListLength():
            print("Invalid input")
            return
        if position is 0:
            self.deleteFromHead()
            return
        while True:
            if currentPosition==position:
                previousNode.next=currentNode.next
                del currentNode.next
                return 
            
            else:
                currentPosition+=1
                previousNode=currentNode
                currentNode=currentNode.next
        
    def insertFromHead(self,newNode):
        if self.head==None:
            self.head=newNode
        else:
            temp=self.head
            self.head=newNode
            self.head.next=temp
        
    def insertBetweenTwoNodes(self,node1,node2,newNode):
        node1.next=newNode
        newNode.next=node2
        
    def insertBetweenTwoNodesAtPosition(self,position,newNode):
        if position==0:
            self.insertFromHead(newNode)
        else:
            currentPosition=0
            currentNode=self.head
            while currentNode.next!=None:
                if currentPosition==position:
                    temp=currentNode.next
                    currentNode.next=newNode
                    newNode.next=temp
                    break
                else:
                    currentPosition+=1
                    currentNode=currentNode.next
    def linkedListLength(self):
        currentNode=self.head
        listLength=0
        while currentNode is not None:
            listLength+=1
            currentNode=currentNode.next
        return listLength
    
    def reverse(self):
        if self.head==None:
            print("Empty List")
        if self.head==self.tail:
            print(self.head.val)
            
        else:
            currentNode=self.head
            while currentNode.next!=None:
                #previousNode=currentNode
                nextNode=currentNode.next
                currentNode=nextNode.next
                nextNode.next=currentNode
                
    def reverse(self): 
        prev = None
        current = self.head 
        while(current is not None): 
            next = current.next
            current.next = prev 
            prev = current 
            current = next
        self.head = prev
                
        
        
    
        
        
lk=LinkedList()
firstN=Node(1)
secondN=Node(2)
thirdN=Node(3)
fourthN=Node(4)

lk.insert(firstN)
lk.insert(secondN)
lk.insert(thirdN)
lk.insert(fourthN)


lk.printLinkedList()
lk.deleteFromTail()
lk.printLinkedList()

lk.insertBetweenTwoNodes(secondN,thirdN,Node(10))
lk.printLinkedList()
lk.insertFromHead(Node(12))
lk.printLinkedList()
lk.insertBetweenTwoNodesAtPosition(10,Node(15))
lk.printLinkedList()
lk.insertFromHead(Node(20))
lk.printLinkedList()
lk.deleteAt(1)
lk.printLinkedList()
lk.printTail()

            
        

            
            

