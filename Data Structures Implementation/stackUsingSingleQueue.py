class Queue:
  
  # queue class constructor
  def __init__(self):
    # initialise the queue
    self.queue = list()
    
  # add data element to the queue
  def enqueue(self, data):
    # check for duplicate entry
    if data not in self.queue:
      self.queue.insert(0, data)
      return True
    else:
      return False
  
  # remove the first data element from the front  
  def dequeue(self):
    # check whether there is data in queue
    if len(self.queue) > 0:
      return self.queue.pop()
    else:
      return False
   
  # check if queue is empty or not 
  def isEmpty(self):
    if len(self.queue) > 0:
      return False
    else:
      return True
  
  # return the number of elements in the queue  
  def size(self):
    return len(self.queue)
   
  # print the complete queue 
  def show(self):
    print (self.queue)
    
  def reverseQueue(self):
    print(self.queue[::-1])


class Stack:
  def __init__(self):
    self.q=Queue()
    
    
  def push(self,data):
    self.q.enqueue(data)
    
  def pull(self):
    for __ in range(len(self.q.queue)-1):
      dequeue=self.q.dequeue()
      self.q.enqueue(dequeue)
    return self.q.dequeue()
  
  def show(self):
    print(self.q.queue)
      
  
s=Stack()
s.push(1)
s.push(10)
s.push(20)
s.pull()
s.show()
    
  
  