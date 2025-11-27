#Welcome to the Stack Implementation in Python
class Stack:
#======== class start ==========
    def __init__(self, height):
        self.height = height
        self.top = -1
        self.data = []
    
    def push(self,x):
        if(self.top == (self.height - 1)):
            print('!!!!!!   Cannot Push - stack is full  !!!!!!!!!')
        else:
            self.top = self.top + 1
            self.data.insert(self.top, x)
    
    def pop(self):
        if(self.top == -1):
            print('nothing to pop')
        else:
            del self.data[self.top]
            self.top = self.top - 1
#============ class end ===================
#27th Noveember 2025 - As I know it works and I want to use this cass elsewhere  I will comment out all the tests
"""
s1 = Stack(5)
print("====== INIT TESTING OF STACK =======" )
print(s1.height)
print(s1.top)
print(s1.data)
#test to see if it works
s1.push(12)
s1.push("42")
s1.push(True)
s1.push(1)
s1.push(2)
#Max should be achieved
print("====== Error Testing =======" )
s1.push('should output stack is full')
s1.push('should output stack is full')
s1.push('should output stack is full')
#Perfect
print("===============" )
print("height of stack is "  + str(s1.top))
print("top of stack is "  + str(s1.data[s1.top]))
print("data in stack is" + str(s1.data))
print("====== Popping Time =======" )
#Time to see if popping works now
s1.pop()
s1.pop()
print("height of stack is "  + str(s1.top))
print("top of stack is "  + str(s1.data[s1.top]))
print("data in stack is" + str(s1.data))
print("====== More Popping Below =======" )
s1.pop()
s1.pop()
s1.pop()
#Below should output error code
s1.pop()
s1.pop()
s1.pop()
"""