class CircQueue:
    def __init__(self,size:int):
        self.size = size
        self.front = -1
        self.tail = -1
        #To simulate C++ memory management
        self.data = ['None'] * size
    
    def enqueue(self,input:int) -> bool:
        #input a int but return a boolean value
        if((self.tail + 1) % self.size) == self.front:
            return False
        
        if self.front == -1:
            self.front = 0
        
        self.tail = (self.tail + 1) % self.size
        self.data[self.tail] = input
        return True

    def dequeue(self) -> bool:
        if self.front == -1:
            return False
        
        if self.front == self.tail:
            self.front = -1
            self.tail = -1
            return True
        
        self.front = (self.front + 1) % self.size
        return True
    
    def Front(self) -> int:
        if self.front == -1: return -1
        return self.data[self.front]
    
    def Rear(self) -> int:
        if self.tail == -1: return -1
        return self.queue[self.tail]
        
    def isEmpty(self) -> bool:
        return self.front == -1
        
    def isFull(self) -> bool:
        return ((self.tail + 1) % self.size) == self.front

        



        


q1 = CircQueue(4)
print(q1.enqueue(4))
print(q1.enqueue(2))
print(q1.dequeue())
print(q1.dequeue())
print(q1.dequeue())
