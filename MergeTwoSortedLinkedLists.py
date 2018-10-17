class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        
        
    def insert(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode=lastnode.next
            lastnode.next=newNode
            
    
    def printLinkedList(self):
        if self.head is None:
            print('')
        currentNode=self.head
        while True:
            if currentNode is None:
                break
            else:
                print(currentNode.data)
                currentNode=currentNode.next    
                
    def insert(self,newNode):
        if self.head is None:
            self.head=newNode
        else:
            lastnode=self.head
            while True:
                if lastnode.next is None:
                    break
                lastnode=lastnode.next
            lastnode.next=newNode    
    
    def  merge(self,mergedlk,lk1,lk2):
        currentFirst=lk1.head
        currentSecond=lk2.head
                
        while True:
            if currentFirst is None:
                mergedlk.insert(currentSecond)
                break
            if currentSecond is None:
                mergedlk.insert(currentFirst)
                break
            if currentFirst.data<currentSecond.data:
                mergedlk.insert(currentFirst)
                currentFirstTemp=currentFirst.next
                currentFirst.next=None
                currentFirst=currentFirstTemp
                
            else:
                mergedlk.insert(currentSecond)
                currentSecondTemp=currentSecond.next
                currentSecond.next=None
                currentSecond=currentSecondTemp                
               
        return mergedlk  
        
        
                

linkedlist1=LinkedList()                
firstNode=Node(1)
secondNode=Node(3)
thirdNode=Node(4)

linkedlist1.insert(firstNode)
linkedlist1.insert(secondNode)
linkedlist1.insert(thirdNode)

#-----------------------------
linkedlist2=LinkedList()                
firstNode=Node(2)
secondNode=Node(7)
thirdNode=Node(9)

linkedlist2.insert(firstNode)
linkedlist2.insert(secondNode)
linkedlist2.insert(thirdNode)

#-----------------------------
mergedLinkedList=LinkedList()
mergedLinkedList=mergedLinkedList.merge(mergedLinkedList,linkedlist1,linkedlist2)
print("Merged linkedLists")
mergedLinkedList.printLinkedList()