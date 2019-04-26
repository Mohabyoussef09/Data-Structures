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
    
# as our Queue class is done, now lets use it
myQueue = Queue()
myQueue.enqueue(10) # return True
myQueue.enqueue(5) # return True
myQueue.enqueue("Hello") # return True

print(myQueue.size()) # return size of queue

print (myQueue.isEmpty()) # return True if empty

myQueue.show() # prints the complete queue

print (myQueue.dequeue()) # return the element removed

myQueue.show() # prints the complete queue

myQueue.reverseQueue()