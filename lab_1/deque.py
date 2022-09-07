class d:
    def __init__(self):
        self.data = []
    def push_front(self,element):
        self.element = element
        self.data.insert(0,self.element)
        print('ok')
    def push_back(self,element):
        self.element = element
        self.data.append(self.element)
        print('ok')
    def pop_front(self):
        if len(self.data) == 0:
            print('error')
            return 0
        print(self.data[0])
        self.data.pop(0)

    def pop_back(self):
        if len(self.data) == 0:
            print('error')
            return 0
        print((self.data[len(self.data)-1]))
        self.data.pop()


    def front(self):
        if len(self.data) == 0:
            print('error')
            return 0
        print(self.data[0])

    def back(self):
        if len(self.data) == 0:
            print("error")
            return 0
        print(self.data[len(self.data)-1])

    def size(self):
        print(len(self.data))

    def clear(self):
        self.data.clear()
        print('ok')

deque = d()

while True:
    a = input()
    if a == 'exit':
        print('bye')
        break
    elif a.split()[0] == 'push_front':
        deque.push_front(a.split()[1])
    elif a.split()[0] == 'push_back':
        deque.push_back(a.split()[1])
    elif a == 'pop_front':
        deque.pop_front()
    elif a == 'pop_back':
        deque.pop_back()
    elif a == 'front':
        deque.front()
    elif a == 'back':
        deque.back()
    elif a == 'size':
        deque.size()
    elif a == 'clear':
        deque.clear()