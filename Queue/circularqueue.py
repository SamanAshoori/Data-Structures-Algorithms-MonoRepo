class Queue:
    def init(self,size):
        self.size = size
        self.front = -1
        self.tail = -1
        #To simulate C++ memory management
        self.data = ['None'] * size