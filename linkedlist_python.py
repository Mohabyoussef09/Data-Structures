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
    
    def linkedListLength(self):
        currentNode=self.head
        list_len=0
        while currentNode is not None:
            list_len+=1
            currentNode=currentNode.next
        return list_len
        
            
    def insertHead(self,newNode):
        tempNode=self.head
        self.head=newNode
        self.head.next=tempNode
        del tempNode
        
    def insertBetweenTwoNodes(self,node1,node2,newNode):
        node1.next=newNode
        newNode.next=node2
         
        
    def insertBetweenTwoNodesUsingPosition(self,newNode,pos):
        currentNode=self.head
        currentposition=0
        
        if pos<0 or pos>self.linkedListLength():
            print("Invalid input")
            return
        if pos is 0:
            self.insertHead(newNode)
            return
        while True:
            if currentposition==pos:
                previousNode.next=newNode
                newNode.next=currentNode
                break
            
            else:
                previousNode=currentNode
                currentNode=currentNode.next
                currentposition+=1
            
    def deleteEnd(self):
        lastNode=self.head
        while lastNode.next is not None:
            previousNode=lastNode
            lastNode=lastNode.next
        previousNode.next=None
        
    def deleteHead(self):
        t=self.head
        self.head=self.head.next
        t.next=None
        
    
    def deleteAt(self,pos):
        currentPos=0
        currentNode=self.head
        if pos<0 or pos>=self.linkedListLength():
            print("Invalid input")
            return
        if pos is 0:
            self.deleteHead()
            return
        while True:
            if currentPos==pos:
                previousNode.next=currentNode.next
                del currentNode.next
                return 
            
            else:
                currentPos+=1
                previousNode=currentNode
                currentNode=currentNode.next
                
    
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
                

linkedlist=LinkedList()                
firstNode=Node("FirstNode")
secondNode=Node("SecondNode")
thirdNode=Node("ThirdNode")

linkedlist.insert(firstNode)
linkedlist.insert(secondNode)
linkedlist.insert(thirdNode)

linkedlist.printLinkedList()
print("----------------------------")
NewHeadNode=Node("firstHead")
linkedlist.insertHead(NewHeadNode)
linkedlist.printLinkedList()

node_betweet_second_third=Node("between sec and third")
linkedlist.insertBetweenTwoNodes(secondNode,thirdNode,node_betweet_second_third)
print("----------------------------")
linkedlist.printLinkedList()


node_at_pos1=Node("node at pos 1")
linkedlist.insertBetweenTwoNodesUsingPosition(node_at_pos1,1)
print("----------------------------")
linkedlist.printLinkedList()

print("----------------------------")
print(linkedlist.linkedListLength())


linkedlist.deleteEnd()
print("----------------------------")
linkedlist.printLinkedList()


linkedlist.deleteAt(0)
print("----------------------------")
linkedlist.printLinkedList()


