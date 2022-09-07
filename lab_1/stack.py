class st:
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
        print(self.data[len(self.data)-1])
        self.data.pop()

    def size(self):
        print(len(self.data))

    def back(self):
        self.ll  = len(self.data)
        if self.ll == 0:
            print("error")
            return 0
        print(self.data[self.ll-1])        
    
    def clear(self):
        self.data.clear()
        print('ok')    

# global stack
stack = st()

a = input()
while True:
    if a == 'size':
        stack.size()
    elif a.split()[0] == 'push':
        stack.push(a.split()[1])
    elif a == 'pop':
        stack.pop()
    elif a == 'back':
        stack.back()
    elif a == 'clear':
        stack.clear()  
    elif a == 'exit':
        print('bye')
        break
    a = input()
