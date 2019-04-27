# A simple implementation of Priority Queue 
# using Queue. 
'''We can design a priority queue using two approaches 
in the first case we can add the queue element at the end of the queue
and we can remove the elements of the queue depending on the priority.
In the second case we can add elements to the queue according to the priority
and remove them from the front of the queeue.
In this code we would use the first approach to implement a Priority Queue.
'''
class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    # for checking if the queue is empty 
    def isEmpty(self): 
        return self.queue == [] 
  
    # for inserting an element in the queue 
    def insert(self, data): 
        self.queue.append(data) 
  
    # for popping an element based on Priority 
    def delete(self): 
        try: 
            max = 0
            for i in range(len(self.queue)): 
                if self.queue[i] > self.queue[max]: 
                    max = i 
            item = self.queue[max] 
            del self.queue[max] 
            return item 
        except IndexError: 
            print() 
            exit() 
  
if __name__ == '__main__': 
    myQueue = PriorityQueue() 
    myQueue.insert(12) 
    myQueue.insert(1) 
    myQueue.insert(14) 
    myQueue.insert(7) 
    print(myQueue)             
    while not myQueue.isEmpty(): 
        print(myQueue.delete())  