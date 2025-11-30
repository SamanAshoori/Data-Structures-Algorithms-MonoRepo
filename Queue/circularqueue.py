class CircQueue:
    def __init__(self,size:int):
        self.size = size
        self.front = -1
        self.tail = -1
        self.isEmpty = True
        #To simulate C++ memory management
        self.data = ['None'] * size
    
    def enqueue(self,input:int) -> bool:
        #input a int but return a boolean value
        if(self.isEmpty == True):
            self.front = self.front + 1
            self.tail = self.tail + 1
            self.data[self.tail] = input
            self.isEmpty = False
            return True

q1 = CircQueue(4)
print(q1.enqueue(4))