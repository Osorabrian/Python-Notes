# creating stack class

class Stack(object):
    
    def __init__(self):
        self.arr = []
        
    #add element to a stack
    def push(self, element):
        self.arr.append(element)
    
    #remove top element from a stack
    def pop(self):
        try:
            popped = self.arr.pop()
        except:
            print("The stack is empty")
        else:
            return popped
    
    #check the top element
    def peak(self):
        return self.arr[-1]
    
    #check if stack is empty
    def is_empty(self):
        return len(self.arr) == 0
    
    #check size of stack
    def size(self):
        return len(self.arr)
    
n = Stack()
n.push(10)
n.push(20)
n.push(30)
print(n.pop())
print(n.peak())
print(n.is_empty())
print(n.size())
    
    