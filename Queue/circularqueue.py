class CircQueue:
    def __init__(self,size:int):
        self.size = size
        self.front = -1
        self.tail = -1
        self.isEmpty = True
        self.isFull = False
        #To simulate C++ memory management
        self.data = ['None'] * size
    
    def enqueue(self,input:int) -> bool:
        #input a int but return a boolean value
        if(self.isEmpty):
            self.front = self.front + 1
            self.tail = self.tail + 1
            self.data[self.tail] = input
            self.isEmpty = False
            return True
        elif(self.isFull):
            return  False
        elif((self.tail+1) % self.size == self.front):
            return False
        else:
            self.tail = self.tail + 1
            self.data[self.tail] = input
            return True

    def dequeue(self) -> bool:
        if(self.isEmpty):
            return False
        elif(self.front == self.tail):
            self.front = -1
            self.tail = -1
            return True
        else:
            self.front = (self.front + 1) % self.size
            return True



        


q1 = CircQueue(4)
print(q1.enqueue(4))
print(q1.enqueue(2))
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
