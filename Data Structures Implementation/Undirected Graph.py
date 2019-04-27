# Undirected graph, Adjacency list implementation
class Graph:
    def __init__(self):
        self.numberOfNodes=0
        self.adjacencyList={}
        
    def addVertex(self,v):
        self.adjacencyList[v]=[]
        self.numberOfNodes+=1   
        
        
        
    def addEdge(self,v1,v2):
        self.adjacencyList[v1].append(v2)
        self.adjacencyList[v2].append(v1)      
        
        
        
    def showGraph(self):
        for v in  self.adjacencyList:
            print(v,"-->",self.adjacencyList[v])
            
    
    
    
myGraph=Graph()

myGraph.addVertex('0');
myGraph.addVertex('1');
myGraph.addVertex('2');
myGraph.addVertex('3');
myGraph.addVertex('4');
myGraph.addVertex('5');
myGraph.addVertex('6');
myGraph.addEdge('3', '1'); 
myGraph.addEdge('3', '4'); 
myGraph.addEdge('4', '2'); 
myGraph.addEdge('4', '5'); 
myGraph.addEdge('1', '2'); 
myGraph.addEdge('1', '0'); 
myGraph.addEdge('0', '2'); 
myGraph.addEdge('6', '5');
            
myGraph.showGraph()        
        
        
        

