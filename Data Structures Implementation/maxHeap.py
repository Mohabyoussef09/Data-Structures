     
class BinHeap:
    def __init__(self):
        self.heapList = [0]
        self.currentSize = 0
        
    def insert(self,val):
        self.heapList.append(val)
        lastIndex=len(self.heapList)-1
        parentIndex=lastIndex//2
        while val<self.heapList[parentIndex]:
            self.heapList[lastIndex],self.heapList[parentIndex]=self.heapList[parentIndex], self.heapList[lastIndex]
            lastIndex=parentIndex
            parentIndex=lastIndex//2
            
    def printHeap(self):
        print(self.heapList)
        
    def delMin(self):
        self.heapList[1],self.heapList[-1]=self.heapList[-1],self.heapList[1]
        parentNodeIndex=1
        leftNodeIndex=self.heapList.index(self.heapList[parentNodeIndex])*2
        rightNodeIndex=self.heapList.index(self.heapList[parentNodeIndex])*2+1
        self.heapList[-1]-=1
        while self.heapList[parentNodeIndex]>self.heapList[leftNodeIndex] or self.heapList[parentNodeIndex]>self.heapList[rightNodeIndex]:
            if self.heapList[leftNodeIndex]<self.heapList[rightNodeIndex]:
                self.heapList[parentNodeIndex],self.heapList[leftNodeIndex]=self.heapList[leftNodeIndex], self.heapList[parentNodeIndex]
                parentNodeIndex=leftNodeIndex
            else:
                self.heapList[parentNodeIndex],self.heapList[rightNodeIndex]=self.heapList[rightNodeIndex],self.heapList[parentNodeIndex]
                parentNodeIndex=rightNodeIndex
             
            leftNodeIndex=self.heapList.index(self.heapList[parentNodeIndex])*2
            rightNodeIndex=self.heapList.index(self.heapList[parentNodeIndex])*2+1
            
            if leftNodeIndex>=self.heapList.index(self.heapList[-1]) or rightNodeIndex>=self.heapList.index(self.heapList[-1]):
                del self.heapList[-1]
                break
        
       
        return self.heapList
                
              
bh=BinHeap()
bh.insert(3)
bh.insert(4)
bh.insert(6)
bh.insert(21)
bh.insert(10)
bh.insert(7)
bh.insert(8)
bh.insert(22)
bh.insert(28)
bh.insert(13)
bh.insert(19)
bh.insert(25)
bh.insert(20)
bh.printHeap()
bh.delMin()
bh.printHeap()  
