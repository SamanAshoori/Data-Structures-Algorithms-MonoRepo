#Welcome to the Stack Implementation in Python
class Stack:
    def __init__(self, height):
        self.height = height
        self.top = -1
        self.data = []
    
    def push(self,x):
        if(self.top == (self.height - 1)):
            print('stack is full')
        else:
            self.top = self.top + 1
            self.data.insert(self.top, x)
            #Note for Python you can just use self.data.append(x) - however I wanted to keep the logic similar to other languages
    
    def pop(self):
        if(self.top == -1):
            print('nothing to pop')
        else:
            #save the value so I can run the logic and still return the value
            returned_value = self.data[self.top]
            del self.data[self.top]
            self.top = self.top - 1
            return returned_value
            #note in Python you can just use self.data.pop() - same as above
    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False
        
    def peek(self):
        return  str(self.data[self.top])
    
    def display(self):
        if(self.top == -1):
            return('stack is empty')
        else:
           return self.data[:self.top + 1]
    