class q:
    def __init__(self):
        self.data = []
    
    
    
    def push(self,element):
        self.element = element
        self.data.append(self.element)
        print('ok')
        
        
    def pop(self):
        if len(self.data) == 0:
            print('error')
            return 0
        print(self.data[0])
        self.data.pop(0)
    
    
    def front(self):
        if len(self.data) == 0:
            print('error')
            return 0
        print(self.data[0])
    
    
    def size(self):
        print(len(self.data))
        
    def clear(self):
        self.data.clear()
        print('ok')



queue = q()

while True:
    a = input()
    if a == 'exit':
        print('bye')
        break
    elif a.split()[0] == 'push':
        queue.push(a.split()[1])
    elif a == 'pop':
        queue.pop()
    elif a == 'front':
        queue.front()
    elif a == 'size':
        queue.size()
    elif a == 'clear':
        queue.clear()
                                                   