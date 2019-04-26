class Stack:
     def __init__(self):
          self.items = []

     def isEmpty(self):
          return self.items == []

     def push(self, item):
          self.items.append(item)

     def pop(self):
          return self.items.pop()

     def peek(self):
          return self.items[len(self.items)-1]

     def size(self):
          return len(self.items)
     
stack1 = Stack()
stack1.push('x')
stack1.push('y')
stack1.pop()
stack1.push('z')
stack1.peek()